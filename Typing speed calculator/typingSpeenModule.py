from time import *
import random as r
def mistake(paratest,usertest):
  error=0
  for i in range(len(paratest)):
    try:
      if paratest[i] != usertest[i]:
        error=error+1
    except:
      error=error+1    
  return error
def speed_time(time_s,time_e,userinput):
  time_delay= time_e-time_s
  time_R=round(time_delay,2)
  speed=len(userinput)/time_R
  return round(speed)




text =["One key takeaway from Musk's speech is his advice to adopt a growth mindset","Musk encourages listeners to view setbacks as learning experiences"," He also highlights the value of perseverance, persistence, and taking risks","Elon Musk's word serves as an upbeat reminder that perseverance"," patience, and the desire to attempt things repeatedly in the face of difficulty are essential for success."]
test1=r.choice(text)
print('             *****Typing speeed calculator*****')
print(test1)
print()
print()
time_1=time()
testInput=input("Enter : ")
time_2=time()
print("speed :",speed_time(time_1,time_2,testInput),"WPS")
print("Error :",mistake(test1,testInput))
