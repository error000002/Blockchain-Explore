import json
# from attrdict import  AttrDict
from web3 import Web3
from flask import Flask, jsonify
from flask_cors import CORS
from web3.middleware import geth_poa_middleware

app = Flask(__name__)
# CORS(app)
CORS(app, resources={r"/api/*": {"origins": "*"}}, headers='Content-Type')


#Getting block data using block number
@app.route('/api/block/number/<int:block_number>', methods=['GET'])
def fetch_block_data_num(block_number):
    try:
        w3 = Web3(Web3.HTTPProvider('https://celo-mainnet.infura.io/v3/c0675c5a775e421db5430b57358c8b52'))
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
        w3 = Web3(Web3.HTTPProvider('https://celo-mainnet.infura.io/v3/c0675c5a775e421db5430b57358c8b52'))
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
        w3 = Web3(Web3.HTTPProvider('https://celo-mainnet.infura.io/v3/c0675c5a775e421db5430b57358c8b52'))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        Transaction_data = w3.eth.get_transaction(transaction_hash)

        return json.dumps(Transaction_data, default=str)
    except:
        return json.dumps("Please Enter Transaction Hash")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
