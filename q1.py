def getPrimeNumbers(n):
    oldList = []
    for i in range(2, n+1):
        oldList.append(i)

    print(oldList)
    newlist = [x for x in oldList if isPrime(x)]
    print(newlist)
    return newlist
        

def isPrime(n):
    devisible = 0
    for i in range(2, n):
        if n%i == 0:
            devisible+=1
    return True if devisible == 0 else False 

getPrimeNumbers(4)