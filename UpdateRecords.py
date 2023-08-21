import psycopg2
import logging

connection = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Adetomi13',
    port='5432'
)

update_sql_query = '''
update customer set age=65 where id=2
'''

pointer = connection.cursor()
pointer.execute(update_sql_query)

connection.commit()
print('Record is updated')
connection.close()
