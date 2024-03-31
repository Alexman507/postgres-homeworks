import csv

import psycopg2

"""Скрипт для заполнения данными таблиц в БД Postgres."""

conn_params = {
    "host": "localhost",
    "database": "north",
    "user": "postgres",
    "password": "123"
}

csv_files = {
    "employees": "north_data/employees_data.csv",
    "customers": "north_data/customers_data.csv",
    "orders": "north_data/orders_data.csv"
}


def load_csv():
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            for name, data in csv_files.items():
                with open(data) as d:
                    iter_file = next(d)
                    opened_file = csv.reader(d)
                    for row in opened_file:
                        if name == "employees":
                            query = "insert into employees values(%s, %s, %s, %s, %s, %s)"
                        elif name == "customers":
                            query = "insert into customers values(%s, %s, %s)"
                        elif name == "orders":
                            query = "insert into orders values(%s, %s, %s, %s, %s)"
                        cur.execute(query, row)
        conn.commit()
        print("Данные в таблицах успешно добавлены")
        # conn.close()


def clear_tables():
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM orders")
            cur.execute("DELETE FROM customers")
            cur.execute("DELETE FROM employees")
        conn.commit()
        print("Данные в таблицах успешно удалены")
        # conn.close()


if __name__ == "__main__":
    load_csv()
    # clear_tables()
