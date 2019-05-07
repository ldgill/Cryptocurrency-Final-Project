import time
import ABI
from web3 import Web3
from web3.providers.rpc import HTTPProvider

contract_address = '0xD755338831B0bc35d75AF9e5bac3513F02d9B811'
wallet_private_key = '41811C182C5B736DDBA7F19A8A7664EC74308F7A9ABE28962300ED2D7E89A73A'
wallet_address = '0x52084bd47Bd44Bd96b108A763A8996dEf614791A'

w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/fd441bf5844f40d28190b7f2fc1bce5b'))

contract = w3.eth.contract(address = contract_address, abi = ABI.abi)

def joinBallot():
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = contract.functions.join_Ballot().buildTransaction({
    'chainId': 3,
    'gas': 500000,
    'gasPrice': w3.eth.gasPrice,
    'nonce': nonce,
    })

    signed_txn = w3.eth.account.signTransaction(txn_dict, private_key=wallet_private_key)
    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.getTransactionReceipt(result)
    count = 0
    while tx_receipt is None and (count < 30):
        time.sleep(10)
        tx_receipt = w3.eth.getTransactionReceipt(result)
        print(tx_receipt)
    if tx_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}
#    processed_receipt = contract.functions.join_Ballot().processReceipt(tx_receipt)
#    print(processed_receipt)
#    output = "Address {} broadcasted the opinion: {}"\
#    .format(processed_receipt[0].args._soapboxer, processed_receipt[0].args._opinion)
#    print(output)
    return {'Success'}

joinBallot();
