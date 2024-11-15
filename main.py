# Dictionary of available currencies and their full names
currencies = {
    "USD": "American Dollar",
    "EUR": "Euro",
    "GBP": "British Pound",
    "SAR": "Saudi Riyal",
    "AED": "UAE Dirham",
    "KWD": "Kuwaiti Dinar",
    "CNY": "Chinese Yuan",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "JPY": "Japanese Yen",
    "ZAR": "South African Rand",
    "NOK": "Norwegian Krone",
    "SEK": "Swedish Krona"
}

# Function to take the amount input from the user
def taking_amount():
    while True:
        global amount_calculate  # Declare a global variable to store the amount entered by the user
        try:
            # Prompt the user to input the amount they want to convert to Pakistani Rupees
            amount_calculate = float(input('Please enter the amount you would like to convert into Pakistani Rupees: '))
            print('\n')  # Add a line break for clarity
            break  # Exit the loop once a valid number is entered
        except:
            # If the input is not a valid number, ask the user to enter a number
            print('Invalid input. Please enter a valid number (e.g., 10, 100, 200).')

# Function to perform currency conversion based on the user's selection
def desired_cal():
    while True:  # Continue prompting the user until they enter a valid currency
        # Display the available currencies to the user
        for short_currency, full_name in currencies.items():
            print(f'{short_currency} : {full_name}')
        
        # Prompt the user to select a currency by its short name (e.g., USD, EUR)
        desired_currency = input('\nSelect the short name of the currency (e.g., USD, EUR) from the listed currencies: ').upper()
        
        if desired_currency not in currencies:
            # If the entered currency is not in the dictionary, notify the user
            print('Invalid currency. Please select from the listed currencies.')
        else:
            # If the selected currency is valid, perform the conversion
            match desired_currency:
                case 'USD': 
                    total = amount_calculate * 303.00  # Conversion rate for USD
                    print(f'{amount_calculate} USD is {total} Pakistani Rupees.')
                case 'EUR':
                    total = amount_calculate * 325.00  # Conversion rate for EUR
                    print(f'{amount_calculate} EUR is {total} Pakistani Rupees.')
                case 'GBP':
                    total = amount_calculate * 380.00  # Conversion rate for GBP
                    print(f'{amount_calculate} GBP is {total} Pakistani Rupees.')
                case 'SAR':
                    total = amount_calculate * 80.00  # Conversion rate for SAR
                    print(f'{amount_calculate} SAR is {total} Pakistani Rupees.')
                case 'AED':
                    total = amount_calculate * 82.50  # Conversion rate for AED
                    print(f'{amount_calculate} AED is {total} Pakistani Rupees.')
                case 'KWD':
                    total = amount_calculate * 1000.00  # Conversion rate for KWD
                    print(f'{amount_calculate} KWD is {total} Pakistani Rupees.')
                case 'CNY':
                    total = amount_calculate * 42.50  # Conversion rate for CNY
                    print(f'{amount_calculate} CNY is {total} Pakistani Rupees.')
                case 'AUD':
                    total = amount_calculate * 200.00  # Conversion rate for AUD
                    print(f'{amount_calculate} AUD is {total} Pakistani Rupees.')
                case 'CAD':
                    total = amount_calculate * 230.00  # Conversion rate for CAD
                    print(f'{amount_calculate} CAD is {total} Pakistani Rupees.')
                case 'JPY':
                    total = amount_calculate * 2.25  # Conversion rate for JPY
                    print(f'{amount_calculate} JPY is {total} Pakistani Rupees.')
                case 'ZAR':
                    total = amount_calculate * 16.00  # Conversion rate for ZAR
                    print(f'{amount_calculate} ZAR is {total} Pakistani Rupees.')
                case 'NOK':
                    total = amount_calculate * 32.00  # Conversion rate for NOK
                    print(f'{amount_calculate} NOK is {total} Pakistani Rupees.')
                case 'SEK':
                    total = amount_calculate * 30.00  # Conversion rate for SEK
                    print(f'{amount_calculate} SEK is {total} Pakistani Rupees.')
                case _:
                    # If the entered currency is somehow invalid, show an error message
                    print('Invalid currency. Please select from the listed currencies.')
            break  # Exit the loop once the currency conversion is done

# Start the currency conversion process
taking_amount()
desired_cal()

# Ask the user if they want to perform another calculation
while True:
    again = input('Would you like to perform another calculation (Yes or No)? ').lower()
    if again == 'yes' or again == 'y':
        taking_amount()  # Prompt for a new amount
        desired_cal()  # Perform the currency conversion
    else:
        print('You have closed the Currency Converter.\nSee you next time.\nTHANK YOU!')  # Display exit message
        break  # Exit the loop and end the program