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
   socket.recv()

def get():
   socket.send(b'POP')
   res = (socket.recv_json())
   eqDict = json.loads(res)
   return eqDict['equation'], eqDict['result']
