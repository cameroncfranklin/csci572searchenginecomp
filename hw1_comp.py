import json


duckduckgoResults = open(
    '/Users/Cameron/Desktop/Homework 2022/CSCI 572/hw1.json')
duckduckgo_json = json.load(duckduckgoResults)
googleResults = open(
    "/Users/Cameron/Desktop/Homework 2022/CSCI 572/Google_Result4.txt")
google_json = json.load(googleResults)


def findURLMatches(json1, json2):
    matches = []
    for query in json1:
        temp = []
        length = len(json1[query])
        for url in range(length):
            if json1[query][url] in json2[query]:           # Found match
                temp.append([json2[query].index(
                    json1[query][url]) + 1, url + 1])
        matches.append(temp)
    return matches


def spearman_cofficient(data):
    for query in data:
        n = len(query)
        for match in query:
            d = match[0] - match[1]
            dsquare = d**2
            if n == 1:
                if match[0] == match[1]:
                    coefficient = 1
                else:
                    coefficient = 0
            else:
                coefficient = 1 - 6*dsquare / (n * (n**2 - 1))
            match.append(coefficient)
    print(data)


def avg_spearman_coefficent(ranking1, ranking2):
    d = []
    n = len(ranking1)
    for rank in range(len(ranking1)):
        d.append(ranking2[rank] - ranking1[rank])
    dsquare = [x**2 for x in d]
    dsquare_sigma = sum(dsquare)
    coefficient = 1 - 6*dsquare_sigma / (n * (n**2 - 1))
    return coefficient


results = findURLMatches(duckduckgo_json, google_json)
spearman_cofficient(results)
