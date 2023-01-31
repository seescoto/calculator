#functions for clear/help buttons 
import tkinter as tk

def openHelpPage(masterWindow):
   faqWindow = tk.Toplevel(masterWindow)
   faqWindow.title("FAQ")

   title = tk.Label(text = "FAQ about this calculator")
   title.pack()

   faqWindow.mainloop()

