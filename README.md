# 💱 Currency Converter (Python)

> **Made with ❤️ by Manav** – a 17-year-old passionate 12th-grade developer who loves building useful tools for developers and learners.  
> This project is a **powerful CLI-based Currency Converter** that uses live exchange rates and caching to work efficiently — even offline.

---

## 🚀 Features

✅ **Live Exchange Rates** – Uses [ExchangeRate API](https://www.exchangerate-api.com/) to get the latest data  
✅ **24h Local Cache** – Saves API results in `rates_cache.json` to avoid unnecessary requests  
✅ **Offline Mode** – Falls back to cached rates or default rates if API is unavailable  
✅ **Multi-Currency Support** – Convert between dozens of currencies  
✅ **Direct Exchange Rate Display** – Shows rate between selected currencies  
✅ **Error Handling** – Gracefully handles network errors & unsupported currencies  

---

## 🛠️ Tech Stack

- **Python 3.x**
- `requests` – For API calls  
- `json` – For caching exchange rates locally  
- `datetime` – For cache validation  

---

## 📸 Preview

```
==================================================
CURRENCY CONVERTER
==================================================

Last update: 2025-09-17 20:15:23
Supported currencies: AUD, BRL, CAD, CHF, CNY, EUR, GBP, INR, JPY, MXN, RUB, USD

Enter amount to convert: 100
From currency (e.g., USD): USD
To currency (e.g., INR): INR

100 USD = 7400.0 INR
Exchange rate: 1 USD = 74.0000 INR
```

---

## 📂 Project Structure

```bash
.
├── currency_converter.py   # Main program
├── rates_cache.json        # Auto-generated cache file
└── README.md               # Documentation
```

---

## ⚡ Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/currency-converter.git
cd currency-converter
```

### 2️⃣ Install Dependencies
```bash
pip install requests
```

### 3️⃣ Get Your API Key
1. Go to [ExchangeRate API](https://www.exchangerate-api.com/)
2. Sign up for a free API key  
3. Copy the key and paste it in the code:
```python
API_KEY = "YOUR_API_KEY_HERE"
```

### 4️⃣ Run the Converter
```bash
python currency_converter.py
```

---

## 💡 Example

**Input**
```
Amount: 50
From: EUR
To: USD
```

**Output**
```
50 EUR = 58.82 USD
Exchange rate: 1 EUR = 1.1765 USD
```

---

## 💡 Future Improvements

- [ ] Add GUI using Tkinter for a more user-friendly experience  
- [ ] Add support for multiple conversions in one go  
- [ ] Show historical exchange rates (last 7 days)  
- [ ] Export results to CSV or text file  

---

## 🧑‍💻 About the Creator

Hi! I'm **Manav**, a **12th-grade student (17 y/o)** who loves building tools that solve real-world problems.  
This project was made to help travelers, developers, and students convert currencies quickly without opening multiple websites.  

---

## ⭐ Contribute

- Found a bug? Open an issue  
- Have an idea? Create a pull request  

If you liked this project, give it a ⭐ on GitHub and share it with others.  

---

**"Made with ❤️ and Python by Manav."**
