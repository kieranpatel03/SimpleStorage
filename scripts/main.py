from brownie import SimpleStorage, accounts, network, Contract


def main():
    if network.show_active() == "development":
        account = accounts[0]
    else:
        account = accounts.load('TestingAccount')
    contract = Contract("0x2cf758b8bfe186989221e6f93cbb8c242704abbd")
    integer = contract.get_int()
    print(integer)
    # storage = SimpleStorage.deploy({"from": account})
    # print(storage.get_int())
    # transaction = storage.set_int(10, {"from": account})
    # transaction.wait(1)
    # print(storage.get_int())
