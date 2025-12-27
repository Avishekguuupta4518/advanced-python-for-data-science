# from module import *
# from module import simpleInterest, compoundInterest
import module

p = float(input("Enter Principal : "))
t = float(input("Enter Time : "))
r = float(input("Enter rate : "))
    
print(f'Simmple Interest is {module.simpleInterest(p,t,r):.3f}')
print(f'Compound Interest is {module.compoundInterest(p,t,r):.3f}')