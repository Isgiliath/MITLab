# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:09:04 2018

@author: Isgiliath
"""
##User inputs for calculating the amount of months to save for a dream home.
##all values are cast as floats.

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

portion_down_payment = 0.25
r = 0.04 ##r is the rate of return, anually on investments applied to current savings
monthly_salary = (annual_salary/12)
current_savings = 0.0
monthly_savings = (monthly_salary*portion_saved)
down_payment_amount = (total_cost*portion_down_payment)

##this loop will count the number of months (month_count) to satsify savings for the
##down_payment_amount.  Current_savings includes calc of annual interest applied to 
##investment on current_savings

month_count=0
while current_savings <= down_payment_amount:
    month_count = month_count+1
    current_savings += (current_savings*r/12)+monthly_savings

##the assignment says to have it output like this, not certain the '>>>'s are needed
##but I did what it said.
print('>>>')
print('Enter your annual salary: ', int(annual_salary))
print('Enter the percent of your salary to save, as a decimal: ', float(portion_saved))
print('Enter the cost of your dream home: ', int(total_cost))
print(month_count)
print('>>>')
