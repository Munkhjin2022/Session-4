
#connenct input
q=int(input("Please put quantity "))

#process phase 

if q > 10000:
  p = 10
elif q >=5000 and q<=10000:
  p = 20
else: 
 p = 30

ep = q * p
tax=(ep/100)*7
total=ep+tax

#output
print("The extanded price: ", ep)
print("The tax: ", tax)
print("The total: ", total)
