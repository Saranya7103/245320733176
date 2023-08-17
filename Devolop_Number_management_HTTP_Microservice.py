import requests
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/numbers')
def numbers():
    urls = request.args.getlist('url')

    numbers = []

    for i in urls:
        response = requests.get(i, timeout=500)
        if response.status_code == 200:
            numbers.extend(json.loads(response.content)['numbers'])

    numbers = sorted(set(numbers))

    return json.dumps({'numbers': numbers})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)