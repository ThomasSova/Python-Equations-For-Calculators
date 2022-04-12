# Math Calculations
from math import *

print("a=")
a = float(input())
print("b=")
b = float(input())
print("c=")
c = float(input())

d=(b*b)-(4*a*c)
print("discimant = "+str(d))

if (d==0):
  print("1 solution)
  s1=(((b*-1)-(sqrt(d)))/((2*a)))
  print("s1= "+str(s1))
  print("Result: "+str(s1))
  print("(x+ " + str(-s1)+")")
elif d>0 :
  print("2 solutions")
  s1=(((b*-1)-(sqrt(d)))/((2*a)))
  s2=(((b*-1)+(sqrt(d)))/((2*a)))
  print("s1= "+str(s1))
  print("s2= "+str(s2))
  print("(x+ " + str(-s1)+")")
  print("(x+ " + str(-s2)+")")
 else:
  print("no solution")
