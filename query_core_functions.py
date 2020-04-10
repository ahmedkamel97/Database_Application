#Importing all the needed libraries

import calendar
import datetime
import numpy as np
import pandas as pd
import sqlalchemy as db
from Create import connection, metadata
from insert import engine

#Connecting the tables

Seller = db.Table('Sellers', metadata, autoload=True, autoload_with=engine)
Buyer = db.Table('Buyers', metadata, autoload=True, autoload_with=engine)
Office = db.Table('Offices', metadata, autoload=True, autoload_with=engine)
Agent = db.Table('Agents', metadata, autoload=True, autoload_with=engine)
Agent_Office = db.Table('Agents_Offices', metadata, autoload=True, autoload_with=engine)
Listing = db.Table('Listings', metadata, autoload=True, autoload_with=engine)
Transaction = db.Table('Transactions', metadata, autoload=True, autoload_with=engine)

"""
This function is used to calculate the commission based on the selling price of the house. 
"""
def commission(amount):
    amount = int(amount)
    if amount < 100000:
        return 0.1 * amount
    elif amount < 200000:
        return 0.075 * amount
    elif amount < 500000:
        return 0.06 * amount
    elif amount < 1000000:
        return 0.05 * amount
    else:
        return 0.04 * amount

"""
This function is used to answer the first query which is finding the top 5 offices with the most sales for that month 
"""

def query_one(number=5, year=datetime.datetime.utcnow().year, month=datetime.datetime.utcnow().month): #Uses today's date
    start = datetime.datetime(year, month, 1)
    end = datetime.datetime(year, month, calendar.monthrange(year, month)[1], 23, 59, 59)

    query = db.select([Office.columns.Name, Office.columns.Zipcode, Office.columns.Phone,
                       db.func.sum(Transaction.columns.SellPrice).label('Total Sales'),
                       db.func.count(Transaction.columns.SellPrice).label('Number of Sales')]) \
        .group_by(Listing.columns.Zipcode) \
        .where(db.and_(Transaction.columns.DateSold >= start, end >= Transaction.columns.DateSold)) \
        .order_by(db.desc(db.func.sum(Transaction.columns.SellPrice)))

    query = query.select_from(
        (Transaction.join(Listing, Transaction.columns.ListingID == Listing.columns.ListingID)).join(Office,
                                                                                                     Office.columns.Zipcode == Listing.columns.Zipcode))
    results = connection.execute(query).fetchall()[:number]
    print("Top {2} Offices with the most sales in month: {0}, year: {1}\n".format(month, year, number))
    if results != []:
        df = pd.DataFrame(results)
        df.columns = results[0].keys()
        print(df)
    else:
        print("No Sales Recorded in the Database!")

"""
This function is used to answer the second query which is finding the top 5 estate agents who have sold the most 
This function also displays their contact details and their sales details so that it is easy contact them and congratulate them
Please Note that we can also specify any number other than 5 and it will also work 
"""

def query_two(number=5):
    query = db.select([Transaction.columns.SellingAgentID, Agent.columns.Phone, Agent.columns.Email,
                       db.func.sum(Transaction.columns.SellPrice).label('Total Sales'),
                       db.func.count(Transaction.columns.SellPrice).label('Number of Sales')]) \
        .group_by(Transaction.columns.SellingAgentID).order_by(db.desc(db.func.sum(Transaction.columns.SellPrice)))

    query = query.select_from(Agent.join(Transaction,
                                         Agent.columns.AgentID == Transaction.columns.SellingAgentID))
    results = connection.execute(query).fetchall()[:number]
    df = pd.DataFrame(results)
    df.columns = results[0].keys()
    print("Top {0} agents\n".format(number))
    print(df)


"""
This function is used to answer the Third question which is calculating the commission that each estate agent must receive
The results are stored in a separate table  
"""
def commission_table():
    query = db.select(
        [Transaction.columns.SellingAgentID, Agent.columns.Phone, Agent.columns.Email, Transaction.columns.SellPrice])

    query = query.select_from(Agent.join(Transaction,
                                         Agent.columns.AgentID == Transaction.columns.SellingAgentID))
    results = connection.execute(query).fetchall()
    df = pd.DataFrame(results)
    df.columns = results[0].keys()
    df['SellPrice'] = df['SellPrice'].apply(commission)
    commission_table = df.groupby(['SellingAgentID']).sum()
    commission_table.columns = ["Total Commision"]
    commission_table.sort_values(["Total Commision"])
    print(commission_table)

"""
This function is used to answer the fourth query which is for all houses that were sold by this month, calculates the average number of days that the house was on the market
Today's date is acquired using the datetime.utcnow()
"""
def query_four(year=datetime.datetime.utcnow().year, month=datetime.datetime.utcnow().month):
    begin = datetime.datetime(year, month, 1)
    end = datetime.datetime(year, month, calendar.monthrange(year, month)[1], 23, 59, 59)
    query = db.select([Transaction.columns.ListingID, Listing.columns.DateListed, Transaction.columns.DateSold]) \
        .where(db.and_(Transaction.columns.DateSold >= begin, end >= Transaction.columns.DateSold))

    query = query.select_from(Transaction.join(Listing,
                                               Transaction.columns.ListingID == Listing.columns.ListingID))
    results = connection.execute(query).fetchall()
    print("Days on market of houses sold in month: {0}, year: {1}".format(month, year))
    if results != []:
        df = pd.DataFrame(results)
        df.columns = results[0].keys()
        df["On Market Day"] = abs(df["DateSold"] - df["DateListed"])
        print(pd.DataFrame(df[["ListingID", "On Market Day"]]))
        print()
        print("The average days on market of houses sold in of houses sold in month {0}, year {1}: {2} (Days) " \
              .format(month, year, np.mean(df["On Market Day"]).days + 1))
    else:
        print("No Data")

"""
This function is used to answer the fifth query which is for all houses that were sold by this month, calculates the average selling price
Today's date is acquired using the datetime.utcnow()
"""
def query_five(year=datetime.datetime.utcnow().year, month=datetime.datetime.utcnow().month):
    begin = datetime.datetime(year, month, 1)
    end = datetime.datetime(year, month, calendar.monthrange(year, month)[1], 23, 59, 59)

    query = db.select([Transaction.columns.ListingID, Transaction.columns.SellPrice]) \
        .where(db.and_(Transaction.columns.DateSold >= begin, end >= Transaction.columns.DateSold))

    query = query.select_from(Transaction.join(Listing,
                                               Transaction.columns.ListingID == Listing.columns.ListingID))
    results = connection.execute(query).fetchall()
    print("The houses are sold in month: {0}, year: {1}".format(month, year))
    if results != []:
        df = pd.DataFrame(results)
        df.columns = results[0].keys()
        print(df)
        print()
        print("The average price: {0} ($)".format(int(np.mean(df["SellPrice"]))))
    else:
        print("No Data available")

"""
This function is used to answer the sixth query which is finding the zip codes with the top 5 average sales prices
Please Note that we can also specify any number other than 5 and it will also work 
Today's date is acquired using the datetime.utcnow()
"""
def query_six(number=5):
    query = db.select([Office.columns.Name, Office.columns.Zipcode, Office.columns.Phone,
                       db.func.avg(Transaction.columns.SellPrice).label('Average Sale Price')]) \
        .group_by(Listing.columns.Zipcode).order_by(db.desc(db.func.sum(Transaction.columns.SellPrice)))

    query = query.select_from(
        (Transaction.join(Listing, Transaction.columns.ListingID == Listing.columns.ListingID)).join(Office,
                                                                                                     Office.columns.Zipcode == Listing.columns.Zipcode))
    results = connection.execute(query).fetchall()[:number]
    if results != []:
        df = pd.DataFrame(results)
        df.columns = results[0].keys()
        print("The top {0} zipcode with highest average sale prices:".format(number))
        print(df)
    else:
        print("No Data Available")