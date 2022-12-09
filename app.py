from flask import Flask
from redis import Redis, RedisError
import os
import socket
# Connect to Redis
redis = Redis(host='redis',
                port=6379,
                db=0,
                socket_connect_timeout=2,
                socket_timeout=2)
app = Flask(__name__)
@app.route('/')
def hello():
    try:
        visits = redis.incr('counter')
    except RedisError:
        visits = '''<i>cannot connect to Redis server, counter
disabled</i>'''
    
    html = '''<h3>Hello, {world}!</h3
                <h4>Hello, {name}. </h4>
                <b>Employee ID</b> {emp_id}<br/>
                <b>Hostname:</b> {hostname}<br/>
                <b>Visits:</b> {visits}'''
    return html.format(
            world=os.getenv('WORLD', 'OSS-LAB-Docker-World'),
            name=os.getenv('NAME', 'Test'),
            emp_id=os.getenv('EMP_ID', '-'),
            hostname=socket.gethostname(),
            visits=visits)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
