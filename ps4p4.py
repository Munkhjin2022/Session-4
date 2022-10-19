#comment input
t=float(input("Enter number of concert tickets "))

#process phase 
if t>=25:
  p=50
elif t>=10 and t<=24:
  p=60
elif t>=5 and t<=9:
  p=70
elif t<5:
  p=75

total= t * p

#output
print("The number of tickets: ", t)
print("Price of per ticket: ", p)
print("Total: ", total)

