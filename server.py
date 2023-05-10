from flask import Flask, request
from block import Blockchain

app = Flask(__name__)

transactionPool = []

@app.route('/addWorker', methods=['POST'])
def addWorker():
    workerName = request.data
    print ("Worker", workerName, "connected to the pool")
    return "Worker connected to server", 200

@app.route('/transactions/new', methods=['POST'])
def newTransaction():
    transData = request.data
    transactionPool.append(transData)
    response = "Server receive transaction " +  str(transData)
    print (response)
    return "received!", 200

@app.route('/mine', methods=['GET'])
def requestMineBlock():
    if len(transactionPool) > 0:
        return transactionPool.pop(), 200
    else:
        return '', 204

@app.route('/chain', methods=['GET'])
def getChain():
    return "chain$$$", 200

@app.route('/minedBlock', methods=['POST'])
def minedBlock():
    minedBlock = request.data
    print("Worker mined block with hash", minedBlock)
    #reward miner
    return "You mined and submited a block, congratz!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    myBlockchain = Blockchain()
    