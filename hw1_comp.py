from typing import SupportsComplex
import numpy as np
import csv
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
    res = []
    query_id = 0
    for query in data:
        res.append([query_id+1])
        res[query_id].append(len(query))
        res[query_id].append(len(query)/10)
        query_id += 1
        dsquares = []
        n = len(query)
        for match in query:
            d = match[0] - match[1]
            dsquare = d**2
            dsquares.append(dsquare)
        if n == 1 or n == 0:
            if match[0] == match[1]:
                coefficient = 1
                res[query_id - 1].append(coefficient)
            else:
                coefficient = 0
                res[query_id - 1].append(coefficient)
        else:
            coefficient = 1 - 6*sum(dsquares) / (n * (n**2 - 1))
            res[query_id - 1].append(coefficient)
    avgOverlap, avgPercent, avgCoefficient, overlapSum, sumPercent, sumCoefficient = 0, 0, 0, 0, 0, 0

    for column in range(100):
        overlapSum += res[column][1]
    avgOverlap = overlapSum/100
    for column in range(100):
        sumPercent += res[column][2]
    avgPercent = sumPercent/100
    for column in range(100):
        sumCoefficient += res[column][3]
    avgCoefficient = sumCoefficient/100
    res.append(['Averages', avgOverlap, avgPercent, avgCoefficient])
    return res


def write_csv(data, filename):
    # file = open(path, 'w', encoding='UTF8', newline='')
    fields = ['Queries', 'Number of Overlapping Results',
              'Percent Overlap', 'Spearman Coefficient']
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(data)


results = findURLMatches(duckduckgo_json, google_json)
res = spearman_cofficient(results)
write_csv(res, 'hw1.csv')
