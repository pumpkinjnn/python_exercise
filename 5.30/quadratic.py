import math

def quadratic(a,b,c):
    sol1 = (-b + math.sqrt(b*b-4*a*c))/2*a
    sol2 = (-b - math.sqrt(b*b-4*a*c))/2*a
    return sol1, sol2 
