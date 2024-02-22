import csv
import psycopg2
import servicies


connection = psycopg2.connect(
    host='localhost',
    database='dns_task',
    user='postgres',
    password='qwerty'
)

try:
    with connection:
        with connection.cursor() as cursor:
            # раскомментировать при повторном запуске программы
            # cursor.execute('DROP TABLE cities, brunches, products, sales')

            cursor.execute(servicies.cities_query)
            cursor.execute(servicies.branches_query)
            cursor.execute(servicies.products_query)
            cursor.execute(servicies.sales_query)

            with open('t_cities.csv') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    city_id = row['']
                    link = row['Ссылка']
                    name = row['Наименование']
                    cursor.execute('INSERT INTO cities VALUES (%s, %s, %s)',
                                   (city_id, link, name,))

            with open('t_branches.csv') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    brunch_id = row['']
                    link = row['Ссылка']
                    title = row['Наименование']
                    city = row['Город']
                    short_name = row['КраткоеНаименование']
                    region = row['Регион']
                    cursor.execute('INSERT INTO brunches VALUES (%s, %s, %s, %s, %s, %s)',
                                   (brunch_id, link, title, city, short_name, region,))

            with open('t_products.csv') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    product_id = row['']
                    link = row['Ссылка']
                    name = row['Наименование']
                    cursor.execute('INSERT INTO products VALUES (%s, %s, %s)',
                                   (product_id, link, name,))

            with open('t_sales.csv') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    sale_id = row['']
                    period = row['Период']
                    branch = row['Филиал']
                    nomenclature = row['Номенклатура']
                    quantity = row['Количество']
                    sale = row['Продажа']
                    cursor.execute('INSERT INTO sales VALUES (%s, %s, %s, %s, %s, %s)',
                                   (sale_id, period, branch, nomenclature, quantity, sale,))

finally:
    connection.close()
