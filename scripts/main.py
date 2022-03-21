from brownie import SimpleStorage, accounts, network, Contract


def main():
    if network.show_active() == "development":
        account = accounts[0]
    else:
        account = accounts.load('TestingAccount')
    if len(SimpleStorage) == 0:
        contract = SimpleStorage.deploy({"from": account})
    else:
        contract = SimpleStorage[-1]
    print(contract.get_int())
    transaction = contract.set_int(10, {"from": account})
    transaction.wait(1)
    print(contract.get_int())
