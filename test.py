# class A():
#   name = 'koddos'
#   def display(self):
#     print('print from A')


# class B(A):

#   def display(self,nameasdf):
#      print('print from B',nameasdf)

#   def display(self,name,l_name):
#       print('print from B',name,l_name)


# obj =  B()
# obj.display('mahbub','alam')

import calendar
from datetime import date, datetime, timedelta, time
from sys import stdout
from typing import Union
from colorama import Fore
from dateutil.parser import parse
def duration_calculation(from_date: Union[datetime, date, str], duration_format: str, duration_unit: int, reverse: bool = False):
    """
    Get calculated date time from duration format and duration unit by adding/subtracting

    Args:
        from_date (Union[datetime,date,str]): _description_
        duration_format (str): _description_
        duration_unit (int): _description_
        reverse (bool, optional): _description_. Defaults to False.

    Returns:
        calculated datetime: datetime
    """
    if from_date and isinstance(from_date, date):
        datetime_obj = datetime.combine(from_date, time.min)
    elif from_date and isinstance(from_date, str):
        datetime_obj = datetime.strptime(from_date, "%Y-%m-%d")
    elif from_date and isinstance(from_date, datetime):
        datetime_obj = from_date.replace(hour=0, minute=0, second=0)
    else:
        datetime_obj = datetime.now().replace(hour=0, minute=0, second=0)

    if reverse == False:
        if duration_format == 'month':
            initial_day = datetime_obj.day
            print("initial_day-->", initial_day)
            for month in range(duration_unit):
                print("\ndatetime_obj-->", datetime_obj)
                # curr_total_days = calendar.monthrange(datetime_obj.year, datetime_obj.month)[1]
                # datetime_obj = datetime_obj + timedelta(days=curr_total_days)

                month_number = datetime_obj.month + 1
                if month_number <= 12:
                    current_day = datetime_obj.day
                    forward_month_days = calendar.monthrange(
                        datetime_obj.year, datetime_obj.month + 1)[1]
                    print("current_day-->", current_day)
                    print("forward_month_days-->", forward_month_days)

                    if current_day > forward_month_days:
                        current_day = forward_month_days

                    datetime_obj = datetime_obj.replace(
                        month=month_number, day=current_day)

                else:
                    datetime_obj = datetime_obj.replace(
                        year=(datetime_obj.year + 1), month=1)

                print("loopend-->", month, 'datetime_obj-->', datetime_obj)

                print("==========")
            # mitigate mismatch after calculation with diff with initial day
            if initial_day > datetime_obj.day:
                datetime_obj = datetime_obj + timedelta(days=1)

        elif duration_format == 'year':

            datetime_obj = datetime_obj.replace(
                year=(datetime_obj.year + duration_unit))

        elif duration_format == 'day':
            datetime_obj = datetime_obj + timedelta(days=duration_unit)

        elif duration_format == 'week':
            datetime_obj = datetime_obj + timedelta(weeks=duration_unit)

        # elif duration_format == 'hour':
        #     datetime_obj = datetime_obj + timedelta(hours=duration_unit)

        return datetime_obj

    else:
        if duration_format == 'month':
            for month in range(duration_unit):
                month_number = datetime_obj.month - 1
                if month_number >= 1:
                    current_day = datetime_obj.day
                    backward_month_days = calendar.monthrange(
                        datetime_obj.year, datetime_obj.month - 1)[1]
                    print("current_day-->", current_day)
                    print("backward_month_days-->", backward_month_days)
                    print("==========")
                    if current_day > backward_month_days:
                        current_day = backward_month_days
                    datetime_obj = datetime_obj.replace(month=month_number)
                else:
                    datetime_obj = datetime_obj.replace(
                        year=(datetime_obj.year - 1), month=12)

        elif duration_format == 'year':

            datetime_obj = datetime_obj.replace(
                year=(datetime_obj.year - duration_unit))

        elif duration_format == 'day':
            datetime_obj = datetime_obj - timedelta(days=duration_unit)

        elif duration_format == 'week':
            datetime_obj = datetime_obj - timedelta(weeks=duration_unit)

        # elif duration_format == 'hour':
        #     datetime_obj = datetime_obj - timedelta(hours=duration_unit)

        return datetime_obj


# date_obj =  duration_calculation('2020-05-31','month',2)  - timedelta(seconds=1)
# print('date_obj: ', date_obj)
# date_obj2 =  duration_calculation('2020-01-25','month',1)
# print('date_obj2: ', date_obj2)

d = {'k1': 1, 'k2': 2, 'k3': 3}
try:
    d.pop('k1s')
except:
    pass

# {'k2': 2, 'k3': 3}

# print(removed_value)


def format_number(number):
    """
    thousand seperator
    """
    if isinstance(number, int):
        # Format integer number
        return "{:,.0f}".format(number)
    elif isinstance(number, float):
        # Format float number
        return "{:,.2f}".format(number)
    else:
        return str(number)  # Return as is if not int or float


num1 = 1900
num2 = -741320651.8998456165

formatted_num1 = format_number(num1)
formatted_num2 = format_number(num2)







valid_to = '1983-10-09T00:00:00'
parsed_date = parse(valid_to).strftime('%d %b %Y %H:%M:%S')
# if type(valid_to) == str:
#     try:
#     except:
#         parsed_date = datetime.now().strftime('%d %b %Y %H:%M:%S')
# elif type(valid_to) == datetime or type(valid_to) == date:
#      parsed_date = valid_to.strftime('%d %b %Y %H:%M:%S')
# else:
#      parsed_date = datetime.now().strftime('%d %b %Y %H:%M:%S')

# print("parsed_date", parsed_date)


# import re

# def create_dict_from_mikrotik_text(text):
#     # Find all key-value pairs using regex
#     """
#     Create a dictionary from text containing key-value pairs.

#     The function takes a text string as input, where each key-value pair is
#     separated by the '=' sign. The left side of the '=' sign represents the
#     key, and the right side represents the value. The function extracts all
#     key-value pairs from the text and returns them as a dictionary.

#     Args:
#         text (str): The input text containing key-value pairs.

#     Returns:
#         dict: A dictionary containing the extracted key-value pairs.

#     Example:
#         text = "0 R name=mahbub.alum service=pppoe caller-id=9C:C9:EB:F8:C9:10"

#         result = create_dict_from_mikrotik_text(text)

#         print(result)
#         # Output: {'name': 'mahbub.alum', 'service': 'pppoe', 'caller-id': '9C:C9:EB:F8:C9:10'}
#     """
#     pattern = r'(\S+)\s*=\s*(\S+)'
#     pairs = re.findall(pattern, text)

#     # Create a dictionary
#     result = {}

#     # Process each key-value pair
#     for pair in pairs:
#         key, value = pair
#         result[key] = value

#     return result

# text = "0 R name=mahbub.alum service=pppoe caller-id=9C:C9:EB:F8:C9:10 address=0.0.0.0 uptime=22m21s encoding= session-id=0x8160035A limit-bytes-in=0 limit-bytes-out=0"

# result = create_dict_from_mikrotik_text(text)
# print(result)

# range_start = ''
# range_end = ''
# slab = ''
# if slab:
#     try:
#         range_start,range_end =  slab.split('-')
#         print("range_start", range_start)
#         print("range_end", range_end)
#     except Exception as e:
#         print('error',e)
# else:
#     print('khali')


def check_slab_conflict(existing_slab:str, new_slab:str):
    # Extract lower and upper limits from the existing slab
    existing_lower, existing_upper = map(int, existing_slab.split('-'))
    
    # Extract lower and upper limits from the new slab
    new_lower, new_upper = map(int, new_slab.split('-'))
    
    # Check for overlap
    if (new_lower >= existing_lower and new_lower <= existing_upper) or \
       (new_upper >= existing_lower and new_upper <= existing_upper) or \
       (existing_lower >= new_lower and existing_lower <= new_upper) or \
       (existing_upper >= new_lower and existing_upper <= new_upper):
        return True  # There is an overlap
    else:
        return False  # No overlap

# Test cases
existing_slab = '0-100'
new_slab_1 = '101-105'


# print('result-->',check_slab_conflict(existing_slab, new_slab_1))




from collections import Counter

def get_identifier(item):
    # Customize this function to return a unique identifier from the dictionary item
    # For example, if the dictionary item has an 'id' key, you can use item['id'] as the identifier.
    # Modify this function based on your specific use case.
    return f"{item['id']}-mahbub" 

def find_duplicates_and_count(list_of_dicts):
    identifier_counter = Counter(get_identifier(item) for item in list_of_dicts)
    duplicates = {identifier: count for identifier, count in identifier_counter.items() if count > 1}
    return duplicates

# Example usage:
list_of_dicts = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 1, 'name': 'Charlie'},
    {'id': 1, 'name': 'Alice'},
    {'id': 4, 'name': 'David'},
    {'id': 2, 'name': 'Bob'},
    {'id': 5, 'name': 'Eve'},
]

duplicates = find_duplicates_and_count(list_of_dicts)
# print(duplicates)


def count_duplicates(list_of_dicts,keys:list):
        counts = {}
        duplicates = []

        for item in list_of_dicts:

            item_key = "-".join([str(item.get(key,'')) for key in keys])

            counts[item_key] = counts.get(item_key, 0) + 1

        for item_key, count in counts.items():
            if count > 1:
                duplicates.append({"combination" :item_key,"count" : count })

        return duplicates

# Example usage:
data = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "John"},
    {"id": 2, "name": "John"},
]

key_to_check = "id"
duplicates = count_duplicates(data, ['id','name'])
print(duplicates)

# print(round(856.45))


toList, ccList, bccList =  [[], [], []]


# if toList == ccList == bccList == []:
#     print("Warning: No email group found.")
           
# else:
#     print("Active: No email group found.")
checking = True
checking_till= False
not_is_null= True
# print('checking',checking or checking_till)

a,b,c = 0,2,5
# print("a", a);print("b", b);print("c", c);c=checking==True;print("c", c)
# if checking==True:print("a", a);print("b", b);print("c", c);c=checking==True;print("c", c)


sopose = 'few' if checking==True else 'monda'
# let sopose =  checking==True ? few' : 'monda'

# effective_deactivation_date =  datetime.now().date()
# nttn_effective_deactivation_date =  datetime.now().date() +  timedelta(days=2)
# if nttn_effective_deactivation_date and nttn_effective_deactivation_date > effective_deactivation_date :
#     print("passed")

credit_limit = 306
available_balance = -16
credit_consumed = 0

def credit_consumed(credit_limit,available_balance):
    """
    credit_consumed calculation

    Args:
        credit_limit (float): allocated credit limit for the reseller
        available_balance (float): available_balance of the reseller

    Returns:
        float: credit consumed amount
    """
    if available_balance > credit_limit:
        # as available balance is higher than the credit limit,so no credit consumed yet.
        return 0
    elif available_balance < 1:
        # consumed full credit amount, as available_balance is less then 1
        return credit_limit
    else:
        return (credit_limit - available_balance)
    
# print("credit_consumed-->",credit_consumed(credit_limit,available_balance))

# interested_on = 'alicense_lisp'
# is_reseller =  interested_on in ['license_lisp','non_license_lisp']
# print("is_reseller", is_reseller)


def colorPrint(*values, color='green'):
    """
    Print color text  instead of regular print() on terminal.
    
    Especially for debugging

    Args:
        msg (str): print string / message
        color (str, optional): text color name. Defaults to 'green'... 
        see Fore doc string for available options
    """
    for msg in values:
        print(getattr(Fore,color.upper(),Fore.GREEN) + str(msg) + Fore.RESET)



# colorPrint('my name is khan','your name is khan','RED')

def color_debug(*values, color='green'):
    """
    Color prints for multiple values stream.
    
    Especially for debugging

    Args:
        values (str): pass multiple print string / message as arguments
        color (str, optional): text color name. Defaults to 'green'... 
        see Fore doc string for available options
    """
    message = " ".join([str(i) for i in values])
    # print(getattr(Fore,color.upper(),Fore.GREEN) + message + Fore.RESET)

# color_debug(Fore,color='red')


def calculate_total_limit (start_date:date,till_date:date,total_sales:float):
    print("====================================================")
    print("start_date-->", start_date,"till_date-->", till_date)
    diff_days = abs((till_date - start_date).days) + 1
    month_end = start_date.replace(day=calendar.monthrange(start_date.year, start_date.month)[1]) 
    print("diff_days-->", diff_days,"month_end-->", month_end.day)

    if till_date > month_end :
        cal_diff_days = abs((month_end - start_date).days) + 1
        print("cal_diff_days-->", cal_diff_days)
        amount = (total_sales/month_end.day) * cal_diff_days
        print("bill amount-->", amount)
        start_date = (month_end + timedelta(days=1))
        return  amount + calculate_total_limit(start_date,till_date,total_sales)
    
    else:
        amount = (total_sales/month_end.day) * diff_days
        print("bill amount-->", amount)
        return amount
        
sales_amount = 100
billing_scheme = 14
start_date =  datetime.now().today()
till_date = start_date + timedelta(days=billing_scheme-1)

# print(round(calculate_total_limit(start_date,till_date,sales_amount)))


start_date =  datetime.strptime("2023-12-17","%Y-%m-%d")
till_date =  datetime.strptime("2023-12-31","%Y-%m-%d")
days_diff= abs((till_date - start_date).days )
# print("days_diff-->", days_diff)

# print("b-->", val)
# from datetime import datetime

from datetime import datetime

def calculate_duration(d1, d2):
    # Calculate the time difference
    time_difference = d2 - d1

    # Extract days, hours, minutes, and seconds
    days, seconds = time_difference.days, time_difference.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    # Build the duration string dynamically
    duration_parts = []
    if days:
        duration_parts.append("{} days".format(days))
    if hours:
        duration_parts.append("{} hours".format(hours))
    if minutes:
        duration_parts.append("{} minutes".format(minutes))
    if seconds:
        duration_parts.append("{} seconds".format(seconds))

    # Join the parts into a single string
    duration_string = " ".join(duration_parts) if len(duration_parts) else '-'

    return duration_string

# Example usage:
d1 = datetime(2023, 1, 1, 5, 0, 0)
d2 = datetime(2023, 1, 1, 5, 0, 0)

result = calculate_duration(d1, d2)
# print(result)

# import pandas as pd

# # Create a sample DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35],
#         'City': ['New York', 'San Francisco', 'Los Angeles']}

# df = pd.DataFrame(data)


# for item in range(20):
#     for key in data:
#         data[key].append(f'Item {key} {item}')






# import re

# def convert_to_megabytes(value, unit):
#     unit_multiplier = {'K': 1 / 1024, 'M': 1, 'G': 1024}
#     return float(value) * unit_multiplier.get(unit.upper(), 1)

# text = "set firewall policer ACL24010002_m60mber-Labadie_FNA if-exceeding bandwidth-limit 60m"

# # Define a regular expression pattern to match the bandwidth-limit value and optional unit
# pattern = r'bandwidth-limit\s+(\d+)([KMG]?)?'

# # Use re.search to find the match in the text
# match = re.search(pattern, text)

# # Extract the value and unit if a match is found
# if match:
#     value, unit = match.groups()
#     print("value-->", value)
#     print("unit-->", unit)
#     converted_value = convert_to_megabytes(value, unit)
#     print("Bandwidth Limit:", converted_value, "MB")
# else:
#     print("Bandwidth Limit not found in the text.")
age = 50
# data = [
#     {'name' : 'Mahbub','age' : ''},
#     {'name' : 'saif','age' : ''},
#     {'name' : 'taqbir','age' : ''},
# ]

# for item in data:
#     item['age'] = age

# print(data)

# for _ in range(10):
#     print("_-->", _)

from datetime import datetime, timedelta, date
today = datetime.now().date()
exception_month = datetime.strptime('2024-03-04','%Y-%m-%d').date()

if today.day == 4 and today != exception_month:
    print("today-->", today)
else:
    print("else-->", today)


import html

raw_text = f"""commit \r\n[edit logical-systems BDIX-RT firewall policer M/S-Blueberry-Online-BDIX-BW]\r\n 'if-exceeding'\r\n Missing mandatory statement: 'burst-size-limit'\r\nerror: commit failed: (missing mandatory statements)\r\n\r\n[edit]\r\ndevOps@Uttara-MX204-RT# exit configuration-mode \r\nThe configuration has been changed but not committed\r\nExiting configuration mode\r\n\r\ndevOps@Uttara-MX204-RT> exit"""

sanitized_text = raw_text.replace(r'\r','').replace(r'\n', '<br/>')
print("sanitized_text-->", sanitized_text)


    
