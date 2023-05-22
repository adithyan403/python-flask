import app
from werkzeug.serving import run_simple

if __name__ == 'app':
    run_simple('localhost', 5000, app, use_reloader=True)
