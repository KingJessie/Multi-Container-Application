from flask import Flask
import redis


app = Flask(__name__)


redis_client = redis.Redis(host='redis', port=6379)


@app.route('/')
def hello_world():
    return 'Hello, World!'
 
@app.route('/count')   
def count_visitor():   
    visitor_count = redis_client.incr('visitor_count')
    return f'Visitor count: {visitor_count}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)