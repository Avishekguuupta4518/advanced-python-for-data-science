def simpleInterest(p,t,r):
    return(p*t*r)/100

def compoundInterest(p,t,r):
    return p*((1+r/100)**t) -p


if __name__ == "__main__":
    p = float(input("Enter Principal : "))
    t = float(input("Enter Time : "))
    r = float(input("Enter rate : "))
    
    print(f'Simmple Interest is {simpleInterest(p,t,r):.3f}')
    print(f'Compound Interest is {compoundInterest(p,t,r):.3f}')
    