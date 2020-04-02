import math

# 1단계: 데이터 정리
movie_sample = [
    (45,5,'M'),(40,10,'M'),(30,20,'M'), (25,24,'M'),
    (1,40,'A'), (10,30,'A'), (20,25,'A'),(15,30,'A')
]


# 2단계: 거리를 계산해주는 함수 만들기
def calcDistance(point1,point2):
    result = math.sqrt(math.pow(point1[0]-point2[0],2)
                       + math.pow(point1[1]-point2[1],2))
    return result

    # math.sqrt()  루트
    # math. pow() 제곱

count_kiss = int(input("키스씬의 숫자를 입력하세요"))
count_action = int(input("액션씬의 숫자를 입력하세요"))


#  3단계: 계산값을 기준으로 정렬
target = (count_kiss, count_action)
movie_sample.sort(key=lambda x : calcDistance(x,target))
print(movie_sample)

#  4단계: 3개만 뽑아서 a가 많은지 m이 많은지