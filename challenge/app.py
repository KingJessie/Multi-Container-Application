from flask import Flask, render_template
import redis, datetime, json, os

app = Flask(__name__, template_folder='templates', static_folder='static')

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/count")
def count():
    total = redis_client.incr("visits")

    today = datetime.date.today().isoformat()
    redis_client.hincrby("visits_by_day", today, 1)

    days = [(datetime.date.today() - datetime.timedelta(days=i)).isoformat() for i in range(6, -1, -1)]
    counts = [int(redis_client.hget("visits_by_day", d) or 0) for d in days]

    return render_template("count.html", count=total,
                           labels=json.dumps(days),
                           chart_data=json.dumps(counts))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)