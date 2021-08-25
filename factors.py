# finds factor pairs of a number

def factors(n):

    factors = []
    for i in range(n//2):
        if n%(i+1) == 0:
            x = i+1
            y = int(n/(i+1))
            entry = [x,y]
            factors.append(entry)
    return factors  # returns list of 2 factors that have n as a product