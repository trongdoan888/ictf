from .core import app, mysql

@app.route('/ping')
def ping_internal():
    return 'pong'

from . import general, teams, services, scored_events, scores, scripts, uploads, ticket
