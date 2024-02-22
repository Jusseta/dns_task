branches_query = 'CREATE TABLE brunches('\
                 'brunch_id integer NOT NULL,'\
                 'link text NOT NULL,'\
                 'title varchar(100) NOT NULL,'\
                 'city text NOT NULL,'\
                 'short_name varchar(100) NOT NULL,'\
                 'region varchar(100) NOT NULL);'

cities_query = 'CREATE TABLE cities('\
                'city_id integer NOT NULL,'\
                'link text NOT NULL,'\
                'name varchar(100) NOT NULL);'

products_query = 'CREATE TABLE products('\
                'product_id integer NOT NULL,'\
                'link text NOT NULL,'\
                'name text NOT NULL);'

sales_query = 'CREATE TABLE sales('\
                 'sale_id integer NOT NULL,'\
                 'period timestamp NOT NULL,'\
                 'branch text NOT NULL,'\
                 'nomenclature text NOT NULL,'\
                 'quantity decimal NOT NULL,'\
                 'sale decimal NOT NULL);'
