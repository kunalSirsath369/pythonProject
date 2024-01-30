email=input("Enter yiur email :")
k,j,d=0,0,0
if len(email)>=6:
  if email[0].isalpha():
    if ("@"in email) and (email.count("@")==1):
      if (email[-4]=='.') ^ (email[-3]=="."):
        for i in email:
          if i.isspace():
            k=1
          elif i.isalpha():
            if i==i.upper():
              j=1
          elif i.isdigit():
            continue
          elif i=="_" or i=="." or i=="@":
            continue
          else:
            d=1    

        if k==1 or j==1 or d==1:
          print("Unwanted space/carector/Uppercase")
        else:
          print("Email is valid")
      else:
        print('error: enter .com at end of email')  
    else:
      print("wrong Email: unwanted symbol")
  else:
    print("wrong Email: email should be in lower case")
else:
  print('wrong Email:lenth is less than 6')