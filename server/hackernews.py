import requests
from bs4 import BeautifulSoup


def request_articles(url):
    return requests.get(url)


def get_article_information(page):
    soup = BeautifulSoup(page, 'html.parser')
    return soup


def get_attributes(soup, class_name):
    return soup.select(class_name)


def sort_list(articles):
    return sorted(articles, key=lambda k: k['votes'], reverse=True)


def get_articles(links, subtext):
    articles = []
    for index, item in enumerate(links):
        title = item.get_text()
        link = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].get_text().replace(' points', ''))
            if points > 99:
                articles.append({"title": title, "link": link, "votes": points})
    return sort_list(articles)


def main():
    page1 = request_articles('https://news.ycombinator.com/news')
    page2 = request_articles('https://news.ycombinator.com/news?p=2')
    all_text = page1.text + page2.text
    soup = get_article_information(all_text)
    links = get_attributes(soup, '.storylink')
    subtext = get_attributes(soup, '.subtext')
    articles = get_articles(links, subtext)
    return articles


if __name__ == '__main__':
    main()
