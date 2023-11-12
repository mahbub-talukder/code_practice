from datetime import datetime 
import time


"""problem1:
"""

def timeConversion(s):
    # Write your code here
    
    return datetime.strptime(s,"%I:%M:%S%p").strftime("%H:%M:%S")


timeConversion("12:05:45AM")