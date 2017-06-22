# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 22:40:25 2017

@author: Daniel
"""

# Test Case 1:
balance = 320000
annualInterestRate = 0.2
#
#Result Your Code Should Generate:
#Lowest Payment: 29157.09

# Test Case 2:
#balance = 999999
#annualInterestRate = 0.18
#
#Result Your Code Should Generate:
#Lowest Payment: 90325.03

def CalculateRemainingBalance(balance, payment, monthlyInterestRate):
    unpaidBalance = balance - payment
    updatedBalance = unpaidBalance + monthlyInterestRate * unpaidBalance
    return updatedBalance
    
def CalculateMinimumPayment(balance, annualInterestRate):
    remainingBalance = balance
    monthlyInterestRate = annualInterestRate/12.0
    lowerBound = balance / 12
    upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
    
    while round(remainingBalance,2) != 0.00:
        remainingBalance = balance
        minimumFixedMonthlyPayment = (lowerBound + upperBound) / 2
        for i in range(12):
            remainingBalance = CalculateRemainingBalance(remainingBalance, minimumFixedMonthlyPayment, monthlyInterestRate)
        
        if remainingBalance > 0:
            lowerBound = minimumFixedMonthlyPayment
        elif remainingBalance < 0:
            upperBound = minimumFixedMonthlyPayment
    
    return minimumFixedMonthlyPayment

minimumFixedMonthlyPayment = CalculateMinimumPayment(balance, annualInterestRate)
print("Lowest Payment: " + str(round(minimumFixedMonthlyPayment,2)))