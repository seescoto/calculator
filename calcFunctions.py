#functions for calculator

import math
import CalculatorMicroservice.MicroserviceClient as client

###main entry point 
fieldText = ""
base = 10
basePrefix =""
ans = ""

def getBase():
   global base 
   return str(base)

def toDisplay(equation):
   #equation given to functions converted to what displays on the calc
   #n1* becomes a negative sign
   equation = equation.replace("n1*", "-")
   return equation

def addEquation(field, equation):  
   global fieldText
   
   fieldText += str(equation)

   #delete prev content from field 
   field.delete("1.0", "end") #delete from start to end
   field.insert("1.0", toDisplay(fieldText)) #display equation

def setBase(newBase):
   global base, basePrefix
   base = newBase 
   if base == 16:
      basePrefix = "0X"
   elif base == 2:
      basePrefix = "0b"

def equals(ansField):
   global fieldText, ans 
   postText = toPostFix(fieldText)
   ans = evalPostFix(postText)

   #send equation and result to client 
   client.send(fieldText)
   client.send(toNumString(ans))

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
            element = toStandardNumber(element)
            stack.append(element)
         else:
            val1 = stack.pop() 
            val2 = stack.pop() 
            stack.append(evaluate(val2, val1, element)) 

      result = stack.pop()

      #if result is whole number, return int
      if int(result) == result:
         result = int(result)

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

#returns a standard number instead of a string 
def toStandardNumber(string):
   result = string

   #if it's negative (like n10 means -10)
   if string[0] == "n":
      result = float(string[1:]) * -1 
   #if e 
   elif string == "e":
      result = math.e 
   #if pi
   elif string == "\u03C0":
      result = math.pi 
   
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


def copyAns(eqField):
   #copy answer from ansField to eqField
   global ans, fieldText
   #delete prev content from field 
   fieldText = toNumString(ans)

   eqField.delete("1.0", "end") #delete from start to end
   eqField.insert("1.0", toDisplay(fieldText))
   pass
   
#to a string representation of a number - -x -> n1*x for all x > 0
def toNumString(number):
   if float(number) < 0:
      number = "n1*"+str(abs(number))
   return str(number)

def getPrev(eqField, ansField):

   newEq, newAns = client.get()
   print(newEq, newAns)
   if newEq == "empty":
      newEq = ""
   if newAns == "empty":
      newAns = ""

   fieldText = newEq 
   ans = toNumString(newAns) 

   eqField.delete("1.0", "end") #delete from start to end
   eqField.insert("1.0", toDisplay(fieldText))

   ansField.delete("1.0", "end")
   ansField.insert("1.0", toDisplay(ans))
   




