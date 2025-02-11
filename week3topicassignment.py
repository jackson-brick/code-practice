import csv
import pandas as pd
import matplotlib.pyplot as plot

print("I am doing prompt 4")

hours = 0
minutes = 0

movieDataTime = []
with open('movieData.csv','r') as file:
    movieData = csv.DictReader(file)
    for line in movieData:
        hoursCaptured = False
        x = ""
        y = ""
        for char in line["runTime"]:
            if hoursCaptured == False:
                if char == "h":
                    hours = int(x)
                    hoursCaptured = True
                elif char == " ":
                    pass
                else:
                    x += char
            else:
                if char.isdigit():
                    y += char
        hours = int(x) * 60
        minutes = int(y) + hours
        movieDataTime.append(minutes)

print(movieDataTime)
#movieDataPD = pd.csv_read('movieData.csv')
plot.hist(movieDataTime,edgecolor = "red",bins=30)
plot.savefig('topicassignment.png')

