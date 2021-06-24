from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_socketio import SocketIO
import time
import random
import json as jason

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
moment = Moment(app)
socketio = SocketIO(app)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    moment.init_app(app)
    return app


from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)


from app import routes, models


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + json['data'])
    # data = {}
    # data['id'] = '214351fe-ae82-4997-9e7a-5cdead4e48d5'
    # data['method'] = 'POST'
    # data['ip'] = '127.0.0.1'
    # data['date'] = '2021-05-12 10:49:10.914226'
    # data['content_type'] = 'application/json'
    # data['content_type'] = 'application/json'
    # data['json_body'] = {'value': 1}
    # for _ in range(2):
    #     socketio.emit('reply', data)
    #     time.sleep(2)


@socketio.on('start')
def speedcheck(json):
    print('received json: ' + json['data'])
    data = {}
    for _ in range(50):
        data['key'] = random.randint(100, 1000)
        json_data = jason.dumps(data)
        socketio.emit('dataSpeed', json_data)
        time.sleep(1)




if __name__ == '__main__':
    socketio.run(app)

