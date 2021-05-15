#!/usr/bin/env python
# coding: utf-8

# In[2]:


import speech_recognition as sr
import pyaudio as py 
import re # to search world from sentance
import smtplib as smt
sender=input(str("enter email address of sender :"))
reciver=input(str("enter email address of reciver :"))
pw=input(str("enter you password (make sure you have completed 2-step verification): "))
r=sr.Recognizer()
class voice: 
    with sr.Microphone() as source:
        print("speak text:")
        audio=r.listen(source)
        #print("done")
    try:
        text=r.recognize_google(audio)
        print("you said : {}".format(text))
    except sr.UnknownValueError:
        print("we could not get your voice")
    except sr.RequestError as e:
        print("request error is : {}".format(e))
def Email(sender_email,reciver_email,password):        
    server=smt.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,password)
    print("log in successful...")
    server.sendmail(sender_email,reciver_email,voice.text)
    print("email has been sent successfully to {}".format(reciver_email))
Email(sender,reciver,pw)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




