import json
from web3 import Web3
from flask import Flask, jsonify
from flask_cors import CORS
from web3.middleware import geth_poa_middleware

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}}, headers='Content-Type')

w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/H82u2Z2YEeKD5Re6VvB7eSkDBIFVA8Ey'))
if w3.isConnected():
    print("Connected to Ethereum network")
else:
    print("Not connected to Ethereum network")

# Fetch the balance of an Ethereum address
# '0x3b9bA781797b57872687Ce5d5219A1A4Bc0e85ea'
@app.route('/api/balance/<address>', methods=['GET'])
def fetch_metamask_data(address):
    try:
        w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/H82u2Z2YEeKD5Re6VvB7eSkDBIFVA8Ey'))
        # w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        data = w3.eth.getBalance(address)
        balance = data / 10 ** 18
        return json.dumps(balance, default=str)
    except:
        return json.dumps("Please Enter valid Address")

#Getting block data using block number
@app.route('/api/block/number/<int:block_number>', methods=['GET'])
def fetch_block_data_num(block_number):
    try:
        w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/H82u2Z2YEeKD5Re6VvB7eSkDBIFVA8Ey'))
        # w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        Block_data = w3.eth.getBlock(block_number)

        return json.dumps(Block_data, default=str)
    except:
        return json.dumps("Please Enter Block Number")

print("\n")

#Getting block data using block Hash
# '0x55a2d76a8c181f5ff01efc382aea84a8e886172999459c0f83bd1ba6f57a8d6e'

@app.route('/api/block/hash/<block_number>', methods=['GET'])
def fetch_block_data_hash(block_number):
    try:
        w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/H82u2Z2YEeKD5Re6VvB7eSkDBIFVA8Ey'))
        # w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        Block_data = w3.eth.getBlock(block_number)

        return json.dumps(Block_data, default=str)

    except:
        return json.dumps("Please Enter Block Hash")

print("\n")

# Getting Transaction data using transaction hash:

# '0x1287bce9d76712f6410c585e1921056f1abfc98c9bb8b57680873de561160234'
@app.route('/api/block/transaction_hash/<transaction_hash>', methods=['GET'])
def fetch_transaction_data(transaction_hash):
    try:
        w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/H82u2Z2YEeKD5Re6VvB7eSkDBIFVA8Ey'))
        # w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        Transaction_data = w3.eth.get_transaction(transaction_hash)

        return json.dumps(Transaction_data, default=str)
    except:
        return json.dumps("Please Enter Transaction Hash")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
