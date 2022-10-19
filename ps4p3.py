#comment input
a=float(input("Enter a principle amount of a CD "))
y=float(input("Enter a year to maturity of CD "))

#process phase
if a>100000 and y==5:
  inr=0.06
elif a>=50000 and a<=100000 and y==10:
  inr=0.05
elif a>=50000 and a<=100000 and y==5:
  inr=0.04
else: 
  inr=0.02

frsty=a * inr

#output
print("The principle: ", a)
print("The interest rate: ", inr)
print("The interest amount for first year: ", frsty)
