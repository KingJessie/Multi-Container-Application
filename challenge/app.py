from flask import Flask
import redis
import os


app = Flask(__name__)

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)


@app.route('/')
def welcome():
    return 'Welcome to the Coderco Visitor Counter Challenge'
 
@app.route('/count')   
def count_visitor():   
    visitor_count = redis_client.incr('visitor_count')
    return f'This page has been visited {visitor_count} times'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)