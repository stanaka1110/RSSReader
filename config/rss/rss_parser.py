import feedparser

def parse(url):
    feed = feedparser.parse(url)
    article_list = [{'url': e['link'], 'title': e['title']} for e in feed['entries']]
    return article_list

