import mysql.connector as sql
from sqlalchemy import create_engine
import pandas as pd
import re
import insert as ins
import search as srch
import report as rp
import invoice as inv


def login():
    username=input('Enter username: ')
    password=input('Enter password: ')
    global connection
    connection = sql.connect(
    host="localhost",
    user=username,
    passwd=password,
    database="autofix"
    )
    alch_login='mysql://'+username+':'+password+'@localhost/autofix'
    global engine
    engine = create_engine(alch_login)
    print ('Logged In')
    
def exit():
    n = int(input(“ Press 999 to exit : “))
    if n == 999:
       os.system(‘cls’) # For Windows
       run()
    else:
       print(“ Invalid Option”)
       exit()
    
def displayMainMenu():
    print(‘ — — — — MENU — — — -’)
    print(‘ 1. Insert Entry’)
    print(‘ 2. Search Database’)
    print(‘ 3. View Reports’)
    print(‘ 4. View Invoice’)
    print(‘ 5. Exit’)
    print(‘ — — — — — — — — — — ‘)

def displayInsertMenu():
    print(‘ — — — — MENU — — — -’)
    print(‘ 1. Insert Through System’)
    print(‘ 2. Insert From Excel’)
    print(‘ 3. Exit’)
    print(‘ — — — — — — — — — — ')

def displaySearchMenu():
    print(‘ — — — — MENU — — — -’)
    print(‘ 1. View All Tables’)
    print(‘ 2. View All Columns Of A Table’)
    print(‘ 3. Read a Table’)
    print(‘ 4. Exit’)
    print(‘ — — — — — — — — — — ‘)
    
def displayReportMenu():
    print(‘ — — — — MENU — — — -’)
    print(‘ 1. Job Price Report’)
    print(‘ 2. Customer Due Report’)
    print(‘ 3. Employee Allocation Report’)
    print(‘ 4. Inventory Report’)
    print(‘ 5. Exit’)    
    print(‘ — — — — — — — — — — ‘)
    

def run():
   displayMainMenu()
   n = int(input(“Enter option : “))
   if n == 1:
      os.system(‘cls’)
      insertMenu()
   elif n == 2:
      os.system(‘cls’)
      searchMenu()
   elif n == 3:
      os.system(‘cls’)
      reportMenu()
   elif n == 4:
      os.system(‘cls’)
      inv.invoice()
      exit()
   elif n == 5:
      os.system(‘cls’)
      print(‘ — — — Thank You — — -’)
   else:
      os.system(‘cls’)
      run()


def insertMenu():
   displayInsertMenu()
   n = int(input(“Enter option : “))
   if n == 1:
      os.system(‘cls’)
      ins.insert()
      exit()
   elif n == 2:
      os.system(‘cls’)
      ins.insert_from_excel()
      exit()
   elif n == 3:
      os.system(‘cls’)
      run()
   else:
      print(“ Invalid Option”)
      os.system(‘cls’)
      insertMenu()

def searchMenu():
   displaySearchMenu()
   n = int(input(“Enter option : “))
   if n == 1:
      os.system(‘cls’)
      srch.list_tables()
      exit()
   elif n == 2:
      os.system(‘cls’)
      srch.list_columns()
      exit()
   elif n == 3:
      os.system(‘cls’)
      srch.read_table()
      exit()
   elif n == 4:
      os.system(‘cls’)
      run()
   else:
      print(“ Invalid Option”)
      os.system(‘cls’)
      searchMenu()

def reportMenu():
   displayReportMenu()
   n = int(input(“Enter option : “))
   if n == 1:
      os.system(‘cls’)
      rp.job_price_report()
      exit()
   elif n == 2:
      os.system(‘cls’)
      rp.customer_due_report()
      exit()
   elif n == 3:
      os.system(‘cls’)
      rp.employee_allocation()
      exit()
   elif n == 4:
      os.system(‘cls’)
      rp.inventory_report()
      exit()
   elif n == 5:
      os.system(‘cls’)
      run()
   else:
      print(“ Invalid Option”)
      os.system(‘cls’)
      reportMenu()


if __name__ == ‘__main__’:
   login()
   run()