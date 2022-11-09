import requests
import time
from parsel import Selector


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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
