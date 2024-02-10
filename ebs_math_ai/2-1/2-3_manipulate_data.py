import csv

WEEK_SIZE = 7
HOUR_SIZE = 24

data = [[] for _ in range(WEEK_SIZE)]

with open('passby_data.csv', 'r') as f :
    reader = csv.DictReader(f)
    day = 0
    hour = 0
    for row in reader :        
        data[day].append(row)
        hour += 1
        if hour % HOUR_SIZE == 0 :
            day += 1

hourTitle = []

avgPersonNumber = []
womanNumber = []
ageGroup = []

floatingPopulation = [242, 256, 237, 223, 263, 81, 46]
personBelow30Number = []
personOver30Number = []

for hour in range(HOUR_SIZE):
    hourTitle.append("{:02}".format(hour))
    sum = [0] * 3

    for day in range(WEEK_SIZE):
        sum[0] = sum[0] + int(data[day][hour]['num'])
        sum[1] = sum[1] + int(data[day][hour]['wnum'])
        sum[2] = sum[2] + int(data[day][hour]['ynum'])
        
    avgPersonNumber.append(sum[0] / WEEK_SIZE)
    womanNumber.append(sum[1] / WEEK_SIZE)
    ageGroup.append(sum[2] / WEEK_SIZE)
    
    personBelow30Number.append(sum[2])
    personOver30Number.append(sum[0] - sum[2])

# for hour in range (0, HOUR_SIZE) :
#     print("[~{0}:00]: {1:4}".format(hourTitle[hour], int(avgh[hour])))

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontName = font_manager.FontProperties(fname="C:/Users/parad/AppData/Local/Microsoft/Windows/Fonts/D2Coding-Ver1.3.2-20180524.ttf").get_name()
rc('font', family=fontName)

plt.figure()
plt.title("시간당 지나간 행인 수", fontsize = 16)
plt.xlabel("시간", fontsize = 10)
plt.ylabel("행인수", fontsize = 12)

# 평균 행인의 수
plt.scatter(hourTitle, avgPersonNumber)
plt.plot(hourTitle, avgPersonNumber)

# 평균 여성의 수
plt.scatter(hourTitle, womanNumber, c = "green")
plt.plot(hourTitle, womanNumber, c = "green")

# 평균 30대 이하의 행인의 수
plt.scatter(hourTitle, ageGroup, c = "red")
plt.plot(hourTitle, ageGroup, c = "red")

plt.figure()
plt.title("시간당 지나간 행인 수", fontsize = 16)
plt.xlabel("시간", fontsize = 10)
plt.ylabel("행인수", fontsize = 12)

# 30대 이하의 행인 수
plt.scatter(hourTitle, personBelow30Number)
plt.plot(hourTitle, personBelow30Number)

# 30대 이상의 행인 수
plt.scatter(hourTitle, personOver30Number, c = "red")
plt.plot(hourTitle, personOver30Number, c = "red")

plt.show()



