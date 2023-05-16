# Python_REST_PostgresSQL

#This is server

http://localhost:8000

- Make sure port 8000 is not used by other apps,

Install PostgresSQL

- pip install psycopg2 

-default port 5432

-use localhost for server


postgres=# 



First:

-Create Database  : 

postgres=# 
 CREATE DATABASE postgres



-Create table :  public.your_table_name


         CREATE TABLE your_table_name (
           data json
            );
            
            CREATE TABLE
            

- Run client in the new terminal and keep server terminal running, 


Output:
            # /Users/morali/PycharmProjects/postgressql/venv/bin/python /Users/morali/PycharmProjects/postgressql/client.py 
            Success
            Process finished with exit code 0



- example of Query: 


         $ SELECT * FROM your_table_name WHERE data->>'age' = '35';
          
          
          
          # {"data": "Morteza", "age": 35, "email": "mortexa.A@example.com"}



