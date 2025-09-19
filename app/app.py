from flask import Flask
from prometheus_client import Counter, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

REQUEST_COUNT = Counter('http_requests_total', 'Total number of HTTP requests')

@app.route('/')
def hello_world():
    REQUEST_COUNT.inc() # Increment the counter on each request
    return 'Hello, DevOps Engineer!'

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
