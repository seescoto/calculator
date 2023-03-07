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
   global base 
   return str(base)

def getSet():
   global base 
   if base == 10: #set of real numbers
      return '\u211D'
   else: #set of integers
      return '\u2124'

def toDisplay(equation):
   #equation given to functions converted to what displays on the calc
   #n1* becomes a negative sign
   equation = str(equation.replace("n1*", "-"))
   equation = equation.replace("p", "\u03C0")
   return equation

def addEquation(field, equation):  
   global fieldText
   
   fieldText += str(equation)

   #delete prev content from field 
   field.delete("1.0", "end") #delete from start to end
   field.insert("1.0", toDisplay(fieldText)) #display equation

def setBase(newBase, field = None, ansField = None):
   global base, fieldText, ans

   
   #change current equation/answer to this base and update display
   fieldText = convertEquation(fieldText, newBase)

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
   global fieldText, ans, base 

   postText = toPostFix(fieldText)
   ans = evalPostFix(postText)

   #send equation and result to client - as base 10 always 
   client.send(convertEquation(fieldText, 10))
   client.send(convertTo(ans, base, 10))

   fieldText = ""

   #replace equation text 
   ansField.delete("1.0", "end") 
   ansField.insert("1.0", str(ans))   

#press clear button 
def clear(field):
   global fieldText
   fieldText = ""
   field.delete("1.0", "end")

#convert infix to postfix
def toPostFix(text):
   postText = ""
   postStack = []

   #go left to right for input string
   for char in text:
      #if an operand add to postText straight away
      if isNumber(char):
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

   return postText

def checkPriority(char, postStack, postText):
   #check the priority of the operator vs the top of the stack

   topIsParenth = top(postStack) == "(" #if top of stack is left parentheses

   #if lower priority or equal to top of stack, pop and repeat
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
   global base

   result = 0
   stack = [] 
   equation = fieldText.split() 

   try:
      for element in equation:
         if isNumber(element):
            if "e" not in element and "p" not in element:
               #if the number isnt e, -e, or pi, -pi which will already be in base 10, convert them
               element = toStandardNumber(element)
               element = convertTo(element, base, 10)
            else:
               element = toStandardNumber(element)
            stack.append(element)
         else:
            val1 = stack.pop() 
            val2 = stack.pop() 
            stack.append(evaluate(val2, val1, element)) 

      result = stack.pop()

      #if result is whole number, return int
      if int(float(result)) == result:
         result = int(result)

      return convertTo(result, 10, base)  
   
   except:
      #if nothing in stack then will get error - bc postfix is incorrect
      print("SYNTAX ERROR") 

#returns if the string is a number in base hex, dec, or bin 
def isNumber(string):
   #numeric characters = nums plus pi, e, n for negative, decimal point
   numChars = "0123456789ABCDEFpen.\u03c0"

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
   #if it's negative (like n10 means -10)
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

   number = number.replace("n1*", "-")
   number = number.replace("\u03c0", "p") #replace pi symbol

   return str(number)

def getPrev(eqField, ansField):
   global fieldText, ans
   
   newEq, newAns = client.get()
   if newEq == "empty":
      newEq = ""
   if newAns == "empty":
      newAns = ""

   #get equation and answer back from base 10 to current base
   fieldText = convertEquation(newEq, base)
   ans = toNumString(convertTo(newAns, 10, base)) 

   eqField.delete("1.0", "end") #delete from start to end
   eqField.insert("1.0", toDisplay(fieldText))
   ansField.delete("1.0", "end")
   ansField.insert("1.0", toDisplay(ans))
   
def copyAns(eqField):
   #copy answer from ansField to eqField
   global ans, fieldText
   #delete prev content from field 
   fieldText = toNumString(ans)

   eqField.delete("1.0", "end") #delete from start to end
   eqField.insert("1.0", toDisplay(fieldText))

def convertEquation(equation, newBase):

   if len(equation) == 0:
      return ''

   newEq = ""
   oldBaseNum = ""

   for char in equation:
      if isNumber(char):
         oldBaseNum += char 
      else:
         #else then we're at an operator and the current number has ended 
         #if not pi or e then convert - pi or e stay same representation in all bases
         if "e" in oldBaseNum or "pi" in oldBaseNum:
            newEq += oldBaseNum
         elif oldBaseNum != "":
            newBaseNum = toStandardNumber(oldBaseNum)
            newBaseNum = convertTo(newBaseNum, base, newBase)
            newBaseNum = toNumString(newBaseNum)
            newEq += newBaseNum 
         
         #add operator character
         newEq += char 

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

