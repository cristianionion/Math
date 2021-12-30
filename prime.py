# function takes an integer and determines if it is a prime number
# run time should be Theta(n)

def prime(n):
    factors = []
    for i in range(n+1):
        if (n%(i+1))==0:
            factors.append(i)

    return len(factors) <= 2