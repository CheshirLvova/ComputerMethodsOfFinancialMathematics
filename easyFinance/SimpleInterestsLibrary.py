def defaul_simple_rates(p,t,i,k):
    S=p*(1+i*t/k)
    return S
def changing_simple_rates(p,t,i,k):
    s=0
    for ti,ki,ii in zip(t,i,k):
        s+=ti*ii/ki
    S=p*s
    return S
def reinvestment_simple_rates(p,t,i,k):
    prod=1
    for ti,ki,ii in zip(t,k,i):
        prod*=1+ti*ii/ki
    S=p*prod
    return S
def simple_rates_for_time_changing_sums(r,t,i,k):
    s=0
    for ri,ti in zip(r,t):
        s+=ri*ti
    I=s*i/k
    return I
def single_time_payment(s,n,m):
    R=s/n/m
    return R
def discount_prise(s,i,t,k):
    P=s/(1+i*t/k)
    return P
def discount(s,p):
    D=s-p
    return D
def bank_accounting_rate(s,p,t,k):
    d=(s-p)/(s*t/k)
    return d
def bank_accounting(s,d,t,k):
    P=s-s*d*t/k
    return P
