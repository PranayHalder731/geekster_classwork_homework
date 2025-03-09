# Indian Military Aircraft Web Scraper 🛩️

## 📖 Overview
This project contains a **Python script (`scrape_military_aircraft.py`)** that scrapes data from the Wikipedia page **[List of active Indian military aircraft](https://en.wikipedia.org/wiki/List_of_active_Indian_military_aircraft)** and stores it in a CSV file (`indian_military_aircraft.csv`).  

## 🛠️ Technologies Used
- **Python** 🐍  
- **BeautifulSoup** (for web scraping)  
- **Requests** (to fetch webpage content)  
- **Pandas** (to process and save data)

## 📜 Files in This Repository
| File | Description |
|------|------------|
| `scrape_military_aircraft.py` | Python script to scrape the Wikipedia table |
| `indian_military_aircraft.csv` | Extracted aircraft data saved as a CSV file |
| `README.md` | Project documentation |

## 📂 How to Run the Script
### **1️⃣ Install Required Libraries**
If you haven’t already installed the dependencies, run:
```sh
pip install requests beautifulsoup4 pandas
2️⃣ Run the Script
Execute the script with:

python scrape_military_aircraft.py
3️⃣ Check Output
After execution, the scraped data will be saved in:

indian_military_aircraft.csv
📌 Example Output
The CSV file will contain data like this:

Aircraft	Origin	Role	Manufacturer	In service
Sukhoi Su-30MKI	Russia/India	Multirole Fighter	HAL/Sukhoi	260
🚀 Contributing
Feel free to open issues or create pull requests if you have improvements.

🏆 Author
📌 Pranay Halder
