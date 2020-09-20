import math
def prob (n,p):
    return (p*(math.pow(1-p,n-1)))

def infoMeasure(n,p):
    return (-math.log2(prob(n,p)))
# print(infoMeasure(3,0.5))


'''
    Function sumProb:
    ------------------------
    Nếu N tiến đến vô cùng thì sumProb trả về tổng của một cấp số nhân
    Khi đó giá trị sum = p/(1-q) với |q|< 1
    Mà 1 - q = p 
    => giá trị cuối cùng là 1
    ------------------------
    
'''
def sumProb(N,p):
    i = 1
    sum = 0
    while(i <= N):
        sum = sum + prob(i,p)
        i += 1
    return sum
# print(sumProb(100,0.5))



'''
    Function approxEntropy:
    --------------------------
    Giá trị thực nghiệm N = 100 hoặc 1000 và p = 1/2 thì entropy xấp xỉ 1.99999999999999
    --------------------------
'''
def approxEntropy(N,p):
    i = 1
    entropy = 0
    while(i <= N):
        entropy = entropy + prob(i,p)*infoMeasure(i,p)
        i += 1
    return entropy
# print(approxEntropy(100,0.5))