from flask import Blueprint
import enforce

account_api = Blueprint('user_objects', __name__)

class Transaction:
	def __init__(self, user_id, ammount, restraunt_id, table_id, date, time) -> None:
		self.user_id = user_id
		self.ammount = ammount
		self.restraunt_id = restraunt_id
		self.table_id = table_id
		self.date = date
		self.time = time
