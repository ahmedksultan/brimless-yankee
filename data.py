# MISSING TERRORISM DATA
import csv


happiness = []
with open('./data/happiness.csv', newline='') as happinessCsv:
    reader = csv.reader(happinessCsv, delimiter=',')
    for row in reader:
        happiness.append(row)


humanFreedomIndex = []
with open('./data/human-freedom-index.csv', newline='') as humanFreedomIndexCsv:
    reader = csv.reader(humanFreedomIndexCsv, delimiter=',')
    for row in reader:
        humanFreedomIndex.append(row)


unemployment = []
with open('./data/unemployment.csv', newline='') as unemploymentCsv:
    reader = csv.reader(unemploymentCsv, delimiter=',')
    for row in reader:
        unemployment.append(row)


universityRankings = []
with open('./data/uni-rankings.csv', newline='') as universityRankingsCsv:
    reader = csv.reader(universityRankingsCsv, delimiter=',')
    for row in reader:
        universityRankings.append(row)