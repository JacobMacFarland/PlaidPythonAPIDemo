import os
from pprint import pprint
from typing import List
from plaid import Client as PlaidClient

plaid_client = PlaidClient(client_id=os.getenv('PLAID_CLIENT_ID'),
						   secret=os.getenv('PLAID_SECRET'),
			   			   public_key=os.getenv('PLAID_PUBLIC_KEY'),
			   			   environment=os.getenv('PLAID_ENV'))

def get_some_transactions(access_token: str, start_date: str, end_date: str) -> List[dict]:
	return plaid_client.Transactions.get(access_token, start_date, end_date, count=500)

some_transactions = get_some_transactions(os.getenv('WELLS_ACCESS_TOKEN'), '1972-01-01', '2020-05-26')

print(f'there are {some_transactions["total_transactions"]} total transactions between those dates.')
print(f'get_some_transactions returned {len(some_transactions["transactions"])} transactions.')

totalCoffeeTransactionsAmount = 0.0

for transaction in some_transactions['transactions']:
	
	name = transaction["name"][0:30]
	amountFloat = transaction["amount"]
	amount = str(amountFloat)
	date = transaction["date"]
	types = ""
	
	for t in transaction["category"]:
		types = types + " " + t + " -"

	#print("Store: {0:40} Amount: {1:15} Date: {2:15} Type: {3:10}".format(name, amount, date, types))
	
	
	# Format strings to mine data for coffee shops
	types = types.lower()
	name = name.lower()
	
	if "local lion" in name or "espresso" in name or "coffee" in types or "coffee" in name:
		totalCoffeeTransactionsAmount += amountFloat
			
print("Total money spent on coffee: ${:.2f}".format(totalCoffeeTransactionsAmount))
#print(some_transactions['transactions'][0])	

# pprint(some_transactions['transactions'][0].keys())

#print({category
#       for transaction in some_transactions['transactions'] if transaction['category'] is not None
#       for category in transaction['category']})
#pprint(some_transactions['accounts'])
