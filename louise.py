from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#born = datetime(1971, 8, 4) # provide UTC time
#age = datetime.utcnow() - born
#print(age.total_seconds())



today = datetime.today()

print(today)
#age = today - born

#print(age)