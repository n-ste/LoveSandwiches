import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    get sales data for input from user
    """
    while True:
        print("Please enter sales data from last market.")
        print("Data should be six numbers, spearated by commas")
        print("Example: 10, 20, 30, 40, 50, 60")

        data_str = input("Enter your data here: ")
        print(f"The data provided is {data_str}")

        sales_data = data_str.split(",")
        validate_data(sales_data)
        
        if validate_data(sales_data):
            print("Data is valid")
            break 
        
    return sales_data

def validate_data(values):
    """
    inside the try, converts all string values to integers.
    Raises ValueError if strings cannot be convertet
    or if there arent exactly 6 integers
    """
    print(values)
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False
        
    return True

data = get_sales_data()

get_sales_data()

