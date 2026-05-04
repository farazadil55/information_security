import hashlib
import datetime

# Simple Block class
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index                    # block number
        self.timestamp = datetime.datetime.now()  # time of block creation
        self.data = data                      # block data
        self.previous_hash = previous_hash    # link to previous block
        self.hash = self.create_hash()        # current block hash

    # function to create hash
    def create_hash(self):
        text = str(self.index) + str(self.timestamp) + self.data + self.previous_hash
        return hashlib.sha256(text.encode()).hexdigest()

# Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = []               # list to store blocks
        self.create_first_block()     # create first block

    # create first block (Genesis Block)
    def create_first_block(self):
        block = Block(0, "First Block", "0")
        self.chain.append(block)

    # add new block
    def add_block(self, data):
        last_block = self.chain[-1]   # get last block
        new_block = Block(len(self.chain), data, last_block.hash)
        self.chain.append(new_block)

    # display blockchain
    def show(self):
        for block in self.chain:
            print("Index:", block.index)
            print("Data:", block.data)
            print("Hash:", block.hash)
            print("Previous Hash:", block.previous_hash)
            print("-----------")

# create blockchain
bc = Blockchain()

# add blocks
bc.add_block("Block 1")
bc.add_block("Block 2")
bc.add_block("Block 3")
bc.add_block("Block 4")

print("Before changing data:")
bc.show()

# change data (tampering)
bc.chain[1].data = "Hacked Block"
bc.chain[1].hash = bc.chain[1].create_hash()

print("\nAfter changing data:")
bc.show()
