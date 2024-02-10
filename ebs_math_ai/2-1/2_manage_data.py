# 데이터로부터 시간대별 평균 유동 인구수 구하기

import csv

WEEK_SIZE = 7
HOUR_SIZE = 24

data = [[] for _ in range(WEEK_SIZE)]

# data[i] = dictionary {num, wnum, ynum} : 요일별로 각 시간대에 저장할 데이터
# csv 파일에서 데이터를 읽어서 2차원 배열 data[][]에 저장 
with open('passby_data.csv', 'r') as f :
    reader = csv.DictReader(f)
    i = j = 0
    for row in reader :        
        data[i].append(row)
        j = j + 1
        if j % HOUR_SIZE == 0 :
            i += 1

hourTitle = []
avgh = []

for j in range(HOUR_SIZE):
    daySum = 0
    hourTitle.append("{:02}".format(j))
    for i in range(7):
        daySum = daySum + int(data[i][j]['num'])  # i번째 요일에 j번째 시간대별 행인수 누적하기
    avgh.append(daySum / WEEK_SIZE)

# 시간대별 평균 유동 인구 출력하기
for j in range (0, HOUR_SIZE) :
    # 시간대별 유동 인구수 출력 {1:4} --> 두번째 인자에 대해서 4칸 공간을 할당후 오른쪽 정렬 출력을 명령
    print("[~{0}:00]: {1:4}".format(hourTitle[j], int(avgh[j])))
