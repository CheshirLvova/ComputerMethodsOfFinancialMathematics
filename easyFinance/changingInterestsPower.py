from math import exp
from math import log as ln
def linear_rate_power(sigma,a,n):
    apst=sigma*n+a*n*n/2
    return apst

def exp_rate_power(sigma,a,n):
    apst=sigma*(a**n-1)/ln(a)
    return apst

def accrued_amount(P,apst):
    S=P*2.7**(apst)
    return round(S,2)

def cost(S,apst):
    P=S/(2.7**(apst))
    return round(P,2)
