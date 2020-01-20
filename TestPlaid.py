import os
from pprint import pprint
from typing import List
from plaid import Client as PlaidClient


plaid_client = PlaidClient(client_id=os.getenv('PLAID_CLIENT_ID'),
						   secret=os.getenv('PLAID_SECRET'),
			   			   public_key=os.getenv('PLAID_PUBLIC_KEY'),
			   			   environment=os.getenv('PLAID_ENV'))

def get_bank_transactions(access_token: str, start_date: str, end_date: str) -> List[dict]:
	return plaid_client.Transactions.get(access_token, start_date, end_date, count = 500)
	
#def get_bank_balance(access_token: str):
#	return plaid_client.Accounts.Balance.get(access_token)




wells_bank_transactions = get_bank_transactions(os.getenv('WELLS_ACCESS_TOKEN'), '1972-01-01', '2020-05-26')

coastal_bank_transactions = get_bank_transactions(os.getenv("COASTAL_ACCESS_TOKEN"), '1972-01-01', '2020-05-26')
# bank_balance = get_bank_balance(os.getenv('WELLS_ACCESS_TOKEN'))

print(f'Wells Fargo: there are {wells_bank_transactions["total_transactions"]} total transactions between those dates.')
print(f'Wells Fargo: get_wells_bank_transactions returned {len(wells_bank_transactions["transactions"])} transactions.')

print(f'Coastal: there are {coastal_bank_transactions["total_transactions"]} total transactions between those dates.')
print(f'Coastal: returned {len(coastal_bank_transactions["transactions"])} transactions.')

totalCoffeeTransactionsAmount = 0.0

for transaction in wells_bank_transactions['transactions']:
	
	name = transaction["name"][0:30]
	amountFloat = transaction["amount"]
	amount = str(amountFloat)
	date = transaction["date"]
	types = ""
	
	for t in transaction["category"]:
		types = types + " " + t + " -"

	print("Store: {0:40} Amount: {1:15} Date: {2:15} Type: {3:10}".format(name, amount, date, types))
	
	
	# Format strings to mine data for coffee shops
	types = types.lower()
	name = name.lower()
	
	if "local lion" in name or "espresso" in name or "coffee" in types or "coffee" in name:
		totalCoffeeTransactionsAmount += amountFloat
			
print("Total money spent on coffee: ${:.2f}".format(totalCoffeeTransactionsAmount))
