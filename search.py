"""This module contains functions related to searching the database"""


import pandas as pd

def list_tables():
    """Function to list all tables in the database"""
    cursor.execute("SHOW TABLES") 
    for table_name in cursor:
        print(table_name)
    exit()
                        

def list_columns():
    """Function to list all columns of a table"""
    table=input('Enter table name: ')
    query='DESCRIBE '+str(table)
    cursor.execute(query)
    for column_name in cursor:
        print(column_name[0])
    cursor.close()
    
def read_table(connection):
    """Function to read a table with options to select columns and enter conditions"""
    table=input('Enter table name:')
    select_column=input('Do you want to select columns [y/n]').lower()
    if select_column=='y':
        column_list=''
        cursor = connection.cursor(buffered=True)
        query='DESCRIBE '+str(table)
        cursor.execute(query)
        for column_name in cursor:
            include=input('Include '+column_name[0]+'?')
            if include=='y':
                column_list=column_list+column_name[0]+','
        column_list=column_list[0:-1]
        query='SELECT '+column_list+' FROM '+str(table)
    else:
        query='SELECT * FROM '+str(table)
    select_condition=input('Do you want to enter a condition? [y/n]').lower()
    if select_condition=='y':
            condition=input('Enter condition: ')
            query=query+' WHERE '+condition 
    print('\n')
    df = pd.read_sql_query(query,connection)
    print(df)
    print('\n')
