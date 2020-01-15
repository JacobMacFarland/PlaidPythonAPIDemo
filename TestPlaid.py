import os
from pprint import pprint
from typing import List
from plaid import Client as PlaidClient


plaid_client = PlaidClient(client_id=os.getenv('PLAID_CLIENT_ID'),
						   secret=os.getenv('PLAID_SECRET'),
			   			   public_key=os.getenv('PLAID_PUBLIC_KEY'),
			   			   environment=os.getenv('PLAID_ENV'))

def get_some_transactions(access_token: str, start_date: str, end_date: str) -> List[dict]:
	return plaid_client.Transactions.get(access_token, start_date, end_date)

some_transactions = get_some_transactions(os.getenv('WELLS_ACCESS_TOKEN'), '1972-01-01', '2020-05-26')

print(f'there are {some_transactions["total_transactions"]} total transactions between those dates.')
print(f'get_some_transactions returned {len(some_transactions["transactions"])} transactions.')

# for transaction in some_transactions['transactions']:
#	print(transaction)
	
print(some_transactions['transactions'][0])	

# pprint(some_transactions['transactions'][0].keys())

#print({category
#       for transaction in some_transactions['transactions'] if transaction['category'] is not None
#       for category in transaction['category']})
#pprint(some_transactions['accounts'])
