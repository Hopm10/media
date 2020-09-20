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

    Thử giá trị với N = 100, r = 10 và p = 1/2 thì sum = 0.9990234374999999
    Thử giá trị với N = 1000, r = 10 và p = 1/2 thì sum = 0.9990234374999999

    ------------------------  
'''
def sumProb(N,p,r):
    sum = 0
    for i in range(r, N):
        sum = sum + prob(i, p, r)
    return sum
print(sumProb(100,0.5,2))



'''
    Function approxEntropy:
    --------------------------
    
    Giá trị thực nghiệm N = 100, r = 10 và p = 1/2 => entropy = 2.2095372252496435
    Giá trị thực nghiệm N = 200, r = 50 và p = 1/2 => entropy = 2.7370440698853584

    --------------------------
'''
def approxEntropy(N,p,r):
    
    entropy = 0
    for i in range(r,N):
        entropy = entropy + prob(i,p,r)*infoMeasure(i,p,r)
    return entropy
# print(approxEntropy(200,0.5,50))
