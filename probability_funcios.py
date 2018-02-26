from matplotlib import pyplot as plt
import numpy as np
from decimal import Decimal as d
import hashlib , binascii
from random import randint
import math

def bernoulli_trial(p):

    res = np.random.multinomial(1,[p,(1-p)])
    res = res[0]
    if res == 1: return True
    return False
        
def bernoulli_hist(p, m):
    truFals = [0,0]

    for i in range(m):
        if bernoulli_trial(p):
            truFals[1] += 1
        else:
            truFals[0] += 1
            
    truFals[0] = float(truFals[0])/m
    truFals[1] = float(truFals[1])/m
    
    plt.figure(1)

    plt.xlim(-.5,1.5)
    ax1 = plt.axes()
    ax1.set_xticks([.09, 1.0])
    ax1.set_xticklabels([0,1])
    plt.bar([0,1],truFals,0.1)
    plt.title("Bernoulli histogram")
    plt.xlabel("True/False")
    plt.ylabel("Probability")
    plt.draw()
    plt.show()
    
#bernoulli_hist(.75, 1000)




#5)

def binomial_draw(n,p):
    suc = 0
    for x in range(n):
        if bernoulli_trial(p): 
            suc += 1
    return suc
#6)
def binom_trials(n,p,numExpts):
    lis = [0]*numExpts
    for i in range(numExpts):
        lis[i] = binomial_draw(n,p)
    return lis
#7) 
def binom_hist(n,p, numExpts):
    y_coords = binom_trials(n,p,numExpts)
    
    plt.figure(1)
    plt.hist(y_coords, bins = n, rwidth = .7, align = 'mid',\
    weights = np.zeros_like(y_coords) + 1. / len(y_coords))
              
    plt.title("Binomial Histogram") 
    plt.xlabel("Bins") 
    plt.ylabel("Probability") 
    plt.draw()
    plt.show()

    
    
#binom_hist(1000, .4, 10000) 
#8)#9)
def q8():
    
    y_coords = [1,3,3,1]
    
    plt.figure(2)
    plt.bar([0,1,2,3],y_coords,color = 'r')
    plt.xlim(1)
    plt.title("Distrubution of S") 
    plt.xlabel("Prob") 
    plt.ylabel("Value") 
    plt.draw()
    plt.show()
    



def q9():
    
    y_coords = [1,8,28,56,70,56,28,8,1]
    
    plt.figure(2)
    plt.bar([0,1,2,3,4,5,6,7,8],y_coords,color = 'b')
    plt.xlim(1)
    plt.title("Distrubution of J") 
    plt.xlabel("Prob") 
    plt.ylabel("Value") 
    plt.draw()
    plt.show()
    


def q14():
    s = [0]*101
    j = [0]*201

    for i in range(101):
        # i = left steps
        
        s[i] = -2*i + 100
    for k in range(201):
        # k = left steps
        
        s[k] = -2*k + 200
        
            







#19)
def q19():
    arr = []

    with open('real_bitcoin.csv') as f:
        for line in f:
         arr += [line.split()]
         
        arr.remove([])
        arr.remove([])
        arr.remove([])
        arr.remove([])
        arr.remove([])
        arr.remove([])
        for i in range(len(arr)):
            arr[i] = arr[i][2]
        for i in range(len(arr)-1):
            arr[i] = (float(arr[i+1])- float(arr[i]))/12.5
        arr = arr[:-1]
        
        
        lamda = sum(arr)/len(arr)
        plt.figure(1)
        
        plt.hist(arr, bins = 6, rwidth = .7, align = 'mid',\
        weights = np.zeros_like(arr) + 1. / len(arr))
                  
        plt.title("Q19") 
        plt.xlabel("Bins") 
        plt.ylabel("Packets") 
        plt.draw()
        plt.show()
    
q19()
    
    
    

    
#20)
def hash_exp (num_zeros):
    
   while(1):
    s = randint(0,9999)

    hash_val = hashlib.sha256(b'wubba lubba dub dub' + str(s)).hexdigest()
    hash_val = int(hash_val,16)
    if hash_val < 2**(256 - num_zeros):
        return s
    
 

#21)
def fake_hash_exp(num_zeros):
    v1 = []
    
    for i in range(500000):
        hash_val = randint(0,2**256-1)

        if hash_val < 2**(256 - num_zeros):
            v1 += [1]
        else:
            v1 += [0]
            
    return v1
            
        
#22) + 23
def interarrival(v1):
    v2 = []
    cn = 0
    for i in range(len(v1)):
        if v1[i] == 1:
            v2 += [cn]
            cn = 0
        else:
            cn += 1
            
    plt.figure(4)
    plt.hist(v2, bins = 20, rwidth = .5, align = 'mid',\
    weights = np.zeros_like(v2) + 1. / len(v2), color = 'b')
    plt.title("Inter-arrival times")
    plt.xlabel("Times (t)")
    plt.ylabel("Probability (Pr[T = t])")
    plt.show()
    
    return v2
            
#interarrival(fake_hash_exp(6))   
    
    
  
#24)
def q24(v1):
    v3 = [0]*500
    for i in range(500):
        vk = v1[0+1000*i:1000+1000*i]
        for j in range(1000):
            if vk[j] == 1: 
                v3[i] += 1
    plt.figure(5)
    plt.hist(v3, bins = max(v3)-min(v3), rwidth = .5, align = 'mid',\
    weights = np.zeros_like(v3) + 1. / len(v3), color = 'b')
    lamda = np.mean(v3)
    plt.title("Success ")
    plt.xlabel("Successes")
    plt.ylabel("Probability")
    x = np.linspace(0, max(v3), len(v3))
    length = len(x)
    y = []
    for i in range(length):
        y += [((math.e**(-lamda))*(lamda**int(x[i])))/math.factorial(int(x[i]))]
    plt.plot(x, y, linestyle = '-', color = 'r', linewidth = 4)
    plt.draw()
    plt.show()
    
    
#q24(fake_hash_exp(6))
    
    
    

