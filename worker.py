import requests
import time
from block import Block
serverUrl = "http://0.0.0.0:8000"

workerName = "workerName1"

try:
    response = requests.post(serverUrl + "/addWorker", data=workerName)
    print (response.text)
except:
    print("ERROR: Failed to connect")
    
while True:
    response = requests.get(serverUrl + "/mine")
    
    if response.status_code == 200:
        transData = response.text
        print("Worker receive transaction, starting mining...")
        print("Transdata =", transData)
        blockToMine = Block()
        block = blockToMine.mine_block(transData)
        if block:
            minedResponse = requests.post(serverUrl + "/minedBlock", data=block)
    if response.status_code == 204:
        time.sleep(5)