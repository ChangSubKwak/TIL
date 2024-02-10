data = [242, 256, 237, 223, 263, 81, 46]

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# D2 코딩
fontName = font_manager.FontProperties(fname="C:/Users/parad/AppData/Local/Microsoft/Windows/Fonts/D2Coding-Ver1.3.2-20180524.ttf").get_name()
rc('font', family=fontName)

xData = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN'] # x축에 표시할 문구

weekdaySize = 5
weekdaySum = 0
weekdayAvg = 0

for i in range(weekdaySize):
    weekdaySum = weekdaySum + data[i]

weekdayAvg = weekdaySum / weekdaySize     # 주중 유동 인구 평균 구하기

print(f"weekday Data = {data[0:5]}")
print(f"weekday Sum : {weekdaySum}")
print(f"weekday Average : {weekdayAvg}")

plt.title("주중 유동 인구 데이터", fontsize = 16)    # 큰 제목
plt.xlabel("요일", fontsize=12)                      # x축 제목 
plt.ylabel("유동 인구수", fontsize=12)               # y축 제목


plt.plot(xData, data)                                # 꺽은선 그래프 그리기 
plt.scatter(xData[0:weekdaySize], data[0:weekdaySize], c = 'red', edgecolor = 'none', s = 50)  # 점찍기 c 는 색, s 점의 크기

plt.show()
