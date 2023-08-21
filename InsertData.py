import psycopg2
import logging

connection = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Adetomi13',
    port='5432'
)

insert_sql_query = '''
insert into Customer(ID, name, age, address, LOAN_AMOUNT) 
values(4, 'Tomi', 24, 'CH', 15090.45)
'''

pointer = connection.cursor()
pointer.execute(insert_sql_query)

connection.commit()
print('Record is created')
connection.close()
