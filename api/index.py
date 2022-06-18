from http.server import BaseHTTPRequestHandler
import redis
class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.end_headers()
    r = redis.Redis(
    host= 'eu1-decent-amoeba-37317.upstash.io',
    port= '37317',
    password= '2bae71892aee4943ba60af8067ee190e', ssl=True)
    r.set('foo','bar')
    self.wfile.write(self.headers.get('x-forwarded-for').encode())
    self.wfile.write(r.get('foo'))

