from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/ping')
def ping():
    return {"status": "ok"}

@app.route('/count')
def count():
    redis_client.incr('visits')
    return {"count": redis_client.get('visits')}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
