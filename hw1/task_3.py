orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

returned_sum = sum(o['amount'] for o in orders if o['status'] == 'returned')
print(returned_sum)

returners = {o['buyer'] for o in orders if o['status'] == 'returned'}
print(returners)

delivered = [o for o in orders if o['status'] == 'delivered']
print(len(delivered))

avg_check = sum(o['amount'] for o in delivered) / len(delivered)
print(round(avg_check, 2))
