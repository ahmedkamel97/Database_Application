## About this project:

In this project I build a mock database system for a large franchised real estate company. This means that the company has many offices located all over the country. Each office is responsible for selling houses in a particular area. However an estate agent can be associated with one or more offices.

### Every month the following reports need to be run:

1) Find the top 5 offices with the most sales for that month.
2) Find the top 5 estate agents who have sold the most (include their contact details and their sales details so that it is easy contact them and congratulate them).
3) Calculate the commission that each estate agent must receive and store the results in a separate table.
4) For all houses that were sold that month, calculate the average number of days that the house was on the market.
5) For all houses that were sold that month, calculate the average selling price
6) Find the zip codes with the top 5 average sales prices

## Data Normalization:

Meanwhile designing and creating the tables for the database, I followed the Normalization guidelines. I mainly followed the 3NF guidelines. All the tables are assured to be in the First Normalization form, Second Normalization form, and the third Normalization form.

### All the tables follow the first normal form rules as:
1) Each table cell only contain a single value

2) Each record is unique
### All the tables follow the second normal form rules as:
1) The tables are in the first normal form

2) There is a single column Primary Key

### All the tables follow the third normal form rules as:
1) The tables are in the second normal form

2) There are no transitive functional dependencies

## Additional Features:

1) The entire project is divided into multiple files where each file is focused to doing one task to achieve a proper implementation of #separationofconcerns and #Breakitdown

2) All the code included is very well commented to ensure a proper application of #communication

3) The random data is not generated manually, instead I created a file that generates random datasets of any size to be able to test the system at any scale easily

4) All the queries can be easily modified, for example to get the top 10 results instead of the top 5 results or using different values or dates.
  
#########################################################################

## Files included in this project:

1) README.md: The description of the project and all the individual files

2) requirements.txt: All the Dependencies needed to run the project correctly

3) Create.py: This file creates the tables and the database using SQLAlchemy

4) Insert.py: This file inserts randomly generated data into the database

5) Data_Generator.py: This file is used to create a random dataset of any size to be inserted into the database.

6) Query_core_functions.py: this file contains all the primary functions needed to run the six queries

7) Query.py: this file runs the six required queries and displays the information in a highly organized way.

8) ER Diagram.png: ER Diagram for the database  

########################################################################

## To Set Up the Virtual Environment and Install all the Requirements:

1) Open a command-line interpreter within the project directory

2) Install Virtual Environment: python3 -m venv env

3) Activate Virtual Environment: source env/bin/activate

4) Install Dependencies: pip install -r requirements.txt  

5) You are good to go!!

########################################################################

## To Run the Project:

1) Open a command-line interpreter within the project directory

2) Type: Python

3) Make sure it is python 3, if it is not please install the latest version of Python 3

4) Run the file Create.py to build the tables

5) Run the file insert.py to insert randomly generated data into the database

6) Run the file Query.py to preview the results of all the queries

########################################################################
