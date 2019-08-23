#this algorithm prints out all the primes smaller than the input number
#works best when number is small

def Sieve(number):

    prime = [True for i in range(number+1)]  #list of n numbers in which all numbers are initially prime
    p = 2   #smallest prime number

    while(p*p<=number):
        
        if prime[p] == True:  #if the number hasn't been already cut off
            for i in range(p*p, number+1, p):  #iterate over all the multiples of p
                prime[i] = False              #and mark them false because they are not primes
            
        p += 1   

    for i in range(2, number+1):
        if prime[i]:   #if the number is still not cut off
            print(i)   #then it's a prime


n = int(input())
Sieve(n)


#The time complexity of this algorithm is O(nlog(logn))