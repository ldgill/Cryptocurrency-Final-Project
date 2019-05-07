import time
import ABI
from web3 import Web3
from web3.providers.rpc import HTTPProvider
from enum import Enum
from lxml import etree
import re
import getpass
import datetime
import random
import base64
from cryptography.fernet import Fernet

contract_address = '0x6ab3bAA1eF32D0C956a8A8E6E26397760fFd17bF'
wallet_private_key = '41811C182C5B736DDBA7F19A8A7664EC74308F7A9ABE28962300ED2D7E89A73A'
wallet_address = '0x52084bd47Bd44Bd96b108A763A8996dEf614791A'
currUser = -1;

w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/fd441bf5844f40d28190b7f2fc1bce5b'))
contract = w3.eth.contract(address = contract_address, abi = ABI.abi)
looping = True
class State(Enum):
        NONE = 0
        START = 1
        VOTE_RECORDED = 2
        VOTE_SEALED = 3
        VOTE_AUDITED = 4
        VOTE_VERIFIED = 5

def isValidEmail(email):
    if len(email) > 7:
        if (re.match(r"[^@]+@[^@]+\.[^@]+", email) != None):
            return True
    return False

def validateVoter():
    global currUser
    prompt = input('Have you registered to vote?(yes/no): ')
    if(prompt == "yes" or prompt == "y" or prompt == "Yes" or prompt == "Y"):
        firstname = input('Enter your first name: ')
        lastname = input('Enter your last name: ')
        social = getpass.getpass(prompt='Enter your social security number: ')
        for voter in root.findall('voter'):
            userId = voter.get('userId')
            for info in voter.findall('info'):
                fn = info.get('firstname')
                ln = info.get('lastname')
                ss = info.get('ss')
                if (fn == firstname and ln == lastname and social == ss):
                    currUser = userId
        if (currUser == -1):
            print("No voter found.")            
    
    if (prompt == "no" or prompt == "n" or prompt == "No" or prompt == "N"):
        firstname = input('Enter your first name: ')
        lastname = input('Enter your last name: ')
        email = input('Enter your email: ')
        if not (isValidEmail(email)):
            email = input('Please enter a valid email: ')
        dob = input('Enter your date of birth (mm/dd/yyyy): ')
        social = getpass.getpass(prompt='Enter your social security number: ')
    
        currUser = len(root)+1;
        child = etree.SubElement(root, "voter", userId="{}".format(len(root)+1))
        info = etree.SubElement(child, "info", dob="{}".format(dob),  email="{}".format(email),  firstname="{}".format(firstname),  lastname="{}".format(lastname), ss="{}".format(social))
        d = datetime.datetime.today()
        reg = etree.SubElement(child, "registration", registerDate="{}".format(d.strftime('%m/%d/%Y')), valid="True")
        tree.write('information.xml', pretty_print=True)

def Recipt(txn):
    signed_txn = w3.eth.account.signTransaction(txn, private_key=wallet_private_key)
    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.getTransactionReceipt(result)
    count = 0
    while tx_receipt is None and (count < 30):
        time.sleep(10)
        tx_receipt = w3.eth.getTransactionReceipt(result)
        if tx_receipt is None:
            print("Mining block...")
        else:
            print("=======================Blockchain Recipt============================")
            print(tx_receipt)
            print("====================================================================")
    if tx_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}
    return {'status': 'Recorded Vote'}

def joinBallot():
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = contract.functions.join_Ballot().buildTransaction({
     'chainId': 3,
     'gas': 500000,
     'gasPrice': w3.eth.gasPrice,
     'nonce': nonce,
     'value': w3.toWei(0.01,'ether')
     })
    Recipt(txn_dict)
    return

def RecordBallot(byte):
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = contract.functions.record_vote(byte,wallet_address).buildTransaction({
    'chainId': 3,
    'gas': 500000,
    'gasPrice': w3.eth.gasPrice,
    'nonce': nonce,
    })
    Recipt(txn_dict)
    return

def SealBallot(vote):
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = contract.functions.seal_vote(vote,wallet_address).buildTransaction({
    'chainId': 3,
    'gas': 500000,
    'gasPrice': w3.eth.gasPrice,
    'nonce': nonce,
    })
    Recipt(txn_dict)
    return

def AuditBallot():
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = contract.functions.audit_vote(wallet_address).buildTransaction({
    'chainId': 3,
    'gas': 500000,
    'gasPrice': w3.eth.gasPrice,
    'nonce': nonce,
    })
    Recipt(txn_dict)
    return

def Authenticate():
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = contract.functions.authenticate(wallet_address).buildTransaction({
    'chainId': 3,
    'gas': 500000,
    'gasPrice': w3.eth.gasPrice,
    'nonce': nonce,
    })
    Recipt(txn_dict)
    print ("Verification successful!")
    return

if __name__ == "__main__":
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse('information.xml', parser)
    root = tree.getroot()
    print("====================================================================")
    print("====================================================================")
    print("============= /$$    /$$  /$$$$$$  /$$$$$$$$ /$$$$$$$$$ ============")
    print("============= | $$   | $$ /$$__  $$|__  $$__/| $$_____/ ============")
    print("============= | $$   | $$| $$  \ $$   | $$   | $$   ================")
    print("============= |  $$ / $$/| $$  | $$   | $$   | $$$$$   =============")
    print("============== \  $$ $$/ | $$  | $$   | $$   | $$__/   =============")
    print("==============  \  $$$/  | $$  | $$   | $$   | $$     ==============")
    print("===============  \  $/   |  $$$$$$/   | $$   | $$$$$$$$ ============")
    print("================  \_/     \______/    |__/   |________/ ============")
    print("====================================================================")
    print("====================================================================")
    
    while (currUser == -1):
        validateVoter()
    state = 0;

    prompt = input('Would you like start a ballot or continue your last one?(Start/Continue): ')
    if (prompt == "start" or prompt == "Start" or prompt == "s" or prompt == "S"):
        state = 0
    if (prompt == "continue" or prompt == "Continue" or prompt == "c" or prompt == "C"):
        state = contract.functions.stateofVote(wallet_address).call();
    print ("Connecting to blockchain...")
    if (state == 0):
        joinBallot();
        state = 1
    while looping:
        if (state == 1 or state == 4):
            prompt = input('Would You like to vote on the Blockchain?(yes/no): ')
            if (prompt == "yes" or prompt == "y" or prompt == "Yes" or prompt == "Y"):
                rvt = input('Red Vines or Twizlers?: ')
                ly = input('Laurel or Yanny?: ')
                bbwg = input('Is the dress black and blue or white and gold?: ')
                gj = input('Gif or Jif?: ')
                message = "Red Vines or Twizlers?: {}, Laurel or Yanny?: {}, Is the dress black and blue or white and gold?: {}, Gif or Jif?: {}".format(rvt, ly, bbwg, gj).encode()
                soical_key = getpass.getpass(prompt='Enter your social security number for encryption: ')
                temp=base64.urlsafe_b64encode(contract.functions.encrypt(soical_key).call())
                cipher_suite = Fernet(temp)
                encoded_text = cipher_suite.encrypt(message)
                print("========================Encrypted Vote==============================")
                print(encoded_text)
                print("====================================================================")
                print ("Sending to blockchain...")
                RecordBallot(encoded_text);
                state = 2
            if (prompt == "no" or prompt == "n" or prompt == "No" or prompt == "N"):
                looping = False
                break
        if(state == 2):
            prompt = input('Would You like to Audit or Seal Your Vote?(Audit/Seal/No): ')
            if (prompt == "Audit" or prompt == "A" or prompt == "a" or prompt == "audit"):
                AuditBallot();
                soical_key = getpass.getpass(prompt='Enter your social security number for decryption: ')
                temp = base64.urlsafe_b64encode(contract.functions.encrypt(soical_key).call())
                cipher_suite = Fernet(temp)
                returnedBytes = contract.functions.getAudit(wallet_address).call()
                decode_text = cipher_suite.decrypt(returnedBytes)
                print("========================Dencrypted Vote=============================")
                print(decode_text)
                print("====================================================================")
                state = 4
        
            if (prompt == "Seal" or prompt == "S" or prompt == "seal" or prompt == "s"):
                vote =contract.functions.getAudit(wallet_address).call()
                print ("Sealing on blockchain...")
                SealBallot(vote)
                print("Vote Sealed!")
                state = 3
            if (prompt == "no" or prompt == "n" or prompt == "No" or prompt == "N"):
                looping = False
                break
        if(state == 3):
            prompt = input('Are you ready to verify your vote? (yes/no)')
            if (prompt == "yes" or prompt == "y" or prompt == "Yes" or prompt == "Y"):
                firstname = input('Enter your first name: ')
                lastname = input('Enter your last name: ')
                social = getpass.getpass(prompt='Enter your social security number: ')
                for voter in root.findall('voter'):
                    userId = voter.get('userId')
                    for info in voter.findall('info'):
                        fn = info.get('firstname')
                        ln = info.get('lastname')
                        ss = info.get('ss')
                        if (fn == firstname and ln == lastname and social == ss):
                            currUser = userId
                            state = 5
                            print ("Verification in progress...")
                            Authenticate();
                if (currUser == -1):
                    print("User Credentials Incorrect")
            if (prompt == "no" or prompt == "n" or prompt == "No" or prompt == "N"):
                state = 5
                break
        if(state == 5):
            print("Thank you for your vote.")
            looping = False
            break
