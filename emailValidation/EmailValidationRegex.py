# a-z
# 0-9
#._@ only simgle time use
# '.' position is after last 4 place
# email validation using regex

import re
user_email=input(" Enter your email :")
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$" 
if re.search(email_condition,user_email):
  print("Right email")
else:
  print("Wrong email")
  
  


