#!/usr/bin/env python3

#import pandas
# df = pandas.read_cvs("filz/cbt_exporter/m8l1_info.cvs")
# print(df)

import csv

f = open("cbt_exporter\\m8l1_info.csv")
csv_f = csv.reader(f)
for row in csv_f:
    # unpacks back into rows, think excel spreadsheet
    slideID, title, narration, layout, darkTheme, audio, cuePoint, optionalText = row
    #row[0] for name
    print("slideID: {}\n, title: {}\n, narration: {}\n, layout: {}\n, darkTheme: {}\n, audio: {}\n, cuePoint: {}\n, optionalText: {}\n\n".format(slideID, title, narration, layout, darkTheme, audio, cuePoint, optionalText))

f.close()

