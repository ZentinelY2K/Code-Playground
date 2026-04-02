
#Purchase Cost of the Car (in $) = 30000
#Monthly Car Expenses (in $) = 350
#Loan Term (in months) = 60

def car_cost(purchase,monthly_expenses,loan_term=60):
    monthly_payment = purchase/loan_term
    monthly_costs = monthly_payment + monthly_expenses

    print(monthly_costs)
    return()

car_cost(30000,350)
         
import math

def calculation():
    a = 17
    b = 12
    a_sq = math.pow(a, 2)
    b_sq = math.pow(b, 2)
    c_sq = a_sq + b_sq
    c = math.sqrt(c_sq)
    c = round(c, 3)
    print(f"The result of the calculation is {c}.")
    print(a_sq)

calculation()

x = 123.864
h =float(round(x,2)) 
print(h)