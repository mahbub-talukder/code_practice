from collections import defaultdict
from datetime import datetime,date,time, timedelta
import calendar
import time as _time
# from joblib import Parallel, delayed
# st_date =  datetime.now()
# valid_from =  datetime.strptime('2023-05-24 10:21:04','%Y-%m-%d %H:%M:%S') 
# valid_to =  datetime.strptime('2023-06-23 23:59:59','%Y-%m-%d %H:%M:%S')
# total_days =  abs((valid_from.date() - valid_to.date()).days) + 1
# print("total_days-->",total_days)


# st_date =  datetime.now()
# valid_from =  datetime.strptime('2023-05-24','%Y-%m-%d') 
# valid_to =  datetime.strptime('2023-06-23','%Y-%m-%d')
# total_days =  abs((valid_to.date() - valid_from.date()).days) + 1
# print("total_days-->",total_days)

# st_date =  datetime.now()
# valid_from =  datetime.strptime('2023-05-24','%Y-%m-%d') 
# valid_to =  datetime.strptime('2023-06-23','%Y-%m-%d')
# total_days =  abs((valid_to.date() - valid_from.date()).days) + 1
# consumed_days =  abs((st_date.date() - valid_from.date()).days)
# print("total_days-->",total_days)
# print("consumed days-->",consumed_days)




# year:str = str(datetime.now().year)[2:]
# month:str = "{:02d}".format(datetime.now().month) 
# count:int = 6
# count_with_padding:str = "{:04d}".format(count)
# print('year-->',year)
# print('month-->',month)
# print('count-->',count_with_padding)

# username = 'MT' +  year+month+count_with_padding
# print('username-->',username)


# from csv import DictWriter,DictReader
# # for importing
# final_array = []
# with open('package.csv', mode='r') as infile:
#     csv_file = DictReader(infile)
#     for row in csv_file:
#         final_array.append(dict(row))
        
        
        
# print('final_array-->',final_array[:1])
   

# # for exporting
# heading =  tuple(item for item in final_array[0])

# print('heading-->',heading)

# with open('spreadsheet.csv','w') as outfile:
#     writer = DictWriter(outfile, heading)
#     writer.writeheader()
#     writer.writerows(final_array)

# def get_month_end_date(date_parameter=None,return_format:str='str'):
    
#     if date_parameter and isinstance(date_parameter,date):
        
#         datetime_object = datetime.combine(date_parameter,time.min)
        
#     elif date_parameter and isinstance(date_parameter,str):

#         datetime_object = datetime.strptime(date_parameter,"%Y-%m-%d")
    
#     elif date_parameter and isinstance(date_parameter,datetime):

#         datetime_object = date_parameter

#     else:

#         datetime_object = datetime.now()
        
#     month_end_date = datetime_object.replace(day=calendar.monthrange(datetime_object.year, datetime_object.month)[1],hour=0,minute=0,second=0,microsecond=0)
#     if return_format == 'datetime':
#         return month_end_date
#     elif return_format == 'date':
#         return month_end_date.date()
#     else:
#         return month_end_date.strftime("%Y-%m-%d")

# today = datetime.today().date()

# result = get_month_end_date(today,'time')

# print('result->',result,'date_type->',type(result))

# duplicate_ids_array = "32,92,65,6,3,9".split(",")

# base_id =  duplicate_ids_array[0]
# remain_ids =  duplicate_ids_array[1:]
# if len(remain_ids)>1:
#     deleted_able_id = str(tuple(remain_ids))
# else:
#     deleted_able_id =  "(" + remain_ids[0] +")"

# print('base_id-->',base_id)
# print('deleted_id-->',deleted_able_id)

# people = [
# {'name': "Tom", 'age': 10},
# {'name': "Mark", 'age': 5},
# {'name': "Mark2", 'age': 5},
# {'name': "Pam", 'age': 7}
# ]
# age = 5
# result  = list(filter(lambda person: person['age'] == age, people))
# print(result)

# string= "01965493210"
# result = string.split(",")
# print('result-->',result)
# from collections import defaultdict
# old_list = [
#     {'name' : 'mahbub','mobile' : '210'},
#     {'name' : 'Atiq','mobile' : '350'},
#     {'name' : 'Shohan','mobile' : '210'},
#     {'name' : 'Malik','mobile' : '350'},
#     {'name' : 'Dabba','mobile' : '210'},
# ]

#  # group by mobile_primary
# groups = defaultdict(list)

# for obj in old_list:
#     groups[obj['mobile']].append(obj)

# new_list = groups.values()
# count= 0 
# count+=1
# print(count)
# print('new_list-->',list(new_list))

# did = []

# resutl = 'where ' + " and ".join(did)
# print(resutl)
# area = 'Mirpur - 14'
# area2 = 'Mirpur 14'
# area3 = 'Mirpur14'
# area4 = 'Mirpur    ,,--  14'

# new_area = area4.replace(" ","").replace("-","").replace(",","").lower list2
# group by mobile_primary

# # python group by 
data = [
    {'router' : 1 ,'interface' : 'ge-0/0/1'},
    {'router' : 2 ,'interface' : 'ge-0/0/2'},
    {'router' : 2 ,'interface' : 'ge-0/0/3'},
    {'router' : 1 ,'interface' : 'ge-0/0/4'},
    {'router' : 1 ,'interface' : 'ge-0/0/4'},
]

command_groups = {}

for obj in data:
    if obj['router'] in command_groups:
        command = [
            f"route_interface  : {obj['interface']}",
            f"route_interface  : {obj['interface']}",
            f"route_interface  : {obj['interface']}",
            f"route_interface  : {obj['interface']}",
        ]
        command_groups[obj['router']].extend(command)
    else:
         command_groups[obj['router']] = []

# group_by_result = []
# for block in  list(groups.values()):
#     obj = {
#         'username' : block[0]['reseller_username'],
#         'list' : block
#     }
#     group_by_result.append(obj)
for key in command_groups:

    print("\ngroup_by_result-->",command_groups[key])



  
# Python program to demonstrate
# overriding in multiple inheritance
  
  
# # Defining parent class 1
# class Parent1():
#     def first(self):
#         print("first show")

#     # Parent's show method
#     def show(self):
#         print("Inside Parent1 show")
          
# # Defining Parent class 2
# class Parent2(Parent1):
          
#     # Parent's show method
#     def display(self):
#         print("Inside Parent2")
        
#     def new(self):
#         self.check()

#     # def check(self):
#     #     print("check Inside parent")
          
# # Defining child class
# class Child(Parent2):
          
#     # Child's show method
#     def show(self):
#         # print("Inside Child")
#         super(Child,self).show()

#     def check(self):
#         print("check Inside Child")

     
        
# # Driver's code
# obj = Child()

# obj.new()
# do observe
# prnt = Parent2()
# prnt.new()
# obj.show()
# obj.display()

# prt2 = Parent2()
# prt2.show()


# parent_fullname = 'Mahbub'
# child_id = 'Koddor'
# child_fullname = 'Koddor'

# emailbody = """ 
#             Dear {parent_fullname},\n

#             We appreciate you for choosing our services. Your reference child account {child_id},{child_fullname} has been created successfully.

#             You can access your previous Receipts anywhere, anytime & recharge at your own convenience using http://myportal.mimebd.com.

#             We value your relationship with us and assure you our best services at all times.

#             Feel free to reach us if you find any problem.
#             Hotline: +8809609006463 & 16676 (24*7)

#             Regards,
#             TEAM MIME
#             """.format(parent_fullname=parent_fullname, child_id=child_id, child_fullname=child_fullname)
# print('emailbody',emailbody)

class Note:
    def __init__(self) -> None:
        self.data = None
        self.next = None


# from joblib import Parallel, delayed
# from math import sqrt
# def sqaure(number,ext):
#     print('ext: ', ext)
#     result = sqrt(number**2)
#     # print('result: ', result)
# start = _time.time()
# datse = 'sdflk'
# node = Note()
# Parallel(n_jobs=-1)(delayed(sqaure)(i,node) for i in range(10))
# # for i in range(10000000):
# #     sqaure(i)
# end = _time.time()
# delay = (end-start)
# print('delay: ', delay)

# def outer_function(x):
#     print('x: ', x)

#     inner_function(50)

#     def inner_function(y):
#         print( x + y)



# Using the outer function to create a new function
# outer_function(10)

