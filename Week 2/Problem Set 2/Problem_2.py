# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 22:14:50 2017

@author: Daniel
"""
# Test Case 1:
balance = 3329
annualInterestRate = 0.2
#
#Result Your Code Should Generate:
#Lowest Payment: 310

# Test Case 2:
#balance = 4773
#annualInterestRate = 0.2
#
#Result Your Code Should Generate:
#Lowest Payment: 440

# Test Case 3:
#balance = 3926
#annualInterestRate = 0.2
#
#Result Your Code Should Generate:
#Lowest Payment: 360

def CalculateRemainingBalance(balance, payment, monthlyInterestRate):
    unpaidBalance = balance - payment
    updatedBalance = unpaidBalance + monthlyInterestRate * unpaidBalance
    return updatedBalance
    
def CalculateMinimumPayment(balance, annualInterestRate):
    remainingBalance = balance
    monthlyInterestRate = annualInterestRate/12.0
    minimumFixedMonthlyPayment = 0
    
    while remainingBalance > 0:
        remainingBalance = balance
        minimumFixedMonthlyPayment += 10
        for i in range(12):
            remainingBalance = CalculateRemainingBalance(remainingBalance, minimumFixedMonthlyPayment, monthlyInterestRate)
    
    return minimumFixedMonthlyPayment

minimumFixedMonthlyPayment = CalculateMinimumPayment(balance, annualInterestRate)
print("Lowest Payment: " + str(minimumFixedMonthlyPayment))