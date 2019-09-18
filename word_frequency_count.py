import os
import re
import sys
import csv
with open('filter.txt') as f:
    filters = f.readlines()
# filters = [x.strip() for x in filters]
filters = [x.lower() for x in filters]
# filters = list(set(filters))
print(filters)
#opening patent.text
text = open("patent.txt", "r")
d = dict()
for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word in d:
           d[word] = d[word] + 1
        else:
           d[word] = 1

#for outputting on interface
for key in list(d.keys()):
    print(key, ":", d[key])

#for outputting on notepad
with open('finalquery.txt', 'w') as f:
     for key in list(d.keys()):
         dic=(key, ":", d[key])
         f.write(str(dic))

#for outputting on csv file
w = csv.writer(open("output.csv", "w"))
for key, d[key] in d.items():
    w.writerow([key, d[key]])
