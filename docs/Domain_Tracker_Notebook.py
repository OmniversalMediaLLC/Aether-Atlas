
# Domain Tracker Maintenance Notebook
# Location: Aether.OmniversalMedia.Org Droplet Book / R2 Bucket

import pandas as pd
from datetime import datetime

# Load domain tracker CSV
csv_path = "Domain_Tracker_Numbers.csv"  # Adjust path if needed
df = pd.read_csv(csv_path)

# Show basic summary
print(f"Total domains: {len(df)}")
df.head()

# Flag domains expiring within the next 60 days
df['Expiration Date'] = pd.to_datetime(df['Expiration Date'], errors='coerce')
today = pd.Timestamp.now()
upcoming = df[df['Expiration Date'].notnull() & (df['Expiration Date'] - today).dt.days <= 60]

print("\nDomains expiring soon:")
display(upcoming[['Domain Name', 'Expiration Date', 'Registrar']])

# Save updated sheet if needed
def save_updated_version(filename="Domain_Tracker_Updated.csv"):
    df.to_csv(filename, index=False)
    print(f"Saved updated version to {filename}")

# Example usage:
# df.loc[df['Domain Name'] == 'example.com', 'Registrar'] = 'Dynadot'
# save_updated_version()
