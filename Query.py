#Importing the functions
from query_core_functions import query_one, query_two, commission_table, query_four, query_five, query_six

"""
The function query one is used to answer the first query which is finding the top 5 offices with the most sales for that month 
"""
print("Query 1: The top 5 offices with the most sales for that month:\n")
query_one()
print("\n")
"""
The function design is modular and accept to make queries with any criteria.
For  example: this additional query finds the office with the most sales in February, 2019
"""
print("Additional: The offices with the most sales in February, 2019:\n")
query_one(1, 2019, 2)
print("\n")

"""
The function query two is used to answer the second query which is finding the top 5 estate agents who have sold the most 
The function query two also displays their contact details and their sales details so that it is easy contact them and congratulate them
Please Note that we can also specify any number other than 5 and it will also work 
"""
print("The top 5 estate agents who have sold the most:\n")
query_two()
print("\n")

"""
This function is used to answer the Third question which is calculating the commission that each estate agent must receive
The results are stored in a separate table  
"""
print("the commission that each estate agent must receive:\n")
commission_table()
print("\n")

"""
The function query four is used to answer the fourth query which is for all houses that were sold by this month, calculates the average number of days that the house was on the market
Today's date is acquired using the datetime.utcnow()
"""
print("For all houses that were sold that month, the average number of days that the house was on the market:\n")
query_four()
print("\n")

"""
The function query five is used to answer the fifth query which is for all houses that were sold by this month, calculates the average selling price
Today's date is acquired using the datetime.utcnow()
"""
print("For all houses that were sold this month, the average selling price:\n")
query_five()
print("\n")

"""
The function query six is used to answer the sixth query which is finding the zip codes with the top 5 average sales prices
Please Note that we can also specify any number other than 5 and it will also work 
Today's date is acquired using the datetime.utcnow()
"""
print("The zip codes with the top 5 average sales prices:\n")
query_six()
print("\n")
