import random
from flask import Flask

app = Flask(__name__)

def sixDigitRandomNumber():
    num = ''
    for i in range(6):
        num += str(random.randint(0,9))
    num += '.'
    num += str(random.randint(0,9))
    return num

@app.route('/dummydata', methods=['GET'])
def dummydata():
    return {'data': sixDigitRandomNumber()}

if __name__ == "__main__":
    app.run(debug=True, port=3001, host='0.0.0.0')
