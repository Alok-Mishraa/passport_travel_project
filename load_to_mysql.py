import pandas as pd
import mysql.connector

# Load CSV
df = pd.read_csv("passport_travel_data.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",        
    password="your_password_here",  
    database="travel_project"
)

cursor = conn.cursor()

# Insert query
query = """
INSERT INTO travel_data (
    Passenger_ID, Name, Age, Gender, Passport_Number,
    Nationality, Departure_Country, Arrival_Country,
    Travel_Date, Travel_Type, Purpose, VIP_Status,
    Flight_Number, Airport
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Convert dataframe to list
data = df.values.tolist()

# Insert in batches (fast + safe)
batch_size = 5000

for i in range(0, len(data), batch_size):
    batch = data[i:i+batch_size]
    cursor.executemany(query, batch)
    conn.commit()
    print(f"Inserted {i + len(batch)} rows")

cursor.close()
conn.close()

print("Data inserted successfully!")