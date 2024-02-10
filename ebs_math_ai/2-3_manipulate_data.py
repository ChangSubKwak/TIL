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
avgh = []

for hour in range(HOUR_SIZE):
    daySum = 0
    hourTitle.append("{:02}".format(hour))
    for day in range(WEEK_SIZE):
        daySum = daySum + int(data[day][hour]['num'])  # i번째 요일에 j번째 시간대별 행인수 누적하기
    avgh.append(daySum / WEEK_SIZE)

# for hour in range (0, HOUR_SIZE) :
#     print("[~{0}:00]: {1:4}".format(hourTitle[hour], int(avgh[hour])))

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontName = font_manager.FontProperties(fname="C:/Users/parad/AppData/Local/Microsoft/Windows/Fonts/D2Coding-Ver1.3.2-20180524.ttf").get_name()
rc('font', family=fontName)

plt.title("시간당 지나간 행인 수", fontsize = 16)
plt.xlabel("시간", fontsize = 10)
plt.ylabel("행인수", fontsize = 12)

plt.scatter(hourTitle, avgh)
plt.plot(hourTitle, avgh)
plt.show()
