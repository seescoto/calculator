#functions for calculator

import math
import CalculatorMicroservice.MicroserviceClient as client

###main entry point 
fieldText = ""
base = 10
set = '\u221D'
ans = ""
eVal = math.e 
piVal = math.pi

def getBase():
   #returns current base system
   global base 
   return str(base)

def getSet():
   #returns the set of numbers available per base
   global base 
   if base == 10: #set of real numbers
      return '\u211D'
   else: #set of integers
      return '\u2124'

def toDisplay(equation):
   #equation given to functions converted to what displays on the calculator
   #n1* becomes a negative sign, p becomes unicode symbol for pi
   equation = str(equation.replace("n1*", "-"))
   equation = equation.replace("p", "\u03C0")

   return equation

def addEquation(field, equation):  
   #add charactors to end of equation and update display
   global fieldText
   
   fieldText += str(equation)

   #delete prev content from field then insert new
   field.delete("1.0", "end") 
   field.insert("1.0", toDisplay(fieldText)) #display equation

def setBase(newBase, field = None, ansField = None):
   global base, fieldText, ans
   
   #change current equation/answer to this base and update display
   fieldText = convertEquation(fieldText, newBase)

   #change display fields
   if field:
      field.delete("1.0","end") 
      field.insert("1.0", toDisplay(fieldText)) 

   if ans:
      ans = convertTo(ans, base, newBase)

      ansField.delete("1.0", "end")
      ansField.insert("1.0", toDisplay(ans))

   #set new base
   base = newBase 

def equals(ansField):
   #evaluates equation and outputs answer
   global fieldText, ans, base 

   postText = toPostFix(fieldText)
   ans = evalPostFix(postText)

   #send equation and result to client - always as base 10 
   client.send(convertEquation(fieldText, 10))
   client.send(convertTo(ans, base, 10))

   #replace equation text 
   fieldText = ""
   ansField.delete("1.0", "end") 
   ansField.insert("1.0", str(ans))   

def clear(field):
   #clears equation from calculator
   global fieldText

   fieldText = ""
   field.delete("1.0", "end")

def toPostFix(text):
   #convert infix to postfix
   postText = ""
   postStack = []

   for char in text:
      #if an operand add to postText straight away
      if isNumber(char):
         postText += char
      #if an operator check priority and push/pop stack
      elif char in "^/*-+":
         postText = checkPriority(char, postStack, postText)
      #if left parentheses, push to stack no matter what
      elif char == "(":
         postStack.append(char) 
      #else must be right parentheses, pop until we get left parentheses
      else:
         while postStack and top(postStack) != "(":
            postText += " " + postStack.pop() + " "
         if postStack: 
            postStack.pop()

   #add rest of stack to postText
   while postStack:
      postText += " " + postStack.pop()

   return postText

def checkPriority(char, postStack, postText):
   #check the priority of the operator vs the top of the stack and push/pop as necessary

   topIsParenth = (top(postStack) == "(") 
   leqPriority = (priority(char) <= priority(top(postStack)))

   #if lower priority or equal to top of stack, pop and repeat
   while postStack and not(topIsParenth) and leqPriority:
      postText += " " + postStack.pop() + " "

   #else nothing or "(" at top of stack OR has higher priority than top of stack so push 
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
   #returns last element in array
   if arr:
      return arr[-1]
   return ""

def evalPostFix(fieldText):
   global base

   result = 0
   stack = [] 
   equation = fieldText.split() 

   try:
      for element in equation:
         if isNumber(element):
            element = toStandardNumber(element) 
            element = convertTo(element, base, 10)
            stack.append(element)
         else: #is an operator
            val1 = stack.pop() 
            val2 = stack.pop() 
            stack.append(evaluate(val2, val1, element))

      result = stack.pop()

      #if result is whole number, return int
      if int(float(result)) == result:
         result = int(result)

      return convertTo(result, 10, base)  
   
   except:
      #if nothing in stack then will get error - equation/postfix is incorrect
      print("SYNTAX ERROR - Equation invalid.") 

#returns if the string is a number in base hex, dec, or bin 
def isNumber(string):
   #numeric characters = nums plus pi, e, n for negative, decimal point
   numChars = "0123456789ABCDEFpen."

   for char in string:
      if char not in numChars:
         return False 
   return True

#returns a standard number instead of a string 
def toStandardNumber(string):
   result = string

   #if e 
   if "e" in string:
      result = result.replace("e", str(math.e))
      result = toStandardNumber(result) #run it again so if its negative itll still work
   #if pi
   elif "p" in string:
      result = result.replace("p", str(math.pi))
      result = toStandardNumber(result)
   #if it's negative (like n1*10 means -10)
   elif string[0] == "n":
      result = result.replace("n", "-")
   
   return result

#returns a operator b (ex. evaluate(1,2,"+") = 1+2= 3)
def evaluate(a, b, operator):
   #returns (a operator b)
   #switch statement in python is match arg case
   a, b = float(a), float(b)
   match operator:
      case "+":
         res = a + b 
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

#to a string representation of a number - -x -> n1*x for all x > 0
def toNumString(number):

   number = number.replace("n1*", "-") #distinguish negative values
   number = number.replace("\u03c0", "p") #replace pi symbol w/ p

   return str(number)

def getPrev(eqField, ansField):
   global fieldText, ans
   
   #get prev equation and answer
   newEq, newAns = client.get()

   if newEq == "empty":
      newEq = ""
   if newAns == "empty":
      newAns = ""

   #equation and answer are in base 10 - convert to current base
   fieldText = convertEquation(newEq, base)
   ans = toNumString(convertTo(newAns, 10, base)) 

   eqField.delete("1.0", "end") #delete from start to end
   eqField.insert("1.0", toDisplay(fieldText))
   ansField.delete("1.0", "end")
   ansField.insert("1.0", toDisplay(ans))
   
def copyAns(eqField):
   global ans, fieldText
   #copy answer from ansField to eqField
   
   fieldText = ans

   eqField.delete("1.0", "end") #delete from start to end
   eqField.insert("1.0", toDisplay(fieldText))

def convertEquation(equation, newBase):

   #if nothing in equation just return
   if len(equation) == 0:
      return ''

   #else edit using old equation as format
   newEq = ""
   oldBaseNum = ""

   for char in equation:
      if isNumber(char):
         oldBaseNum += char 
      else:
         #else then we're at an operator and the current number has ended, 
         #so convert and add to eq
         if oldBaseNum != "":
            newBaseNum = toStandardNumber(oldBaseNum)
            newBaseNum = toNumString(convertTo(newBaseNum, base, newBase))
            newEq += newBaseNum 
            oldBaseNum = ""
         
         #add operator char
         newEq += char 

   #convert last number in equation and add to newEq 
   newBaseNum = toStandardNumber(oldBaseNum)
   newBaseNum = toNumString(convertTo(newBaseNum, base, newBase))
   newEq += newBaseNum 

   return newEq

def convertTo(number, currBase, newBase):
   #convert all to decimal and then return based off newBase

   #if no need to convert, just return
   if currBase == newBase:
      return str(number)

   #if not in base 10, convert. if in base 10, floor to an int to keep values in Z
   if currBase != 10:
      number = int(number, currBase)
   else:
      number = int(float(number))

   #convert
   if newBase == 2: #binary
      number = str(bin(number))
      number = number.replace("0b", "") #get rid of prefix
      number = number.upper()
   elif newBase == 16: #hexadecimal
      number = str(hex(number))
      number = number.replace("0x", "")
      number = number.upper()

   return str(number)

base = 16 
newBase = 10 
eq="5+F"
print(convertEquation(eq, newBase))