import os
from flask import Flask, app
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

app = Flask(__name__)

@app.route('/<randomstring>')
def return_backwards_string(random_string):
    return "".join(reversed(random_string))



@app.route('/get-mode')
def get_mode():
    return os.environ.get('MODE')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

