#by audrie nielson from https://github.com/audrie-nielsen/CalculatorMicroservice

#   Connects REQ socket to tcp://localhost:5555
import zmq
context = zmq.Context()
import json  #translate json to python dictionary 

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


def send(string):
   socket.send(string.encode('ASCII')) 

def get():
   socket.send(b'POP')
   res = (socket.recv_json())
   eqDict = json.loads(res)
   return eqDict['equation'], eqDict['result']

'''
# Option 1: socket.send('[request]'.encode('ASCII'))
socket.send('16/4'.encode('ASCII'))
socket.recv()

# Option 2: socket.send((b"[request]")
socket.send(b"4.0")
socket.recv()

socket.send(b"3 + 6 / 2 - 9")
socket.recv()

socket.send('3'.encode('ASCII'))
socket.recv()

socket.send(b"POP")  # Send request "POP" to retrieve the last equation and result pushed
res = socket.recv_json() # Use socket.recv_json() to receive the equation and result as a JSON
print(res)

socket.send('POP'.encode('ASCII'))
res = socket.recv_json()
print(res)


#send equation and answer 
socket.send(b'15/2')
socket.recv()
socket.send(b'7.5') 
socket.recv()

#get last eqiation and answer 
socket.send(b'POP') 
res = (socket.recv_json())
eqDict = json.loads(res)
print(eqDict['equation'], " = ", eqDict['result'])
'''