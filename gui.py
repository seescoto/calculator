###graphical user interface of calculator 

import tkinter as tk
from calcFunctions import *  #math stuff
from miscFunctions import *  #ui stuff - help page, clear warning, etc.

padwidth = 5
padheight = 5  
buttonwidth = 10 
buttonheight = 10

#creating calculator

window = tk.Tk() 
window.title("Calculator")

#windows for where equation and answer text will show up 
eqField = tk.Text(window, height = 5, width = 50)
eqField.grid(row = 1, columnspan = 4)
ansField = tk.Text(window, height = 5, width = 10)
ansField.grid(row = 1, column = 4, columnspan = 1)

baseLabel = tk.Label(text="BASE " + getBase())
baseLabel.grid(row=0, column = 0) 
numTypeLabel = tk.Label(text = "works for values in " + getSet())
numTypeLabel.grid(row = 0, column = 2, columnspan = 2)

 
#reminds user of what base they're in 
def showBase():
   baseLabel.config(text = "BASE " + getBase())
   numTypeLabel.config(text="works for values in " + getSet())
baseLabel.grid(column=0, row=0)



#number buttons 
#0, ., (-)
button0 = tk.Button(window, text = "0", command = lambda: addEquation(eqField, 0), width = buttonwidth)
button0.grid(row = 8, column = 1, padx = padwidth, pady = padheight)


buttonDot = tk.Button(window, text = ".", command = lambda: addEquation(eqField, "."), width = buttonwidth)
buttonDot.grid(row = 8, column = 2, padx = padwidth, pady = padheight)


buttonNeg = tk.Button(window, text = "( - )", command = lambda: addEquation(eqField, "n1*"), width = buttonwidth)
buttonNeg.grid(row = 8, column = 3, padx = padwidth, pady = padheight)

#1, 2, 3
button1 = tk.Button(window, text = "1", command = lambda: addEquation(eqField, 1), width = buttonwidth)
button1.grid(row = 7, column = 1, padx = padwidth, pady = padheight)

button2 = tk.Button(window, text = "2", command = lambda: addEquation(eqField, 2), width = buttonwidth)
button2.grid(row = 7, column = 2, padx = padwidth, pady = padheight)

button3 = tk.Button(window, text = "3", command = lambda: addEquation(eqField, 3), width = buttonwidth)
button3.grid(row = 7, column = 3, padx = padwidth, pady = padheight)

#4, 5 ,6
button4 = tk.Button(window, text = "4", command = lambda: addEquation(eqField, 4), width = buttonwidth)
button4.grid(row = 6, column = 1, padx = padwidth, pady = padheight)

button5 = tk.Button(window, text = "5", command = lambda: addEquation(eqField, 5), width = buttonwidth)
button5.grid(row = 6, column = 2, padx = padwidth, pady = padheight)

button6 = tk.Button(window, text = "6", command = lambda: addEquation(eqField, 6), width = buttonwidth)
button6.grid(row = 6, column = 3, padx = padwidth, pady = padheight)

#7, 8, 9
button7 = tk.Button(window, text = "7", command = lambda: addEquation(eqField, 7), width = buttonwidth)
button7.grid(row = 5, column = 1, padx = padwidth, pady = padheight)

button8 = tk.Button(window, text = "8", command = lambda: addEquation(eqField, 8), width = buttonwidth)
button8.grid(row = 5, column = 2, padx = padwidth, pady = padheight)

button9 = tk.Button(window, text = "9", command = lambda: addEquation(eqField, 9), width = buttonwidth)
button9.grid(row = 5, column = 3, padx = padwidth, pady = padheight)

#A, B, C
buttonA = tk.Button(window, text = "A", command = lambda: addEquation(eqField, "A"), width = buttonwidth)
buttonA.grid(row = 4, column = 1, padx = padwidth, pady = padheight)

buttonB = tk.Button(window, text = "B", command = lambda: addEquation(eqField, "B"), width = buttonwidth)
buttonB.grid(row = 4, column = 2, padx = padwidth, pady = padheight)

buttonC = tk.Button(window, text = "C", command = lambda: addEquation(eqField, "C"), width = buttonwidth)
buttonC.grid(row = 4, column = 3, padx = padwidth, pady = padheight)

#D, E, F
buttonD = tk.Button(window, text = "D", command = lambda: addEquation(eqField, "D"), width = buttonwidth)
buttonD.grid(row = 3, column = 1, padx = padwidth, pady = padheight)

buttonE = tk.Button(window, text = "E", command = lambda: addEquation(eqField, "E"), width = buttonwidth)
buttonE.grid(row = 3, column = 2, padx = padwidth, pady = padheight)

buttonF = tk.Button(window, text = "F", command = lambda: addEquation(eqField, "F"), width = buttonwidth)
buttonF.grid(row = 3, column = 3, padx = padwidth, pady = padheight)


#basic calc function buttons (col 4)
#clear, ^, /, *, -, +, =
buttonClear = tk.Button(window, text = "clear", command = lambda: clear(eqField), width = buttonwidth)
buttonClear.grid(row = 2, column = 4, padx = padwidth, pady = padheight)
#if double clicked, clears all 
buttonClear.bind('<Double-1>', func = lambda x: clearAll(window))

buttonPower = tk.Button(window, text = "^", command = lambda: addEquation(eqField, "^"), width = buttonwidth)
buttonPower.grid(row = 3, column = 4, padx = padwidth, pady = padheight)

buttonDiv = tk.Button(window, text = "/", command = lambda: addEquation(eqField, "/"), width = buttonwidth)
buttonDiv.grid(row = 4, column = 4, padx = padwidth, pady = padheight)

buttonMult = tk.Button(window, text = "*", command = lambda: addEquation(eqField, "*"), width = buttonwidth)
buttonMult.grid(row = 5, column = 4, padx = padwidth, pady = padheight)

buttonSub = tk.Button(window, text = "-", command = lambda: addEquation(eqField, "-"), width = buttonwidth)
buttonSub.grid(row = 6, column = 4, padx = padwidth, pady = padheight)

buttonAdd = tk.Button(window, text = "+", command = lambda: addEquation(eqField, "+"), width = buttonwidth)
buttonAdd.grid(row = 7, column = 4, padx = padwidth, pady = padheight)

buttonEqual = tk.Button(window, text = "=", command = lambda: equals(ansField), width = buttonwidth)
buttonEqual.grid(row = 8, column = 4, padx = padwidth, pady = padheight)


#row 2 buttons, right beneath text box
#prev, ans, (, ), clear(already done, no need to repeat)
buttonPrev = tk.Button(window, text = "prev", command = lambda : getPrev(eqField, ansField), width = buttonwidth)
buttonPrev.grid(row = 2, column = 0, padx = padwidth, pady = padheight)

buttonAns = tk.Button(window, text = "ans", command = lambda: copyAns(eqField), width = buttonwidth)
buttonAns.grid(row = 2, column = 1, padx = padwidth, pady = padheight)

buttonPar1 = tk.Button(window, text = "(", command = lambda: addEquation(eqField, "("), width = buttonwidth)
buttonPar1.grid(row = 2, column = 2, padx = padwidth, pady = padheight)

buttonPar2 = tk.Button(window, text = ")", command = lambda: addEquation(eqField, ")"), width = buttonwidth)
buttonPar2.grid(row = 2, column = 3, padx = padwidth, pady = padheight)


#col1 buttons
#hex, dec, bin, help!, pi, e
#last 3
buttonPi = tk.Button(window, text = "\u03C0", command = lambda: addEquation(eqField, "p"), width = buttonwidth)
buttonPi.grid(row = 7, column = 0, padx = padwidth, pady = padheight)

buttonEuler = tk.Button(window, text = "e", command = lambda: addEquation(eqField, "e"), width = buttonwidth)
buttonEuler.grid(row = 8, column = 0, padx = padwidth, pady = padheight)

buttonHelp = tk.Button(window, text = "Help?", command = lambda: openHelpPage(window), width = buttonwidth)
buttonHelp.grid(row = 6, column = 0, padx = padwidth, pady = padheight)

#number buttons for disabling/enabling according to base
numButtons = [button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, 
              buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, buttonDot, buttonEuler, buttonPi]
disable(base, numButtons)
#first 3
buttonSetHex = tk.Button(window, text = "HEX", command = lambda: [setBase(16, eqField, ansField), showBase(), disable(16, numButtons)], width = buttonwidth)
buttonSetHex.grid(row = 3, column = 0, padx = padwidth, pady = padheight)

buttonSetDec = tk.Button(window, text = "DEC", command = lambda: [setBase(10, eqField, ansField), showBase(), disable(10, numButtons)], width = buttonwidth)
buttonSetDec.grid(row = 4, column = 0, padx = padwidth, pady = padheight)

buttonSetBin = tk.Button(window, text = "BIN", command = lambda: [setBase(2, eqField, ansField), showBase(), disable(2, numButtons)], width = buttonwidth)
buttonSetBin.grid(row = 5, column = 0, padx = padwidth, pady = padheight)






#always show window 
window.mainloop()


