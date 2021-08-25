# functions to calculate sums over time
# 
# source:
# https://qrc.depaul.edu/studyguide2009/notes/savings%20accounts/compound%20interest.htm

def compound(initial, interest, rate, years):
    # returns final value after specific interest rate and time
    # initial = original amount
    # interest = annual rate of interest as a decimal
    # rate = how often interest is compounded per year
    # years = how long will interest impact

    final = 1.0 + interest/rate
    final = final**(rate*years)
    final = initial*final

    return final

