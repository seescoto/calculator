###graphical user interface of calculator 

import tkinter as tk
from calcFunctions import *  #math stuff
from miscFunctions import *  #ui stuff - help page, clear warning, etc.

padwidth = 5
padheight = 5  
buttonwidth = 10 
buttonheight = 10

#creating calculator


#window for where field text will show up 
window = tk.Tk() 
window.title("Calculator")

field = tk.Text(window, height = 5)
field.grid(row = 1, column = 0, columnspan = 6)
baseLabel = tk.Label(text="BASE " + getBase())
baseLabel.grid(column=0, row=0)

def showBase():
   baseLabel.config(text = "BASE " + getBase())
baseLabel = tk.Label(text="BASE " + getBase())
baseLabel.grid(column=0, row=0)


#number buttons 
#
#0, ., (-)
button0 = tk.Button(window, text = "0", command = lambda: addEquationEnd(field, 0), width = buttonwidth)
button0.grid(row = 7, column = 3, padx = padwidth, pady = padheight)

buttonDot = tk.Button(window, text = ".", command = lambda: addEquationEnd(field, "."), width = buttonwidth)
buttonDot.grid(row = 7, column = 4, padx = padwidth, pady = padheight)

buttonNeg = tk.Button(window, text = "( - )", command = lambda: addEquationFront(field, "-"), width = buttonwidth)
buttonNeg.grid(row = 7, column = 5, padx = padwidth, pady = padheight)
#

#
#1, 2, 3
button1 = tk.Button(window, text = "1", command = lambda: addEquationEnd(field, 1), width = buttonwidth)
button1.grid(row = 6, column = 3, padx = padwidth, pady = padheight)

button2 = tk.Button(window, text = "2", command = lambda: addEquationEnd(field, 2), width = buttonwidth)
button2.grid(row = 6, column = 4, padx = padwidth, pady = padheight)

button3 = tk.Button(window, text = "3", command = lambda: addEquationEnd(field, 3), width = buttonwidth)
button3.grid(row = 6, column = 5, padx = padwidth, pady = padheight)
#

#
#4, 5 ,6
button4 = tk.Button(window, text = "4", command = lambda: addEquationEnd(field, 4), width = buttonwidth)
button4.grid(row = 5, column = 3, padx = padwidth, pady = padheight)

button5 = tk.Button(window, text = "5", command = lambda: addEquationEnd(field, 5), width = buttonwidth)
button5.grid(row = 5, column = 4, padx = padwidth, pady = padheight)

button6 = tk.Button(window, text = "6", command = lambda: addEquationEnd(field, 6), width = buttonwidth)
button6.grid(row = 5, column = 5, padx = padwidth, pady = padheight)
#

#
#7, 8, 9
button7 = tk.Button(window, text = "7", command = lambda: addEquationEnd(field, 7), width = buttonwidth)
button7.grid(row = 4, column = 3, padx = padwidth, pady = padheight)

button8 = tk.Button(window, text = "8", command = lambda: addEquationEnd(field, 8), width = buttonwidth)
button8.grid(row = 4, column = 4, padx = padwidth, pady = padheight)

button9 = tk.Button(window, text = "9", command = lambda: addEquationEnd(field, 9), width = buttonwidth)
button9.grid(row = 4, column = 5, padx = padwidth, pady = padheight)
#

#
#A, B, C
buttonA = tk.Button(window, text = "A", command = lambda: addEquationEnd(field, "A"), width = buttonwidth)
buttonA.grid(row = 3, column = 3, padx = padwidth, pady = padheight)

buttonB = tk.Button(window, text = "B", command = lambda: addEquationEnd(field, "B"), width = buttonwidth)
buttonB.grid(row = 3, column = 4, padx = padwidth, pady = padheight)

buttonC = tk.Button(window, text = "C", command = lambda: addEquationEnd(field, "C"), width = buttonwidth)
buttonC.grid(row = 3, column = 5, padx = padwidth, pady = padheight)
#

#
#D, E, F
buttonD = tk.Button(window, text = "D", command = lambda: addEquationEnd(field, "D"), width = buttonwidth)
buttonD.grid(row = 2, column = 3, padx = padwidth, pady = padheight)

buttonE = tk.Button(window, text = "E", command = lambda: addEquationEnd(field, "E"), width = buttonwidth)
buttonE.grid(row = 2, column = 4, padx = padwidth, pady = padheight)

buttonF = tk.Button(window, text = "F", command = lambda: addEquationEnd(field, "F"), width = buttonwidth)
buttonF.grid(row = 2, column = 5, padx = padwidth, pady = padheight)
#



#basic calc function buttons 
#clear, /, *, -, +, =
buttonClear = tk.Button(window, text = "clear", command = lambda: clear(field), width = buttonwidth)
buttonClear.grid(row = 2, column = 6, padx = padwidth, pady = padheight)

buttonDiv = tk.Button(window, text = "/", command = lambda: addEquationEnd(field, "/"), width = buttonwidth)
buttonDiv.grid(row = 3, column = 6, padx = padwidth, pady = padheight)

buttonMult = tk.Button(window, text = "*", command = lambda: addEquationEnd(field, "*"), width = buttonwidth)
buttonMult.grid(row = 4, column = 6, padx = padwidth, pady = padheight)

buttonSub = tk.Button(window, text = "-", command = lambda: addEquationEnd(field, "-"), width = buttonwidth)
buttonSub.grid(row = 5, column = 6, padx = padwidth, pady = padheight)

buttonAdd = tk.Button(window, text = "+", command = lambda: addEquationEnd(field, "+"), width = buttonwidth)
buttonAdd.grid(row = 6, column = 6, padx = padwidth, pady = padheight)

buttonEqual = tk.Button(window, text = "=", command = lambda: equals(field), width = buttonwidth)
buttonEqual.grid(row = 7, column = 6, padx = padwidth, pady = padheight)


#col 2 buttons
#setting base, parentheses, power
buttonSetHex = tk.Button(window, text = "HEX", command = lambda: [setBase(16), showBase()], width = buttonwidth)
buttonSetHex.grid(row = 2, column = 2, padx = padwidth, pady = padheight)

buttonSetDec = tk.Button(window, text = "DEC", command = lambda: [setBase(10), showBase()], width = buttonwidth)
buttonSetDec.grid(row = 3, column = 2, padx = padwidth, pady = padheight)

buttonSetBin = tk.Button(window, text = "BIN", command = lambda: [setBase(2), showBase()], width = buttonwidth)
buttonSetBin.grid(row = 4, column = 2, padx = padwidth, pady = padheight)

buttonPar1 = tk.Button(window, text = "(", command = lambda: addEquationEnd(field, "("), width = buttonwidth)
buttonPar1.grid(row = 5, column = 2, padx = padwidth, pady = padheight)

buttonPar2 = tk.Button(window, text = ")", command = lambda: addEquationEnd(field, ")"), width = buttonwidth)
buttonPar2.grid(row = 6, column = 2, padx = padwidth, pady = padheight)

buttonPower = tk.Button(window, text = "^", command = lambda: addEquationEnd(field, "^"), width = buttonwidth)
buttonPower.grid(row = 7, column = 2, padx = padwidth, pady = padheight)


#col3 buttons 
#help, copy ans, pi, e, log, sqrt
buttonHelp = tk.Button(window, text = "Help!", command = lambda: openHelpPage(window), width = buttonwidth)
buttonHelp.grid(row = 2, column = 1, padx = padwidth, pady = padheight)

buttonAns = tk.Button(window, text = "ans", command = lambda: copyAns(field), width = buttonwidth)
buttonAns.grid(row = 3, column = 1, padx = padwidth, pady = padheight)

buttonPi = tk.Button(window, text = "\u03C0", command = lambda: addEquationEnd(field, "\u03C0"), width = buttonwidth)
buttonPi.grid(row = 4, column = 1, padx = padwidth, pady = padheight)

buttonPar1 = tk.Button(window, text = "e", command = lambda: addEquationEnd(field, "e"), width = buttonwidth)
buttonPar1.grid(row = 5, column = 1, padx = padwidth, pady = padheight)

buttonPar2 = tk.Button(window, text = "log", command = lambda: addEquationEnd(field, "log("), width = buttonwidth)
buttonPar2.grid(row = 6, column = 1, padx = padwidth, pady = padheight)

buttonPower = tk.Button(window, text = "\u221A", command = lambda: addEquationEnd(field, "\u221A"), width = buttonwidth)
buttonPower.grid(row = 7, column = 1, padx = padwidth, pady = padheight)


#always show window 
window.mainloop()


