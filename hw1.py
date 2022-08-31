import time
from bs4 import BeautifulSoup
import requests
from random import randint
from html.parser import HTMLParser
USER_AGENT = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


class SearchEngine:
    @staticmethod
    def search(query, sleep=True):
        if sleep:  # Prevents loading too many pages too soon
            time.sleep(randint(7, 35))
        # for adding + between words for the query
        temp_url = '+'.join(query.split())
        url = 'https://www.duckduckgo.com/html/?q=' + temp_url
        soup = BeautifulSoup(requests.get(
            url, headers=USER_AGENT).text, "html.parser")
        new_results = SearchEngine.scrape_search_result(soup)

        print(query, new_results)

    @staticmethod
    def scrape_search_result(soup):
        raw_results = soup.find_all("a", attrs={"class": "result__a"})
        results = []
    # implement a check to get only 10 results and also check that URLs must not be duplicated
        for result in raw_results:
            link = result.get('href')
            results.append(link)
        return results

#############Driver code#############


def main():
    DuckDuckGo = SearchEngine()
    with open("/Users/Cameron/Desktop/Homework 2022/CSCI 572/100QueriesSet4.txt") as f:
        lines = f.readlines()
    # print(lines)
    for query in lines:
        DuckDuckGo.search(query)


if __name__ == '__main__':
    main()
