import psycopg2
import logging

connection = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Adetomi13',
    port='5432'
)

table_select_query = '''
    select * from customer
'''

pointer = connection.cursor()
pointer.execute(table_select_query)
rows = pointer.fetchall()
for each_row in rows:
    print(each_row[1], '-----', each_row[-1])
# connection.commit()
# print(rows)
# connection.close()
