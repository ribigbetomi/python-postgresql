import psycopg2
import logging

connection = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Adetomi13',
    port='5432'
)

# print(connection)

table_customer__query = '''
    CREATE TABLE Customer(
        ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE INT NOT NULL,
        ADDRESS CHAR(100),
        LOAN_AMOUNT REAL
    )
'''

pointer = connection.cursor()

try:
    pointer.execute(table_customer_query)
    connection.commit()
    logging.info("Table is created")
except Exception as e:
    logging.error('Table is duplicated', e)
finally:
    connection.close()
