from math import e
from math import exp
from math import log as ln
def continuousSum(p,delta,n):
    S=p*exp(delta,n)
    return S
def continuousRate(i):
    delta=ln(1+i)
    return delta
def rate_from_contimuousRate(sigma):
    i=exp(sigma)-1
    return i
def get_P_from_countinuousSum(s,sigma,n):
    P=s/exp(sigma*n)
    return P
