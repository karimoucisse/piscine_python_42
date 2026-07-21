class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)
		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0
		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")
	def transfer(self, amount):
		self.value += amount

class Bank(object):
	"""The bank"""
	def __init__(self):
		self.accounts = []

	def is_corrupted(self, account):
		# if len(account) % 2 != 0:
		# 	return True

		if not isinstance(account['value'], (int, float)) or not isinstance(account['id'], int)\
			or not isinstance(account['name'], (str)):
			return True


		if len([key for key in account if key.startswith('b')]) > 0:
			return True

		if 'zip' not in list(account.keys()):
			return True
		if 'addr' not in list(account.keys()):
			return True

		return False

	def fix_corrupted(self, account):
		account_keys = list(account.keys())
		for key in account_keys:
			if key.startswith('b'):
				del account[key]
		if 'zip' not in account_keys:
			account['zip'] = ""
		if 'addr' not in account_keys:
			account['addr'] = ""
		return account

	def add(self, new_account):
		""" Add new_account in the Bank
		@new_account: Account() new account to append
		@return True if success, False if an error occured
		"""
		if not new_account:
			return False
		if not isinstance(new_account, Account):
			return False

		for account in self.accounts:
			if new_account.name == account["name"]:
				return False
		self.accounts.append(new_account.__dict__)
		return True

	def transfer(self, origin, dest, amount):
		"""" Perform the fund transfer
		@origin: str(name) of the first account
		@dest: str(name) of the destination account
		@amount: float(amount) amount to transfer
		@return True if success, False if an error occured
		"""
		if not isinstance(origin, str) or not isinstance(dest, str) or\
			not isinstance(amount, (int, float)):
			return False
		if amount < 0:
			return False

		for account in self.accounts:
			if origin == account['name']:
				origin_account = account
			if dest == account['name']:
				dest_accounts = account

		if not origin_account or not dest_accounts:
			return False
		if origin_account['value'] < amount:
			return False
		if self.is_corrupted(origin_account):
			return False
		if self.is_corrupted(dest_accounts):
			return False
		origin_account['value'] -= amount
		dest_accounts['value'] += amount
		return True

	def fix_account(self, name):
		if not isinstance(name, str):
			return False
		for i in range(0, len(self.accounts)):
			if self.accounts[i]['name'] == name:
				if self.is_corrupted(self.accounts[i]):
					self.accounts[i] = self.fix_corrupted(self.accounts[i])
				return True
		return False
