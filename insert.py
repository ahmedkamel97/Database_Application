#Importing all the needed libraries

import random
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from Create import engine
from Data_Generator import add_random_seller, add_random_buyer, add_random_office, add_random_agent, \
    random_office_agent, add_listing, buy_process

#Intializing the session for database connection
Session = sessionmaker(bind=engine)
session = Session() 
metadata = MetaData()

def main():

    for i in range(100): 
        add_random_seller()

    for i in range(100): 
        add_random_buyer()

    for Zipcode in range(94100, 94121):
        add_random_office(Zipcode)

    for i in range(50): 
        add_random_agent()

    for AgentID in range(50):
        random_office_agent(AgentID)

    for i in range(200):
        add_listing()

    population = set(range(1,101))
    samples = random.sample(population, 50)
    for i in samples:
        buy_process(random.randint(1, 100), i, random.randint(1, 50), random.randint(100000, 1000000))

if __name__ == "__main__":
    main()

