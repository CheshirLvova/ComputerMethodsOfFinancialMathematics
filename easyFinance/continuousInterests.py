from math import e
from math import exp
from math import log as ln
def continuousSum(p,delta,n):
    S=p*2.7**(delta*n)
    return round(S,2)
def continuousRate(i):
    delta=ln(1+i)
    return delta
def rate_from_contimuousRate(sigma):
    i=2.7**(sigma)-1
    return i
def get_P_from_countinuousSum(s,sigma,n):
    P=s/2.7**(sigma*n)
    return round(P,2)
