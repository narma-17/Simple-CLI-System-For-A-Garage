import pandas as pd
import re

"""Module containing functions for common reports that will be generated from the system"""

def job_price_report(connection):
    """ This function gets the amounts charged for each job"""
    specify_date=input('Do you want to specify dates? [y/n]')
    if specify_date=='y':
        start_date=input('Enter start date: ')
        end_date=input('Enter end date: ')
        query="SELECT jr.job_code,job_date,customer_id,sum(price) FROM service_list JOIN job_requirement AS jr ON service_list.service_code=jr.service_code JOIN job AS j ON jr.job_code=j.job_code JOIN vehicle AS v ON j.vehicle_no=v.vehicle_no WHERE job_date BETWEEN '"+start_date+"' AND '"+end_date+"' GROUP BY jr.job_code "
    else:
        query="SELECT jr.job_code,job_date,customer_id,sum(price) FROM service_list JOIN job_requirement AS jr ON service_list.service_code=jr.service_code JOIN job AS j ON jr.job_code=j.job_code JOIN vehicle AS v ON j.vehicle_no=v.vehicle_no WHERE job_date BETWEEN SUBDATE(NOW(),INTERVAL 60 DAY) AND NOW() GROUP BY jr.job_code "
    df = pd.read_sql_query(query,connection)
    print(df)
    
    
      
    
def customer_due_report(connection):
    """ This function gets amound outstanding from customers"""
    select_cust=input('Do you want to select customer? [y/n]')
    if select_cust=='y':
        name_code=input('Search by last name(n) or id(i)? [i/n]').lower()
        if name_code=='i':
            cust_id=input('Enter customer id: ')
            query='''SELECT c.customer_id,first_name,last_name,sum(price) FROM 
            service_list JOIN job_requirement AS jr ON service_list.service_code=jr.service_code
            JOIN job AS j ON jr.job_code=j.job_code JOIN vehicle AS v ON j.vehicle_no=v.vehicle_no
            JOIN customer AS c ON c.customer_id=v.customer_id WHERE c.customer_id={} 
            GROUP BY customer_id"'''
            query=query.format(cust_id)
        else:
            cust_name=input('Enter customer last name: ').lower()
            query='''SELECT c.customer_id,first_name,last_name,sum(price) FROM 
            service_list JOIN job_requirement AS jr ON service_list.service_code=jr.service_code
            JOIN job AS j ON jr.job_code=j.job_code JOIN vehicle AS v ON j.vehicle_no=v.vehicle_no
            JOIN customer AS c ON c.customer_id=v.customer_id WHERE c.last_name LIKE '%{}%'
            GROUP BY customer_id'''
            query=query.format(cust_name)
    else:
        query='''SELECT c.customer_id,first_name,last_name,sum(price) FROM service_list
        JOIN job_requirement AS jr ON service_list.service_code=jr.service_code 
        JOIN job AS j ON jr.job_code=j.job_code JOIN vehicle AS v ON j.vehicle_no=v.vehicle_no 
        JOIN customer AS c ON c.customer_id=v.customer_id 
        GROUP BY customer_id"'''
    df = pd.read_sql_query(query,connection)
    print(df)
	
def employee_allocation(connection):
    """ This function gets a report on the allocation of employee hours and services to jobs and services"""
    query='''SELECT jr.job_code,jr.service_code,sl.description,es.employee_id,es.expertise,es.start_hour,es.end_hour FROM `employee_schedule` AS es 
          JOIN job_requirement AS jr ON es.job_code = jr.job_code
          JOIN service_list as sl on jr.service_code=sl.service_code
          JOIN employee AS e ON e.employee_id=es.employee_id'''
    specify_date=input('Do you want to specify dates? [y/n]')
    if specify_date=='y':
        start_date=input('Enter start date: ')
        end_date=input('Enter end date: ')
        query=query+' WHERE es.start_hour > {} AND es.end_hour<{}' 
        query=query.format(start_date,end_date) 
        return query
    else:
        query=query+' WHERE es.start_hour > DATE_SUB(NOW(),INTERVAL 60 DAY)'
    specify_job_code=input('Do you want to specify job code? [y/n]')
    if specify_job_code=='y':
        job_code=input('Enter job code: ')
        query=query+" AND jr.job_code='{}'"
        query=query.format(job_code)
    specify_emp=input('Do you want to specify employee? [y/n]').lower()
    if specify_emp=='y':
        name_or_code=input('Search by last name(n) or id(i)? [i/n]').lower()
        if name_or_code=='n':
            name=input('Employee name: ')
            query=query+" AND e.last_name LIKE '%{}%'"
            query=query.format(name)
        else:
            emp_id=input('Employee name: ')
            query=query+" AND e.employee_id='{}'"
            query=query.format(emp_id)    
    df = pd.read_sql_query(query,connection)
    save=input('Do you want to save to excel? [y/n]').lower()
    if save=='y':
        save_to_excel(df)
    print(df)
    
    
def inventory_report(connection):
    """ This function gets a report on inventory purchase and usage"""
    query='''SELECT mp.material_code,m.material_description,purchase_qty,sum(use_quantity),(purchase_qty-sum(use_quantity))
            AS net_quantity 
            FROM  material_purchase as mp JOIN material_use as mu ON mp.material_code=mu.material_code
            JOIN materials AS m ON m.material_code=mp.material_code
            GROUP BY mp.material_code'''
    df = pd.read_sql_query(query,connection)
    save=input('Do you want to save to excel? [y/n]').lower()
    if save=='y':
        save_to_excel(df)
    print(df)
    
def save_to_excel(df):
    """ This function uses pandas to_excel function to save a report to excel"""
    path=input('Enter path to file: ')
    path=path.replace('\\','/')
    sheet_name=input('Enter sheet name: ')
    with pd.ExcelWriter(path) as writer:  
        df.to_excel(writer, sheet_name=sheet_name)
