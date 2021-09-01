'''Invoicing function'''
def name_vehicle(j_code,connection):
    query="""SELECT j.vehicle_no,c.first_name,c.last_name FROM job as j JOIN vehicle AS v
            ON j.vehicle_no=v.vehicle_no 
            JOIN customer AS c ON c.customer_id=v.customer_id
            WHERE j.job_code='{}'"""
    query=query.format(j_code)
    df=df = pd.read_sql_query(query,connection)
    vehicle_no=df.iloc[0]['vehicle_no']
    f_name=df.iloc[0]['first_name']
    l_name=df.iloc[0]['last_name']
    return tuple([vehicle_no,f_name,l_name])
 
 

def service_list(j_code,connection):
    query="""SELECT s.service_code, s.description, s.price FROM service_list AS s 
            JOIN job_requirement AS jr ON s.service_code=jr.service_code
            WHERE jr.job_code='{}'"""
    query=query.format(j_code)
    df=df = pd.read_sql_query(query,connection)
    service_code=list(df['service_code'])
    service_desc=list(df['description'])
    service_price=list(df['price'])
    return (service_code,service_desc,service_price)


def spare_part(j_code,connection):
    query="""SELECT description,quantity,total_parts_price FROM spare_part
    WHERE job_code='{}'
    """
    query=query.format(j_code)
    df=df = pd.read_sql_query(query,connection)
    description=list(df['description'])
    quantity=list(df['quantity'])
    price=list(df['total_parts_price'])
    return (description,quantity,price)


def invoice(connection):
    j_code=input('Enter job number: ')
    nameVehicle=name_vehicle(j_code)
    services=service_list(j_code)
    parts=spare_part(j_code)
    service_cost=0
    parts_cost=0
    line='______________________________________________________________\n'
    line=line+'                         Invoice                            \n'
    line=line+'______________________________________________________________\n'
    customer_line='Customer:{} {}\n'
    customer_line=customer_line.format(nameVehicle[1],nameVehicle[2])
    line=line+customer_line
    vehicle_line='Vehicle:{}\n'
    vehicle_line=vehicle_line.format(nameVehicle[0])
    line=line+vehicle_line
    line=line+'--------------------------------------------------------------\n'
    for i in range(len(services[0])):
        service_line='{}        {}\n'.ljust(35)+ '{:.2f}\n'.rjust(35)
        service_line=service_line.format(services[0][i],services[1][i],float(services[2][i]))
        service_cost=service_cost+services[2][i]
        line=line+service_line
    line=line+'--------------------------------------------------------------\n'
    service_cost_line='Total Service Cost                                 {:.2f}\n'
    service_cost_line=service_cost_line.format(float(service_cost))
    line=line+service_cost_line
    line=line+'--------------------------------------------------------------\n'
    for i in range(len(parts[0])):
        parts_line='            {} {}nos.\n'.ljust(35)+ '{:.2f}\n'.rjust(45)
        parts_line=parts_line.format(parts[0][i],parts[1][i],float(parts[2][i]))
        parts_cost=parts_cost+parts[2][i]
        line=line+parts_line
    line=line+'--------------------------------------------------------------\n'
    parts_cost_line='Total Spare Parts Cost                             {:.2f}\n'
    parts_cost_line=parts_cost_line.format(float(parts_cost))
    line=line+parts_cost_line
    line=line+'--------------------------------------------------------------\n'
    total_cost=parts_cost+service_cost
    total_cost_line='Total Cost                                         {:.2f}\n'
    total_cost_line=total_cost_line.format(total_cost)
    line=line+total_cost_line
    line=line+'_______________________________________________________________\n\n'
    print (line)
    
