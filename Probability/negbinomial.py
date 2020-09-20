import math

def prob (n,p,r):
    return (math.comb(n+r-1,n)*math.pow(p,r)*math.pow(1-p,n))
# print(prob(5,0.4,5))

def infoMeasure(n,p,r):
    return (-math.log2(prob(n,p,r)))
# print(infoMeasure(5,0.5,7))



'''
    Function sumProb:
    ------------------------

    Thử giá trị với N = 100, r = 50 và p = 1/2 thì sum = 0.9999821644216893
    Thử giá trị với N = 1000, r = 50 và p = 1/2 thì sum = 0.9999999999999988

    ------------------------  
'''
def sumProb(N,p,r):
    sum = 0
    for i in range(1, N):
        sum = sum + prob(i, p, r)
    return sum
# print(sumProb(1000,0.5,50))



'''
    Function approxEntropy:
    --------------------------
    
    Giá trị thực nghiệm N = 100, r = 10 và p = 1/2 => entropy = 4.141009695863947
    Giá trị thực nghiệm N = 200, r = 50 và p = 1/2 => entropy = 5.358098129142148

    --------------------------
'''
def approxEntropy(N,p,r):
    
    entropy = 0
    for i in range(1,N):
        entropy = entropy + prob(i,p,r)*infoMeasure(i,p,r)
    return entropy
# print(approxEntropy(100,0.5,10))
# print(approxEntropy(200,0.5,50))
