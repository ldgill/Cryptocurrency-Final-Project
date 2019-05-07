abi = """[
    {
    "constant": false,
    "inputs": [
    {
    "name": "person",
    "type": "address"
    }
    ],
    "name": "audit_vote",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
    },
    {
    "constant": false,
    "inputs": [
    {
    "name": "person",
    "type": "address"
    }
    ],
    "name": "authenticate",
    "outputs": [],
    "payable": true,
    "stateMutability": "payable",
    "type": "function"
    },
    {
    "constant": false,
    "inputs": [],
    "name": "join_Ballot",
    "outputs": [],
    "payable": true,
    "stateMutability": "payable",
    "type": "function"
    },
    {
    "constant": false,
    "inputs": [
    {
    "name": "encoded_vote",
    "type": "bytes"
    },
    {
    "name": "person",
    "type": "address"
    }
    ],
    "name": "record_vote",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
    },
    {
    "constant": false,
    "inputs": [
    {
    "name": "vote",
    "type": "string"
    },
    {
    "name": "person",
    "type": "address"
    }
    ],
    "name": "seal_vote",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
    },
    {
    "inputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "constructor"
    },
    {
    "constant": true,
    "inputs": [
    {
    "name": "",
    "type": "address"
    }
    ],
    "name": "balances",
    "outputs": [
    {
    "name": "",
    "type": "uint256"
    }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
    },
    {
    "constant": true,
    "inputs": [],
    "name": "election_name",
    "outputs": [
    {
    "name": "",
    "type": "string"
    }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
    },
    {
    "constant": true,
    "inputs": [
    {
    "name": "social",
    "type": "string"
    }
    ],
    "name": "encrypt",
    "outputs": [
    {
    "name": "",
    "type": "bytes32"
    }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
    },
    {
    "constant": true,
    "inputs": [
    {
    "name": "person",
    "type": "address"
    }
    ],
    "name": "getAudit",
    "outputs": [
    {
    "name": "",
    "type": "bytes"
    }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
    },
    {
    "constant": true,
    "inputs": [
    {
    "name": "person",
    "type": "address"
    }
    ],
    "name": "stateofVote",
    "outputs": [
    {
    "name": "",
    "type": "uint8"
    }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
    },
    {
    "constant": true,
    "inputs": [
    {
    "name": "",
    "type": "address"
    }
    ],
    "name": "Voter",
    "outputs": [
    {
    "name": "voted",
    "type": "bool"
    },
    {
    "name": "e_vote",
    "type": "bytes"
    },
    {
    "name": "vote",
    "type": "string"
    },
    {
    "name": "state",
    "type": "uint8"
    }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
    }
    ]"""
