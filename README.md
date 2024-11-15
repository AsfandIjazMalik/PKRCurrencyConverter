# PKRCurrencyConverter
Python Programming 

### Important Note:
This project was developed on 15th November 2024 with exchange rates set according to the values available on that day. You can modify the exchange rates in the code as per the latest available rates, making this project flexible and adaptable to future changes. <br>
## Overview
This project is a simple Currency Converter that allows users to convert a given amount of money from various currencies to Pakistani Rupees (PKR). The program takes the amount from the user and lets them choose from a list of available currencies to perform the conversion. <br>
### Features
•	Supports conversion for 13 different currencies: <br>
o	USD (American Dollar) <br>
o	EUR (Euro) <br>
o	GBP (British Pound) <br>
o	SAR (Saudi Riyal) <br>
o	AED (UAE Dirham) <br>
o	KWD (Kuwaiti Dinar) <br>
o	CNY (Chinese Yuan) <br>
o	AUD (Australian Dollar) <br>
o	CAD (Canadian Dollar) <br>
o	JPY (Japanese Yen) <br>
o	ZAR (South African Rand) <br>
o	NOK (Norwegian Krone) <br>
o	SEK (Swedish Krona) <br>
•	User-friendly interface to input the amount and select the desired currency. <br>
•	Error handling for invalid input and currency selection. <br>
•	Option to perform multiple conversions. <br>
### Python Concepts Used<br>
This project utilizes several core Python concepts, including: <br>
1.	Data Structures: <br>
o	Dictionaries: Used to store currency codes and their corresponding names. <br>
o	Example: currencies = {"USD": "American Dollar", "EUR": "Euro", ...} <br>
2.	Loops: <br>
o	While Loop: Used to repeatedly prompt the user for input until valid data is entered (e.g., amount to convert and valid currency selection).
o	Example: while True: <br>
3.	Conditionals: <br>
o	If-Else Statements: Used to check if the user's input matches a valid currency code and to perform the corresponding conversion. <br>
o	Example: if desired_currency not in currencies: <br>
4.	Error Handling: <br>
o	Try-Except: Used to catch invalid inputs (e.g., non-numeric values when entering the amount) and prevent the program from crashing. <br>
o	Example: try: ... except: <br>
5.	User Input: <br>
o	Input Function: Used to take user input for the amount to convert and the desired currency. <br>
o	Example: input('How much amount would you like to convert into Pakistani Rupees: ') <br>
6.	String Manipulation: <br>
o	Upper() Method: Used to ensure that the user's input for currency selection is case-insensitive. <br>
o	Example: desired_currency = input().upper()<br>
7.	Match-Case:
o	Match-Case Statements: Used for selecting the correct conversion rate based on the currency code entered by the user. <br>
o	Example: <br>
python<br>
Copy code<br>
match desired_currency: <br>
    case 'USD': <br>
        # Conversion logic here<br>
8.	Global Variables: <br>
o	Global Scope: Used to store the amount to be converted (amount_calculate) and make it accessible across different functions. <br>
o	Example: global amount_calculate<br>
9.	Loops and Flow Control: <br>
o	Break Statement: Used to exit the loop once the valid conversion is made or if the user opts out. <br>
o	Example: break # Exit the loop<br>
### How It Works<br>
1.	Input the Amount: The user is prompted to enter the amount of money they would like to convert to Pakistani Rupees (PKR). <br>
2.	Currency Selection: The user selects a currency by entering the short code (e.g., USD, EUR, etc.) from the available options. <br>
3.	Conversion: The program calculates the equivalent amount in PKR based on the selected currency and displays the result. <br>
4.	Repeat or Exit: After the conversion, the user can choose to perform another calculation or exit the program. <br>

