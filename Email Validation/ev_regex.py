# email validaion using regex module
# conditions
# length > 6
# a-z
# 0-9
# . _ (1 at a time)
# @ ( 1 time)
# . position is second or third position from negative index

import re 
# ^ start letter [a_z] << range of alphabet
# + merge conitions
# \ search connector
# ? gives one connector or zero in the below condition
# \w search strings
# $ negative indexing

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# condition corresponing to the code
# first letter to be alphabet
# .. __ not allowed only single at a time
# a to z and 0 to 9 alphanumeric strings can be used
# @ can be used one time
# . to be palced at -2 and -3 index 
user_email = input("Enter your Email : ")

if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")
