import math
a = "investment"
b = "bond"
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
c = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
if c.lower() == a:
    P = float(input("Please enter amount of money that you are depositing: "))
    r = float(input("Please enter interest rate: "))
    t = float(input("Please enter number of years you plan on investing: "))
    e = input("Please choose one of the following options: simple or compound ")
    f = "simple"
    g = "compound"
    A = float(P*(1 + r*t))
    A2 = float(P * math.pow((1+r),t))
    if e.lower() == f:
      print(A)
    else:
      print(A2)
elif c.lower() == b:
    P2 = float(input("Please enter value of the house: "))
    i = float(input("Please enter interest rate: "))
    n = float(input("Please enter number of months you plan to take to repay: "))
    repayment = float((i/12/100)*P2) / (1-(1 + i/12)/100)**(-n)
    print(repayment)
else:
    print("Sorry, you have to choose one of the options: investment or bond") 
   
    
