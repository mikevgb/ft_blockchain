import requests
from block import Block
import datetime

serverUrl = "http://0.0.0.0:8000"

def sendTransaction(transactionData):
    try:
        response = requests.post(serverUrl + "/transactions/new", data=transactionData)
        print (response.text)
    except:
        print("ERROR: Client failed to send transaction")

if __name__ == '__main__':
    while True:
        clientInput = input("Enter your transaction: ")
        if clientInput == "exit":
            print("Bye!")
            break
        else:
            newBlock = Block(1, datetime.datetime.now(), {clientInput}, "")
            print(newBlock)
            sendTransaction(newBlock)
        
