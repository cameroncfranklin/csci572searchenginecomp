import json
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
            time.sleep(randint(5, 10))
        # for adding + between words for the query
        temp_url = '+'.join(query.split())
        url = 'https://www.duckduckgo.com/html/?q=' + temp_url
        soup = BeautifulSoup(requests.get(
            url, headers=USER_AGENT).text, "html.parser")
        new_results = SearchEngine.scrape_search_result(soup)
        return new_results

    @staticmethod
    def scrape_search_result(soup):
        raw_results = soup.find_all("a", attrs={"class": "result__a"})
        results = []
    # implement a check to get only 10 results and also check that URLs must not be duplicated
        limitResults = 10
        if len(raw_results) < 10:
            limitResults = len(raw_results)
        for result in range(0, limitResults):
            if raw_results[result] not in results:
                link = raw_results[result].get('href')
                results.append(link)
        return results

#############Driver code#############


def main():
    DuckDuckGo = SearchEngine()
    with open("/Users/Cameron/Desktop/Homework 2022/CSCI 572/100QueriesSet4.txt") as f:
        lines = f.read().splitlines()
    data = {}
    for query in lines:
        data[query.rstrip()] = DuckDuckGo.search(query)
    json_dump = json.dumps(data)
    with open('hw1.json', 'w') as outfile:
        outfile.write(json_dump)


if __name__ == '__main__':
    main()
