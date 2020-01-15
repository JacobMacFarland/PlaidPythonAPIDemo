import os
from pprint import pprint
from typing import List
from plaid import Client as PlaidClient


plaid_client = PlaidClient(client_id='5e0173f01a2d810011a2851b',
						   secret='5f31790e61e8350b94635a40aa809f',
			   			   public_key='dd7c74bd8189ddec4cfee87943a9a4',
			   			   environment='sandbox')

def get_some_transactions(access_token: str, start_date: str, end_date: str) -> List[dict]:
	return plaid_client.Transactions.get(access_token, start_date, end_date)

some_transactions = get_some_transactions('access-sandbox-47f91189-080a-4b53-a004-e974499b1529', '1972-01-01', '2020-05-26')

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
