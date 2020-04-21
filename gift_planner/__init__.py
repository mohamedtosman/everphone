from flask import Flask
from flask_sqlalchemy import SQLAlchemy

async_mode = None
app = Flask(__name__)
app.config.from_pyfile('../config.cfg')
db = SQLAlchemy(app)

import gift_planner.model  # NOQA
import gift_planner.service  # NOQA


service.init_db()
