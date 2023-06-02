import requests
import time
import json
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
        if response.text:
            transData = response.json()
            print("Worker receive transaction, starting mining...")
            block = Block(transData['trans'], transData['lastB'])
            block.mine_block()
            calculated = str(block.getHash)
            # if block:
            minedResponse = requests.post(serverUrl + "/minedBlock", data=calculated)
            print("Hash send...", minedResponse.text)
    if response.status_code == 204:
        time.sleep(5)