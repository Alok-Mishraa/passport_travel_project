import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

num_rows = 100000

countries = ["India", "USA", "UK", "Canada", "Australia", "Germany", "UAE", "Singapore"]
airports = ["DEL", "BOM", "BLR", "DXB", "JFK", "LHR", "SIN"]
purposes = ["Tourism", "Business", "Study"]

data = []

for _ in range(num_rows):
    departure = random.choice(countries)
    arrival = random.choice([c for c in countries if c != departure])

    data.append({
        "Passenger_ID": fake.uuid4(),
        "Name": fake.name(),
        "Age": random.randint(18, 75),
        "Gender": random.choice(["Male", "Female"]),
        "Passport_Number": fake.bothify(text='??######'),
        "Nationality": random.choice(countries),
        "Departure_Country": departure,
        "Arrival_Country": arrival,
        "Travel_Date": fake.date_between(start_date='-2y', end_date='today'),
        "Travel_Type": "Outbound" if departure == "India" else "Inbound",
        "Purpose": random.choice(purposes),
        "VIP_Status": random.choices(["Yes", "No"], weights=[5, 95])[0],
        "Flight_Number": f"{random.choice(['AI','EK','BA','UA'])}{random.randint(100,999)}",
        "Airport": random.choice(airports)
    })

df = pd.DataFrame(data)

df.to_csv("passport_travel_data.csv", index=False)

print("Dataset generated successfully!")