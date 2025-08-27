
from flask import Flask, render_template
import redis
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/count')
def count_visitor():
    visitor_count = redis_client.incr('visitor_count')
    return render_template('count.html', count=visitor_count)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)