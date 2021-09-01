import pandas as pd
"""This module contains functions related to insertion of data"""

def insert(cursor):
    """This function asks the user for the table they want to enter data into, 
    retrieves the columns of the table, and asks the user for the entry value
    into each column
    """ 
    table=input('Enter table name: ')
    query='DESCRIBE '+str(table) # Getting the column names and other table details
    cursor.execute(query)
    columns='('
    values='('
    for column_name in cursor:
        column=column_name[0]# seperating out the column name
        columns=columns+column+','
        print ('Enter text within quotation marks')
        value=input('Enter value for '+column+' ')
        values=values+value+','
    columns=columns[0:-1]+')'
    values=values[0:-1]+');'
    query='INSERT INTO {}{} VALUES {}'
    print (query.format(table,columns,values))
    cursor.execute(query.format(table,columns,values))
    print('Entry Successful')
    
    
        

def insert_from_excel(alch_connection):
    """This function uses pandas to_sql function to insert data from an excel sheet into the database"""

    excel_file=input('Enter excel file path: ')
    table_name=input('Enter table name: ')
    excel_file=excel_file.replace('\\','/')
    df=pd.read_excel(excel_file,index_col=0)
    print(df)
    df.to_sql(table_name,con=alch_connection,if_exists='append')
    print('Entry Successful')
