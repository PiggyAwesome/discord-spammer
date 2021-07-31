from tkinter import *
import time
import requests


messageContent = "" # The content of the message that should be spammed
channel = "" # The id of the channel that should be spammed in
tokens_directory = "" # Where to find tokens that should be spammed with


def do_request():
 with open(r"{tokens_directory}", "r") as a_file:
  for line in a_file:
    token = line.strip()
    print(token)
    response = requests.post(f"https://discord.com/api/v6//channels/{channel}/messages", headers={'authorization':f"{token}", 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.336'}, json={'content':messageContent})


tk = Tk()
tk.config(height = 20, width = 20)

def press():
    do_request()



clickthing =  Button(tk, text="SPAM!",  command=press,)
clickthing.config(height = 20, width = 20)
clickthing.grid(row = 0, column = 3, padx = 100)

clickthing.pack()
tk.mainloop()
