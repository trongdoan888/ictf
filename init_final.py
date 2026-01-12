from .core import app, mysql

# Đăng ký các blueprint/routes từ các module con
from . import general
from . import teams
from . import services
from . import scored_events
from . import scores
from . import scripts
from . import uploads
from . import ticket

@app.route('/ping')
def ping_internal():
    return 'pong'
