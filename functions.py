#functions for calculator

###main entry point 
fieldText = ""
fieldDisplay =""
base = 10
basePrefix =""

def addEquationEnd(field, equation):  
   global fieldText, fieldDisplay 
   fieldDisplay += str(equation)
   #if neg number, 
   #delete prev content from field 
   field.delete("1.0", "end") #delete from start to end
   #put in new fieldText
   field.insert("1.0", fieldDisplay) 

def addEquationFront(field, equation):
   #used for negating an entire answer, etc. 
   #ONLY IF THERES SOMETHING IN THE TEXT ALREADY
   global fieldText 
   if len(fieldText) != 0:
      fieldText = str(equation) + "(" + fieldText + ")" 
      #replace content  
      field.delete("1.0", "end")
      field.insert("1.0", fieldText)

def setBase(newBase):
   global base, basePrefix
   base = newBase 
   if base == 16:
      basePrefix = "0X"
   elif base == 2:
      basePrefix = "0b"

def equals(field):
   global fieldText 
   postText = toPostFix(fieldText)



   result = str(eval(fieldText)) 
   #replace equation text 
   field.delete("1.0", "end") 
   field.insert("1.0", result)

#press clear button 
def clear(field):
   global fieldText 
   fieldText = "" 
   field.delete("1.0", "end")

def toPostFix(text):
   postText = ""
   postStack = []

   #go left to right for input string
   for char in text:
      #if an operand (nums plus pi and e), add to postText straight away
      if char in "0123456789ABCDEF\u03C0e":
         postText += char + " "
      #if an operator (l for log, sqrt, n for negative)
      elif char in "^/*-+l\u221An":
         checkPriority(char, postStack)
      #if left parentheses, add to stack no matter what
      elif char == "(":
         postStack.append(char) 
      #else must be right parentheses
      else:
         #just add everything else from stack to expression
         while postStack and top(postStack) != "(":
            postText += postStack.pop() + " "
         #now must be left parentheses, if not raise error, if it is pop (
         if top(postStack) != "(":
            raise SyntaxError
         postStack.pop()
   #now just add rest of stack to postText
   while postStack:
      postText += postStack.pop() + " "

   return postText
            


def checkPriority(char, postStack):
   #check the priority of the operator vs the top of the stack
   pass 


def top(list):
   return list[-1]

def copyAns(field):
   pass

def openHelpPage():
   pass