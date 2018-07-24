from itertools import tee, islice, chain 
import re
import csv

def previous_and_next(iterable):
    prevs, items, nexts =  tee(iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)







# def getLines(textfile):
#     listContainer = []
#     with open(textfile) as f:
#         for line in f:
#             listContainer.append(line)
#             # line = line[:-1]
#             # breaks = line.split(" ")
#             # for word in breaks:
#             #     if word != '':
#             #         listContainer.append(word)
#         return listContainer


# longLines2018 = getLines("output_2018.txt")
# longLines2017 = getLines("output_2017.txt")

# titles2017=[]

def getTitles(textfile, year):
    title_years = []
    with open(textfile) as f:
        for previous, item, nxt in previous_and_next(f):
            if year == 2015:
                for word in item.split(" "):
                    if re.search('\w+', word) != None:
                        word = re.search('\w+', word).group(0)
                        title_years.append(word)
                test = None
            elif year == 2017:
                test = re.search(':\d\d[ap]m\s', item)
            elif year == 2018:
                test = re.search('\d+\s[ap]m\s+\w+day,\s\w+\s\d+', item)
            if test != None:
                for word in nxt.split(" "):
                    if re.search('\w+', word) != None:
                        title_years.append(word)
    return title_years


titles2015 = getTitles('output_2015.txt', 2015)
titles2017 = getTitles("output_2017.txt", 2017)
titles2018 = getTitles("output_2018.txt", 2018)


def getCounts(listOfWords):
    yearDict = {}
    for previous, item, nxt in previous_and_next(listOfWords):
        item = re.search('\w+', item).group(0)
        if item == 'ArcGIS' or item == 'Story' or item == 'Machine':
            nxt = re.search('\w+', nxt).group(0)
            item = item + ' ' + nxt
        if item == 'for' and previous == 'ArcGIS':
            nxt = re.search('\w+', nxt).group(0)
            previous = re.search('\w+', previous).group(0)
            item = previous + " " + item + " " + nxt
        if item in yearDict:
            yearDict[item] += 1
        else:
            yearDict[item] = 1
    return yearDict

dict2017 = getCounts(titles2017)
dict2018 = getCounts(titles2018)
dict2015 = getCounts(titles2015)

finalCount = []


for word in dict2018:
    row = [word]
    if word in dict2015:
        row.append(dict2015[word])
    else:
        row.append(" ")
    if word in dict2017:
        row.append(dict2017[word])
    else:
        row.append(" ")
    if word in dict2018:
        row.append(dict2018[word])
    finalCount.append(row)



with open('2015-17-18.csv', 'w', newline='') as newFile:
    theWriter = csv.writer(newFile, delimiter =",")
    theWriter.writerow(['word', '2015', '2017', '2018'])
    for row in finalCount:
        theWriter.writerow(row)
