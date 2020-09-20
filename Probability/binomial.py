import math

def prob (n,p,N):
    return (math.comb(N,n)*math.pow(p,n)*math.pow(1-p,N-n))
# print(prob(3,0.5,6))

def infoMeasure(n,p,N):
    return (-math.log2(prob(n,p,N)))
# print(infoMeasure(5,0.5,7))



'''
    Function sumProb:
    ------------------------
    Thử giá trị với N = 100 hoặc 1000 và p = 1/2 thì sum ~ 1
    ------------------------  
'''
def sumProb(N,p):
    sum = 0
    for i in range(1, N):
        sum = sum + prob(i, p, N)
    return sum
# print(sumProb(100,0.5))



'''
    Function approxEntropy:
    --------------------------

    Giá trị thực nghiệm N = 100 và p = 1/2 => entropy = 4.369011409223017
    Giá trị thực nghiệm N = 200 và p = 1/2 => entropy = 4.869020643912809

    --------------------------
'''
def approxEntropy(N,p):
    
    entropy = 0
    for i in range(1,N):
        entropy = entropy + prob(i,p,N)*infoMeasure(i,p,N)
    return entropy
# print(approxEntropy(200,0.5))
