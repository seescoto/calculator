#functions for clear/help buttons 
import tkinter as tk


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
   buttonYes = tk.Button(clearAllWindow, text = "Yes, delete all calculations", command = lambda: [clearAllSure(), clearAllWindow.destroy()])
   buttonYes.grid(pady=10) 
   buttonNo = tk.Button(clearAllWindow, text = "No, take me back", command = lambda: clearAllWindow.destroy())
   buttonNo.grid(pady=10) 

   clearAllWindow.mainloop()

def clearAllSure():
   pass

