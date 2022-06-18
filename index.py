from flask import Flask, Response
app = Flask(__name__)
import redis

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    r = redis.Redis(
      host= 'eu1-decent-amoeba-37317.upstash.io',
      port= '37317',
      password= '2bae71892aee4943ba60af8067ee190e', ssl=True)
    return Response("<h1>Flask</h1><p>Hello, %s, You visited: /%s</p>" % (r.get('foo'), path), mimetype="text/html")
