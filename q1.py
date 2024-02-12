def getPrimeNumbers(n):
    newlist = [x for x in range(2, n+1) if isPrime(x)]
    return newlist
        

def isPrime(n):
    devisible = 0
    for i in range(2, n):
        if n%i == 0:
            devisible+=1
    return True if devisible == 0 else False 

getPrimeNumbers(6)