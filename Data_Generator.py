#Importing all the needed libraries

import datetime
import random
from random import choice
from string import ascii_uppercase
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from Create import Buyers, Sellers, Offices, Agents, Agents_Offices, Listings, Transactions, engine

#Intializing the session for database connection
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()


"""
This function is used to populate the sellers table with random information.
"""
def add_random_seller():
    first_name = ''.join(choice(ascii_uppercase) for i in range(random.randint(3, 7)))
    last_name = ''.join(choice(ascii_uppercase) for i in range(random.randint(3, 7)))
    Email = first_name + "." + last_name + "@gmail.com"
    Phone = int(''.join(choice("0123456789") for i in range(10)))
    session.add(Sellers(Firstname = first_name, Surname = last_name, Email = Email, Phone = Phone))
    session.commit()

"""
This function is used to populate the buyers table with random information. 
"""
def add_random_buyer():
    first_name = ''.join(choice(ascii_uppercase) for i in range(random.randint(3, 7)))
    last_name = ''.join(choice(ascii_uppercase) for i in range(random.randint(3, 7)))
    Email = first_name + "." + last_name + "@gmail.com"
    Phone = int(''.join(choice("0123456789") for i in range(10)))
    session.add(Buyers(Firstname = first_name, Surname = last_name, Email = Email, Phone = Phone))
    session.commit()

"""
This function is used to populate the offices table with random information. 
"""
def add_random_office(Zipcode):
    Name = ''.join(choice(ascii_uppercase) for i in range(5))
    Email = Name + "_" + str(Zipcode) + "@gmail.com"
    Phone = int(''.join(choice("0123456789") for i in range(10)))
    session.add(Offices(Name = Name, Email = Email, Phone = Phone, Zipcode = Zipcode))
    session.commit()

"""
This function is used to populate the agents table with random information. 
"""
def add_random_agent():
    first_name = ''.join(choice(ascii_uppercase) for i in range(random.randint(3, 7)))
    last_name = ''.join(choice(ascii_uppercase) for i in range(random.randint(3, 7)))
    Email = first_name + "." + last_name + "@minerva.kgi.edu"
    Phone = int(''.join(choice("0123456789") for i in range(10)))
    session.add(Agents(Firstname = first_name, Surname = last_name, Email = Email, Phone = Phone))
    session.commit()

"""
This function is used to populate the office agents table with random information. 
"""
def random_office_agent(AgentID):
    population = set(range(1,21))
    relations  = random.randint(1, 10)
    samples = random.sample(population, relations)
    for i in samples:
        session.add(Agents_Offices(AgentID = AgentID, OfficeID = i))
        session.commit()

"""
This function is used to add a new house 
"""
def add_listing():
    bedroom = random.randint(1,7)
    bathroom = random.randint(1,7)
    price = random.randint(100000, 1000000)
    Add = ''.join(choice(ascii_uppercase) for i in range(random.randint(20, 40)))
    Zip = random.randint(94100, 94120)
    date_listed = datetime.datetime(random.randint(2017, 2019), random.randint(1,12), random.randint(1,28))
    agent_id = random.randint(1, 50)
    seller_id = random.randint(1, 100)
    session.add(Listings(Bedroom = bedroom, Bathroom = bathroom, Price = price, Address = Add, Zipcode = Zip, DateListed = date_listed, ListingAgentID = agent_id, SellerID = seller_id, Status = 0))
    session.commit()

"""
This function is used to check the conditions required to make a transaction and it also performs various updates 
"""
def buy_process(BuyerID, ListingID, SellingAgentID, SellPrice):
    buyer = session.query(Buyers).filter(Buyers.BuyerID==BuyerID).first()
    house = session.query(Listings).filter(Listings.ListingID==ListingID).first()
    if buyer == None:
        print("Invalid BuyerID")
    elif house == None:
        print("Invalid HouseID")
    elif house.Status == 1:
        print("Cannot make transactions! House has been SOLD!")
    else:
        house.Status = 1

        transaction = Transactions(ListingID = house.ListingID,
                                    BuyerID = buyer.BuyerID,
                                    SellerID = house.SellerID,
                                    SellingAgentID = SellingAgentID,
                                    SellPrice = SellPrice)

        session.add(transaction)
        session.commit()

