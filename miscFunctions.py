#functions for clear/help buttons 
import tkinter as tk


def openHelpPage(masterWindow):
   faqWindow = tk.Toplevel(masterWindow)
   faqWindow.title("FAQ")

   title = tk.Label(text = "FAQ about this calculator")
   title.pack()

   faqWindow.mainloop()

def clearAll(masterWindow):
   clearAllWindow = tk.Toplevel(masterWindow) 
   clearAllWindow.geometry("400x150")
   clearAllWindow.title("Are you sure?")

   lab = tk.Label(text = "Are you sure you'd like to delete all past calculations? This can't be undone.")
   lab.pack()
   buttonYes = tk.Button(clearAllWindow, text = "Yes, delete all calculations", command = lambda: clearAllSure())
   buttonYes.pack() 

   clearAllWindow.mainloop()

def clearAllSure():
   pass

