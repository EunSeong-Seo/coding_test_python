'''
문제3. 드론 구매하기

입력으로 드론의 수(N<200,000)와 드론판매대의 모델을 차례대로 제공
판매 규칙 #1 : 드론이 판매대에 일렬로 전시되어있고 이중에 같은 모델은 같은 숫자임 ex) 3 3 1 1 1 
판매 규칙 #2 : 이어서 사야한다 예를들어 1번과 3번이 마음에 든다고 1번과 3번을 살수 있는것이 아니라 1 2 3 이렇게 이어서 사야함 
판매 규칙 #3 : 같은 모델을 살수 없음 

(예시)
[입력]
5
3 3 1 1 1

 [출력]
6

위의 예제에선 각모델 한개씩사기→ 5가지 , 3 1 → 1개 = 총 6개의 구매방법

문제3 은 3중 for문으로 풀수 있으나 시간초과로 탈락. 고로 이진탐색을 사용해야함
'''

n = int(input())
drons = list(map(int, input().split()))

result = 0

start= 0
end = n

while start != n-1:
    exit = False
    lst = drons[start:end]
    for i in range(len(lst)):
        if lst.count(lst[i]) >=2:
            exit = True
            break
    if exit == False:
        result+=1
    end -=1
    if start == end:
        end = n
        start +=1

print(result+1)
