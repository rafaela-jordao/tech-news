from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(query)
    return [(new["title"], new["url"]) for new in news]


# Requisito 7
def search_by_date(date):
    try:
        format_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        news = search_news({"timestamp": format_date})
        return [(new["title"], new["url"]) for new in news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    tag_name = {"tags": {"$regex": tag, "$options": "i"}}
    news = search_news(tag_name)
    return [(new["title"], new["url"]) for new in news]


# Requisito 9
def search_by_category(category):
    category_name = {"category": {"$regex": category, "$options": "i"}}
    news = search_news(category_name)
    return [(new["title"], new["url"]) for new in news]
