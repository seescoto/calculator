###graphical user interface of calculator 

import tkinter as tk

padwidth = 5 
padheight = 5 
buttonwidth = 10 
buttonheight = 10

#creating calculator




###main entry point 
fieldText = ""

def addEquationEnd(equation):  
   global fieldText 
   fieldText += str(equation)
   #delete prev content from field 
   field.delete("1.0", "end") #delete from start to end
   #put in new fieldText
   field.insert("1.0", fieldText) 

def addEquationFront(equation):
   #used for negating an entire answer, etc. 
   #ONLY IF THERES SOMETHING IN THE TEXT ALREADY
   global fieldText 
   if len(fieldText) != 0:
      fieldText = str(equation) + "(" + fieldText + ")" 
      #replace content 
      field.delete("1.0", "end") 
      field.insert("1.0", fieldText)

#press equal button
def calculate():
   global fieldText 
   result = str(eval(fieldText)) 
   #replace equation text 
   field.delete("1.0", "end") 
   field.insert("1.0", result)

#press clear button 
def clear():
   global fieldText 
   fieldText = "" 
   field.delete("1.0", "end")




#window for where field text will show up 
window = tk.Tk() 
field = tk.Text(window, height = 5, width = 30)
field.grid(row=1, column = 1, columnspan = 6)





#number buttons 

#
#0, ., (-)
button0 = tk.Button(window, text = "0", command = lambda: addEquationEnd(0), width = buttonwidth)
button0.grid(row = 6, column = 3, padx = padwidth, pady = padheight)

buttonDot = tk.Button(window, text = ".", command = lambda: addEquationEnd("."), width = buttonwidth)
buttonDot.grid(row = 6, column = 4, padx = padwidth, pady = padheight)

buttonNeg = tk.Button(window, text = "(-)", command = lambda: addEquationFront("-"), width = buttonwidth)
buttonNeg.grid(row = 6, column = 5, padx = padwidth, pady = padheight)
#

#
#1, 2, 3
button1 = tk.Button(window, text = "1", command = lambda: addEquationEnd(1), width = buttonwidth)
button1.grid(row = 5, column = 3, padx = padwidth, pady = padheight)

button2 = tk.Button(window, text = "2", command = lambda: addEquationEnd(2), width = buttonwidth)
button2.grid(row = 5, column = 4, padx = padwidth, pady = padheight)

button3 = tk.Button(window, text = "3", command = lambda: addEquationEnd(3), width = buttonwidth)
button3.grid(row = 5, column = 5, padx = padwidth, pady = padheight)
#

#
#4, 5 ,6
button4 = tk.Button(window, text = "4", command = lambda: addEquationEnd(4), width = buttonwidth)
button4.grid(row = 4, column = 3, padx = padwidth, pady = padheight)

button5 = tk.Button(window, text = "5", command = lambda: addEquationEnd(5), width = buttonwidth)
button5.grid(row = 4, column = 4, padx = padwidth, pady = padheight)

button6 = tk.Button(window, text = "6", command = lambda: addEquationEnd(6), width = buttonwidth)
button6.grid(row = 4, column = 5, padx = padwidth, pady = padheight)
#

#
#7, 8, 9
button7 = tk.Button(window, text = "7", command = lambda: addEquationEnd(7), width = buttonwidth)
button7.grid(row = 3, column = 3, padx = padwidth, pady = padheight)

button8 = tk.Button(window, text = "8", command = lambda: addEquationEnd(8), width = buttonwidth)
button8.grid(row = 3, column = 4, padx = padwidth, pady = padheight)

button9 = tk.Button(window, text = "9", command = lambda: addEquationEnd(9), width = buttonwidth)
button9.grid(row = 3, column = 5, padx = padwidth, pady = padheight)
#

#
#A, B, C
buttonA = tk.Button(window, text = "A", command = lambda: addEquationEnd("A"), width = buttonwidth)
buttonA.grid(row = 2, column = 3, padx = padwidth, pady = padheight)

buttonB = tk.Button(window, text = "B", command = lambda: addEquationEnd("B"), width = buttonwidth)
buttonB.grid(row = 2, column = 4, padx = padwidth, pady = padheight)

buttonC = tk.Button(window, text = "C", command = lambda: addEquationEnd("C"), width = buttonwidth)
buttonC.grid(row = 2, column = 5, padx = padwidth, pady = padheight)
#

#
#D, E, F
buttonD = tk.Button(window, text = "D", command = lambda: addEquationEnd("D"), width = buttonwidth)
buttonD.grid(row = 2, column = 3, padx = padwidth, pady = padheight)

buttonE = tk.Button(window, text = "E", command = lambda: addEquationEnd("E"), width = buttonwidth)
buttonE.grid(row = 2, column = 4, padx = padwidth, pady = padheight)

buttonF = tk.Button(window, text = "F", command = lambda: addEquationEnd("F"), width = buttonwidth)
buttonF.grid(row = 2, column = 5, padx = padwidth, pady = padheight)
#

#always show window 
window.mainloop()
