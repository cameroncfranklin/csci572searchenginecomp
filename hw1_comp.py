import json


duckduckgoResults = open(
    '/Users/Cameron/Desktop/Homework 2022/CSCI 572/hw1.json')
duckduckgo_json = json.load(duckduckgoResults)
googleResults = open(
    "/Users/Cameron/Desktop/Homework 2022/CSCI 572/Google_Result4.txt")
google_json = json.load(googleResults)
# print(f'DuckDuckGo results: {duckduckgo_json} Google Results: {google_json}')

res = []
googleRanking = []
for query in duckduckgo_json:
    counter = 0
    length = len(duckduckgo_json[query])
    for anchor in range(length):
        if duckduckgo_json[query][anchor] in google_json[query]:
            counter += 1
            googleRanking.append(google_json[query].index(
                duckduckgo_json[query][anchor]))
    res.append([anchor, counter, counter/10])

print(res)
print(googleRanking)
