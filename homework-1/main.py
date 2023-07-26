"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

CUSTOMERS_FILE = "north_data\customers_data.csv"
EMPLOYSEES_FILE = "north_data\employees_data.csv"
ORDERS_FILE = "north_data\orders_data.csv"


#connect to db
conn = psycopg2.connect(host = "localhost", database = 'north', user = 'postgres', password = '128943')
try:
    with conn:
            with open(CUSTOMERS_FILE, 'r', encoding='utf-8') as file:
                file_reader = csv.reader(file, delimiter=",")
                count=0
                for row in file_reader:
                    if row[0] != "customer_id" and row[1] != "company_name" and row[2] != "contact_name":
                        with conn.cursor() as cur:

                        #execute query
                            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (row[0],row[1],row[2]))
                    count += 1

            with open(EMPLOYSEES_FILE, 'r', encoding='utf-8') as file:
                file_reader = csv.reader(file, delimiter=",")
                count=0
                for row in file_reader:
                    if row[0] != "employee_id" and row[1] != "first_name" and row[2] != "last_name"  and row[3] != "title"  and row[4] != "birth_date" and row[5] != "notes" :
                        with conn.cursor() as cur:
                        #execute query
                            cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (row[0],row[1],row[2],row[3],row[4],row[5]))
                    count += 1

            with open(ORDERS_FILE, 'r', encoding='utf-8') as file:
                file_reader = csv.reader(file, delimiter=",")
                count = 0
                for row in file_reader:
                    if row[0] != "order_id" and row[1] != "customer_id" and row[2] != "employee_id" and row[3] != "order_date" and row[4] != "ship_city":
                        with conn.cursor() as cur:
                            # execute query
                            cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4]))
                    count += 1

finally:
    conn.close()

