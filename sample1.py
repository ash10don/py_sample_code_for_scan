import os
import sqlite3
import pickle
import hashlib
import logging
from flask import Flask, request

app = Flask(__name__)

#Hardcoded API Key (Security Flaw: Sensitive Data Exposure)
API_KEY = "1234567890abcdef"

#Insecure Database Connection (No input validation, allows SQL injection)
def insecure_db_connect(query):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(query)  #SQL Injection Vulnerability
    results = cursor.fetchall()
    conn.close()
    return results

#Weak Hashing Algorithm (MD5 is deprecated)
def weak_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

#Insecure Deserialization (Pickle can execute arbitrary code)
def insecure_deserialize(data):
    return pickle.loads(data)  #Remote Code Execution risk

#Command Injection (User input passed to os.system)
@app.route('/run', methods=['POST'])
def run_command():
    cmd = request.form.get('cmd')  #No sanitization
    os.system(cmd)  #Arbitrary command execution vulnerability
    return "Command executed"

#Logging Sensitive Data (User passwords should not be logged)
logging.basicConfig(filename='app.log', level=logging.INFO)
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    logging.info(f'Login attempt: {username}, Password: {password}')  #Password logged
    return "Login attempted"

if __name__ == '__main__':
    app.run(debug=True)
