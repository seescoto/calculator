#functions for clear/help buttons 
import tkinter as tk
import CalculatorMicroservice.MicroserviceClient as client

def openHelpPage(masterWindow):
   faqWindow = tk.Toplevel(masterWindow)
   faqWindow.title("FAQ")

   title = tk.Label(text = "FAQ about this calculator")
   title.pack()

   faqWindow.mainloop()

def clearAll(masterWindow):
   #new window above masterWindow, asks if you're sure you want to clear all, closes
   clearAllWindow = tk.Toplevel(masterWindow) 
   clearAllWindow.geometry("400x130")
   clearAllWindow.title("Are you sure?")

   lab = tk.Label(clearAllWindow, text = "Are you sure you'd like to delete all past calculations? This can't be undone.")
   lab.grid(row = 0, pady = 10)
   buttonYes = tk.Button(clearAllWindow, text = "Yes, delete all calculations", command = lambda: [showWait(clearAllWindow), clearAllSure(), clearAllWindow.destroy()])
   buttonYes.grid(pady=10) 
   buttonNo = tk.Button(clearAllWindow, text = "No, take me back", command = lambda: clearAllWindow.destroy())
   buttonNo.grid(pady=10) 

   clearAllWindow.mainloop()

def clearAllSure():
   #clear all from stack in microservice
   eq, ans = client.get() 
   while eq != 'empty' and eq != ans:
      eq, ans = client.get()

def showWait(window):

   lab = tk.Label(window, text = "Please wait...")
   lab.grid()

def disable(base, buttons):

   if base == 2:
      #binary, disable decimal point button and buttons 2-F + e and pi
      for i in range(2, len(buttons)):
         buttons[i]['state'] = 'disabled'
      #enable 0-1
      for i in range(0, 2):
         buttons[i]['state'] = 'active' 

   elif base == 10:
      #disable A-F (10 thru 15) but not e or pi
      for i in range(10, len(buttons)-2):
         buttons[i]['state'] = 'disabled' 
      #enable 0-9 and ALSO pi, e, decimal point
      abled = [b for b in range(0, 10)] + [b for b in range(len(buttons) -1, 16, -1)]
      for i in abled:
         buttons[i]['state'] = 'active'

   
   else:
      #hex, disable decimal point, pi, e
      for i in range(16, len(buttons)):
         buttons[i]['state'] = 'disabled'
      #enable all other buttons 0-F (0 thru 15)
      for i in range(0, 16):
         buttons[i]['state'] = 'active'