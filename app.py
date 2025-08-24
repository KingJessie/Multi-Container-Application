from flask import Flask
import redis


app = Flask(__name__)


redis_client = redis.Redis(host='redis', port=6379)


@app.route('/')
def welcome():
    return 'Welcome to the Coderco Visitor Counter Challenge'
 
@app.route('/count')   
def count_visitor():   
    visitor_count = redis_client.incr('visitor_count')
    return f'This page has been visited {visitor_count} times'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)