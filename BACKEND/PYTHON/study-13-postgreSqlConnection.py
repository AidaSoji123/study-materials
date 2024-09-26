import psycopg2

try:
    # Establishing the connection
    connection = psycopg2.connect(
        user="postgres",              
        password="12345",             
        host="127.0.0.1",             
        port="5432",                  
        database="python_db"          
    )

    cursor = connection.cursor()

    # Print PostgreSQL connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Execute a query to get the PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
    

    # Step 1: Create a table (if it doesn't already exist)
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        age INT NOT NULL,
        department TEXT NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table 'employees' created successfully")

    # Step 2: Insert multiple records into the table
    insert_query = '''
    INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)
    '''
    records_to_insert = [
        ('John Doe', 30, 'Engineering'),
        ('Jane Smith', 28, 'Marketing'),
        ('Alice Johnson', 35, 'Human Resources')
    ]

    # Executing the insert query for multiple records
    cursor.executemany(insert_query, records_to_insert)
    connection.commit()
    print("Records inserted successfully into 'employees' table")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # Ensure that connection exists before attempting to close it
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
