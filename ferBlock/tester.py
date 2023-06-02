import requests
import json
serverUrl = "http://0.0.0.0:80"
nodeCounter = 42

def sendTransaction():
    sender = input("Enter the sender: ")
    recipient = input("Enter the recipient: ")
    amount = float(input("Enter the amount: "))
    transactionData = {'sender': sender,'recipient': recipient,'amount': amount}
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(serverUrl + "/transactions/new", data=json.dumps(transactionData), headers=headers)
        print(response.status_code)
        print (response.json())
    except:
        print("ERROR: Client failed to send transaction")
def mineBlock():
    try:
        response = requests.get(serverUrl + "/mine")
        print(response.text)
    except:
        print("ERROR: Failed to receive transaction")
        
def requestChain():
    try:
        response = requests.get(serverUrl + "/chain")
        print(response.text)
    except:
        print("ERROR: Failed to receive transaction")

def register():
    global nodeCounter
    numberOfNodes = int(input("Enter the number of nodes: "))
    nodesData = {'nodes': []}
    for i in range(numberOfNodes):
        node = "http://0.0.0.0:" + str(nodeCounter + i)
        nodesData['nodes'].append(node)
        print("Node created: ", node)
    nodeCounter += numberOfNodes
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(serverUrl + "/nodes/register", data=json.dumps(nodesData), headers=headers)
        print(response.status_code)
        print(response.json())
    except:
        print("ERROR: Failed to add nodes")

def resolve():
    try:
        response = requests.get(serverUrl + "/nodes/resolve")
        print(response.text)
    except:
        print("ERROR: Failed to resolve nodes")


if __name__ == '__main__':
    while True:
        print("1. New transaction")
        print("2. Mine")
        print("3. Chain")
        print("4. Register")
        print("5. Resolve")
        clientInput = input("Enter test value: ")
        if clientInput == "1":
            sendTransaction()
        elif clientInput == "2":
            mineBlock()
        elif clientInput == "3":
            requestChain()
        elif clientInput == "4":
            register()
        elif clientInput == "5":
            resolve()
        elif clientInput == "exit":
            print("Bye!")
            break
        else:
            print("Value not found")