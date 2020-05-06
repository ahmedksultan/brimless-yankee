import csv
import string
import sys

globalTerrorism = []
with open('./data/global-terrorism.csv', newline='') as globalTerrorismCsv:
    reader = csv.DictReader(globalTerrorismCsv, delimiter=',')
    for row in reader:
        globalTerrorism.append(row)


happiness = []
with open('./data/happiness.csv', newline='') as happinessCsv:
    reader = csv.DictReader(happinessCsv, delimiter=',')
    for row in reader:
        happiness.append(row)


humanFreedomIndex = []
with open('./data/human-freedom-index.csv', newline='') as humanFreedomIndexCsv:
    reader = csv.DictReader(humanFreedomIndexCsv, delimiter=',')
    for row in reader:
        humanFreedomIndex.append(row)


unemployment = []
with open('./data/unemployment.csv', newline='') as unemploymentCsv:
    reader = csv.DictReader(unemploymentCsv, delimiter=',')
    for row in reader:
        unemployment.append(row)


universityRankings = []
with open('./data/uni-rankings.csv', newline='') as universityRankingsCsv:
    reader = csv.DictReader(universityRankingsCsv, delimiter=',')
    for row in reader:
        universityRankings.append(row)

