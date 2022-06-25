n = 1260
cnt = 0

array = [500,100,50,10]

for coin in array:
    cnt += n // coin
    n %= coin

print(cnt)