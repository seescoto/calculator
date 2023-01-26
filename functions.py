#functions for calculator

###main entry point 
fieldText = ""
base = 10

def addEquationEnd(field, equation):  
   global fieldText 
   fieldText += str(equation)
   #delete prev content from field 
   field.delete("1.0", "end") #delete from start to end
   #put in new fieldText
   field.insert("1.0", fieldText) 

def addEquationFront(field, equation):
   #used for negating an entire answer, etc. 
   #ONLY IF THERES SOMETHING IN THE TEXT ALREADY
   global fieldText 
   if len(fieldText) != 0:
      fieldText = str(equation) + "(" + fieldText + ")" 
      #replace content  
      field.insert("1.0", fieldText)

#press equal button
def calculate(field):
   global fieldText 
   result = str(eval(fieldText)) 
   #replace equation text 
   field.delete("1.0", "end") 
   field.insert("1.0", result)

#press clear button 
def clear(field):
   global fieldText 
   fieldText = "" 
   field.delete("1.0", "end")

def setBase(newBase):
   global base 
   base = newBase 


def copyAns(field):
   pass

def openHelpPage():
   pass