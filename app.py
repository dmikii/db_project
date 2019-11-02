from database import Database
from user import User

Database.initialise(database="learning", host="localhost", user="postgres", password="testing123")

user = User('jose@schoolofcode.me', 'Jose', 'Salvatierra', None)

user.save_to_db()

user_from_db = User.load_from_db_by_email('jose@schoolofcode.me')

print(user_from_db)




