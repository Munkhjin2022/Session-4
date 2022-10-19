#comment input
p=int(input("Enter the quantity of part "))

#process phase
if p==10 and p==55:
  cost=1.00 
elif p==99:
  cost=2.00
elif p==80 and p==70:
  cost=3.00
else: 
  cost=5.00
total=p * cost

#output
print("The part number :", p)
print("The cost per unit : ", cost)
print("The total cost: ", total)
