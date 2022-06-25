data = input()

result = int(data[0])

for i in range(1, len(data)):
    n = int(data[i])

    if n <= 1 or result <=1:
        result += n
    else :
        result *= n

print(result)