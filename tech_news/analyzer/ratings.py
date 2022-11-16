from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    top_news = get_collection().find({})
    news = top_news.sort([("comments_count", -1), ("title", 1)])
    return [(new["title"], new["url"]) for new in news[:5]]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
