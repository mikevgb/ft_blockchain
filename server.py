from flask import Flask, request, jsonify
from block import Blockchain

app = Flask(__name__)

transactionPool = []
myBlockchain = Blockchain()

@app.route('/addWorker', methods=['POST'])
def addWorker():
    workerName = request.data
    print ("Worker", workerName, "connected to the pool")
    return "Worker connected to server", 200

@app.route('/transactions/new', methods=['POST'])
def newTransaction():
    transData = request.data#.decode('utf-8')
    transactionPool.append(transData)
    print("Server receive block")
    return "received!", 200

@app.route('/mine', methods=['GET'])
def requestMineBlock():
    if len(transactionPool) > 0:
        print("last hash", myBlockchain.getLastHash())
        message = {'lastB': myBlockchain.getLastHash() if myBlockchain.getLastHash() else None, 'trans': transactionPool.pop()}
        return jsonify(message), 200
    else:
        return '', 204

@app.route('/chain', methods=['GET'])
def getChain():
    return "chain$$$", 200

@app.route('/minedBlock', methods=['POST'])
def minedBlock():
    minedBlock = request.data
    print("Worker mined block with hash", minedBlock)
    #add to the chain
    myBlockchain.add_block(minedBlock)
    #reward miner
    # print("Is blockchain valid? ", myBlockchain.is_chain_valid())
    return "\nYou mined and submited a block, congratz!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    
    