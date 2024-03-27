import psycopg2

# Connection details
host = "localhost"
port = "5432"
database = "postgres"
user = "postgres"
password = "postgres"

# Establish a connection
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

# Create a cursor
cur = conn.cursor()

# Create a table
cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER,
        salary DECIMAL(10, 2)
    )
""")

# Insert sample data
cur.execute("INSERT INTO employees (name, age, salary) VALUES (%s, %s, %s)", ("John Doe", 30, 50000.00))
cur.execute("INSERT INTO employees (name, age, salary) VALUES (%s, %s, %s)", ("Jane Smith", 35, 60000.00))
cur.execute("INSERT INTO employees (name, age, salary) VALUES (%s, %s, %s)", ("Mike Johnson", 28, 45000.00))

# Commit the changes
conn.commit()

# Retrieve data from the table
cur.execute("SELECT * FROM employees")
rows = cur.fetchall()

# Print the retrieved data
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()