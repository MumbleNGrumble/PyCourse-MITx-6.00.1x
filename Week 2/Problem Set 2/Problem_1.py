# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 21:41:34 2017

@author: Daniel
"""

# Test Case 1
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
#
#Result Your Code Should Generate Below:
#Remaining balance: 31.38

# Test Case 2
#balance = 484
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
#
#Result Your Code Should Generate Below:
#Remaining balance: 361.61

def CalculateRemainingBalance(balance, monthlyPaymentRate, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlyPayment = monthlyPaymentRate * balance
    unpaidBalance = balance - minimumMonthlyPayment
    updatedBalance = unpaidBalance + monthlyInterestRate * unpaidBalance
    return updatedBalance

remainingBalance = balance

for i in range(12):
    remainingBalance = CalculateRemainingBalance(remainingBalance, monthlyPaymentRate, annualInterestRate)
#    print("Month " + str(i + 1) + " Remaining balance: " + str(round(balance,2)))

print("Remaining blance: " + str(round(remainingBalance, 2)))