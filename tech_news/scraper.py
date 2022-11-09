import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url: str, wait: int = 3):
    try:
        headers = {"user-agent": "Fake user-agent"}
        time.sleep(1)
        response = requests.get(url, timeout=wait, headers=headers)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content).css(
        "h2.entry-title a::attr(href)"
        ).getall()
    return selector


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content).css(
        "a.next.page-numbers::attr(href)"
    ).get()
    return selector


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = selector.css("div.comment-respond").getall()
    summary = selector.css(
        "div.entry-content > p:nth-of-type(1) *::text"
    ).getall()
    tags = selector.css("section.post-tags a::text").getall()
    category = selector.css("span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": len(comments_count),
        "summary": "".join(summary).strip(),
        "tags": tags,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news = []

    while len(news) < amount:
        html_content = fetch(url)
        for new in scrape_novidades(html_content):
            if len(news) == amount:
                break
            news_content = fetch(new)
            news.append(scrape_noticia(news_content))
        url = scrape_next_page_link(html_content)

    create_news(news)
    return news
