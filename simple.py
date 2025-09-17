import requests
import json
from datetime import datetime, timedelta

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://v6.exchangerate-api.com/v6"
        self.rates = {}
        self.last_update = None
        self.load_cached_rates()
    
    def load_cached_rates(self):
        """Load rates from cache file if available and not expired"""
        try:
            with open('rates_cache.json', 'r') as f:
                cache = json.load(f)
                # Check if cache is less than 24 hours old
                cache_time = datetime.fromisoformat(cache['timestamp'])
                if datetime.now() - cache_time < timedelta(hours=24):
                    self.rates = cache['rates']
                    self.last_update = cache_time
                    print("Using cached exchange rates")
                    return True
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        return False
    
    def save_cached_rates(self):
        """Save current rates to cache file"""
        cache_data = {
            'timestamp': datetime.now().isoformat(),
            'rates': self.rates
        }
        with open('rates_cache.json', 'w') as f:
            json.dump(cache_data, f)
    
    def fetch_exchange_rates(self, base_currency='USD'):
        """Fetch latest exchange rates from API"""
        try:
            print("Fetching latest exchange rates...")
            response = requests.get(f"{self.base_url}/{self.api_key}/latest/{base_currency}")
            response.raise_for_status()
            data = response.json()
            
            if data['result'] == 'success':
                self.rates = data['conversion_rates']
                self.last_update = datetime.now()
                self.save_cached_rates()
                print("Exchange rates updated successfully!")
                return True
            else:
                print(f"API Error: {data.get('error-type', 'Unknown error')}")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            if not self.rates:
                print("No cached rates available. Using default rates.")
                self.rates = self.get_default_rates()
            return False
    
    def get_default_rates(self):
        """Return default rates if API is unavailable"""
        return {
            'USD': 1.0, 'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.0,
            'CAD': 1.25, 'AUD': 1.35, 'CHF': 0.92, 'CNY': 6.45,
            'INR': 74.0, 'BRL': 5.5, 'RUB': 75.0, 'MXN': 20.0
        }
    
    def get_supported_currencies(self):
        """Return list of supported currency codes"""
        return list(self.rates.keys())
    
    def convert(self, amount, from_currency, to_currency):
        """Convert amount from one currency to another"""
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        
        if from_currency not in self.rates:
            raise ValueError(f"Unsupported currency: {from_currency}")
        if to_currency not in self.rates:
            raise ValueError(f"Unsupported currency: {to_currency}")
        
        # Convert to USD first, then to target currency
        amount_in_usd = amount / self.rates[from_currency]
        converted_amount = amount_in_usd * self.rates[to_currency]
        
        return round(converted_amount, 2)
    
    def get_exchange_rate(self, from_currency, to_currency):
        """Get direct exchange rate between two currencies"""
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        
        if from_currency not in self.rates or to_currency not in self.rates:
            return None
        
        return self.rates[to_currency] / self.rates[from_currency]

def main():
    # Replace with your API key from https://www.exchangerate-api.com/
    API_KEY = "YOUR_API_KEY_HERE"
    
    converter = CurrencyConverter(API_KEY)
    
    # Try to fetch latest rates, fall back to cache or defaults
    if not converter.fetch_exchange_rates():
        if not converter.rates:
            print("Using default exchange rates")
    
    print("\n" + "="*50)
    print("CURRENCY CONVERTER")
    print("="*50)
    
    while True:
        print(f"\nLast update: {converter.last_update}")
        print("Supported currencies:", ", ".join(sorted(converter.get_supported_currencies())))
        
        try:
            amount = float(input("\nEnter amount to convert: "))
            from_curr = input("From currency (e.g., USD): ").upper()
            to_curr = input("To currency (e.g., EUR): ").upper()
            
            result = converter.convert(amount, from_curr, to_curr)
            rate = converter.get_exchange_rate(from_curr, to_curr)
            
            print(f"\n{amount} {from_curr} = {result} {to_curr}")
            print(f"Exchange rate: 1 {from_curr} = {rate:.4f} {to_curr}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        
        another = input("\nConvert another? (y/n): ").lower()
        if another != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()