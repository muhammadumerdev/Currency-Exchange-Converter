import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('API_KEY')

def pair_conversion(pair_from, pair_to, amount):
    # Define the URL with the necessary parameters
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{pair_from}/{pair_to}"
   
    try:
        # Send the GET request
        response = requests.get(url)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()

        # Extract conversion rate
        conversion_rate = data.get('conversion_rate', 'No conversion rate available')

        if isinstance(conversion_rate, str):
            print(conversion_rate)
            return
        
        # Calculate converted amount
        converted_amount = amount * conversion_rate

        # Print or process the data
        print(f"Conversion rate from {pair_from} to {pair_to}: {conversion_rate}")
        print(f"Converted amount: {converted_amount}")
    
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        print(f"An error occurred: {e}")

# Example usage
first = input("Enter the first pair (From):").upper()
last = input("Enter the second pair (To):").upper()
amount = float(input("Enter the amount please: "))

pair_conversion(first, last, amount)
