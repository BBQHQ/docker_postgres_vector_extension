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

# Execute a query
cur.execute("SELECT version()")

# Fetch the result
version = cur.fetchone()
print("PostgreSQL version:", version)

# Close the cursor and connection
cur.close()
conn.close()