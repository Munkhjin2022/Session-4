#comment input
name=str(input("Enter the last name: "))
salary=float(input("Enter the salary: "))
level=float(input("Enter the job level: "))

#process phase 
if level>=10:
  rate=0.25
elif level>=5 and level<=9:
  rate=0.2
else:
  rate=0.1

bonus=salary*rate

#output
print("Last name : ", name)
print("The bonus : ", bonus)
