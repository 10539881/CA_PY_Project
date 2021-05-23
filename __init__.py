"""
import pyodbc
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import sqlalchemy
from sqlalchemy import create_engine, Table, MetaData, select, or_, and_, insert

app = Flask(__name__)

server = '23.97.146.240' 
database = 'Student'
driver = 'ODBC Driver 17 for SQL Server'
username = 'sa' 
password = 'Password888£'

#with open(".pw") as f:
 #   password = f.read()

#setting up a sql connection
database_connection = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'
engine = create_engine(database_connection)
connection = engine.connect()

metadata = MetaData()

"""