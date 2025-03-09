import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_active_Indian_military_aircraft"

# Send a GET request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all tables on the page
    tables = soup.find_all("table", {"class": "wikitable"})

    # Extract table data (assuming the first relevant table)
    table = tables[0]  # Adjust index if needed

    # Extract column headers
    headers = [header.text.strip() for header in table.find_all("th")]

    # Extract table rows
    rows = []
    for row in table.find_all("tr")[1:]:  # Skip header row
        cells = row.find_all(["td", "th"])  # Include 'th' if row headers exist
        row_data = [cell.text.strip() for cell in cells]

        # Ensure row data matches column count by padding or truncating
        if len(row_data) < len(headers):
            row_data.extend([""] * (len(headers) - len(row_data)))  # Fill missing values
        elif len(row_data) > len(headers):
            row_data = row_data[:len(headers)]  # Trim extra values

        rows.append(row_data)

    # Convert data into a DataFrame
    df = pd.DataFrame(rows, columns=headers)

    # Save to CSV file
    df.to_csv("indian_military_aircraft.csv", index=False, encoding="utf-8")

    print("Data successfully scraped and saved to 'indian_military_aircraft.csv'.")
else:
    print(f"Failed to retrieve the page. Status Code: {response.status_code}")
