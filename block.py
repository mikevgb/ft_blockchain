import hashlib
import datetime
import sys

INDEX = 0

class Block:
    def __init__(self, data, previous_hash, nonce=0):
        global INDEX
        INDEX = INDEX + 1
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce

        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(INDEX).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8') +
                   str(self.nonce).encode('utf-8'))
        return sha.hexdigest()

    def mine_block(self):
        target = '4242'
        while self.hash[-len(target):] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            print(self.hash, end='\r')
        print("\nBlock mined:", self.hash)
        return str(self.hash)
    
    def getHash(self):
        return self.hash


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]
    
    def getLastHash(self):
        return self.chain[-1] if self.chain else None

    def add_block(self, new_block):
        # new_block.previous_hash = self.get_latest_block().hash
        # new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# if __name__ == '__main__':
#     my_blockchain = Blockchain()

#     block1 = Block(1, datetime.datetime.now(), {"amount": 4}, "")
#     my_blockchain.add_block(block1)

#     block2 = Block(2, datetime.datetime.now(), {"amount": 8}, "")
#     my_blockchain.add_block(block2)

#     print("Is blockchain valid? ", my_blockchain.is_chain_valid())
