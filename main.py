from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetOptInParams,
    AssetTransferParams,
    PayParams,
)

algorand = AlgorandClient.default_local_net()
dispenser = algorand.account.dispenser()
# print(dispenser.address)




creator = algorand.account.random()

algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=creator.address,
        amount=10_000_000  # 10 algos
    )
)
print(algorand.account.get_information(creator.address))
algorand.send.payment(

    PayParams(
        sender=dispenser.address,
        receiver=creator.address,
        amount=10_000_000  # 10 algos
    )
)

print(algorand.account.get_information(creator.account))


sent_tnx=algorand.send.assest_create(
    AssetCreateParams(
sender=creator.address,
total=100,
assest_name="WebPak3",
uint_name="W3P"

    ))
    assest_id=sent_tnx["confirmation"]["assest-index"]
    receiver_id=