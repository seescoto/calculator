#functions for calculator

###main entry point 
fieldText = ""
fieldDisplay =""
base = 10
basePrefix =""

def getBase():
   global base 
   return str(base)

def addEquationEnd(field, equation):  
   global fieldText, fieldDisplay 
   fieldDisplay += str(equation)
   fieldText += str(equation)
   #if neg number, 
   #delete prev content from field 
   field.delete("1.0", "end") #delete from start to end
   #put in new fieldText
   field.insert("1.0", fieldDisplay) 

def addEquationFront(field, equation):
   #used for negating an entire answer, etc. 
   #ONLY IF THERES SOMETHING IN THE TEXT ALREADY
   global fieldText, fieldDisplay
   if len(fieldDisplay) != 0:
      fieldDisplay = str(equation) + "(" + fieldDisplay + ")" 
      if equation == "-":
         #if negating, have it be n1 * (fieldText) where n = negative 1 
         fieldText = "n * (" + fieldText + ")"
      #replace content  
      field.delete("1.0", "end")
      field.insert("1.0", fieldDisplay)

def setBase(newBase):
   global base, basePrefix
   base = newBase 
   if base == 16:
      basePrefix = "0X"
   elif base == 2:
      basePrefix = "0b"

def equals(field):
   global fieldText, fieldDisplay 
   postText = toPostFix(fieldText)
   result = evalPostFix(postText)

   result = str(eval(fieldText))
   fieldText = "" 
   #replace equation text 
   field.delete("1.0", "end") 
   field.insert("1.0", result)


#press clear button 
def clear(field):
   global fieldText, fieldDisplay 
   fieldText = ""
   fieldDisplay = "" 
   field.delete("1.0", "end")


#convert infix to postfix
def toPostFix(text):
   postText = ""
   postStack = []

   #go left to right for input string
   for char in text:
      #if an operand (nums plus pi, e, n for negative, decimal point), add to postText straight away
      if char in "0123456789ABCDEF\u03C0en.":
         postText += char
      #if an operator
      elif char in "^/*-+":
         postText = checkPriority(char, postStack, postText)
      #if left parentheses, add to stack no matter what
      elif char == "(":
         postStack.append(char) 
      #else must be right parentheses
      else:
         #just add everything else from stack to expression until left parentheses
         while postStack and top(postStack) != "(":
            postText += " " + postStack.pop() + " "
         #now must be left parentheses
         if postStack: 
            postStack.pop()

   #add rest of stack to postText
   while postStack:
      postText += " " + postStack.pop()

   print (postText)
   return postText

def checkPriority(char, postStack, postText):
   #check the priority of the operator vs the top of the stack

   topIsParenth = top(postStack) == "(" #if top of stack is left parentheses

   #if lower priority or equal than top of stack, pop and repeat
   while postStack and not(topIsParenth) and (priority(char) <= priority(top(postStack))):
      postText += " " + postStack.pop() + " "

   #if nothing or "(" at top of stack OR has higher priority than top of stack, push 
   postText += " "
   postStack.append(char) 
   
   return postText

def priority(char):
   high = "*/^"
   low = "+-"
   if char not in (low+high):
      return -1
   return 2 if char in high else 1 

def top(arr):
   if arr:
      return arr[-1]
   return ""

def evalPostFix(fieldText):
   result = 0
   stack = [] 
   equation = fieldText.split() 

   try:
      for element in equation:
         if isNumber(element):
            stack.append(element)
         else:
            val1 = stack.pop() 
            val2 = stack.pop() 
            result = evaluate(val2, val1, element)
            stack.append(result) 
      return result  
   
   except:
      #if nothing in stack then will get error - bc postfix is incorrect
      print("SYNTAX ERROR") 

   

#returns if the string is a number in base hex, dec, or bin 
def isNumber(string):
   #number values - 0-9, A-F, pi, e, n for negative, decimal point
   numberVals = "0123456789ABCDEF\u03C0en."
   for char in string:
      if char not in numberVals:
         return False 
   return True

def evaluate(a, b, operator):
   #returns (a operator b)
   #switch statement in python is match arg case
   a, b = float(a), float(b)
   match operator:
      case "+":
         res = int(a) + b 
      case "-":
         res = a - b 
      case "*":
         res = a * b 
      case "/":
         res = a / b 
      case "^":
         res = a ** b 
      case default:
         res = None

   return res



def copyAns(field):
   pass


def getPrev(field):
   pass


equation = "(1+2)^3"
equation2 = equation.replace("^", "**")
txt = toPostFix(equation)
print(evalPostFix(txt), eval(equation), evalPostFix(txt) == eval(equation))

