from app import app
from flask import render_template, request, abort, redirect, url_for
from uuid import uuid4
from datetime import datetime
from app import db
from app.models import WebhookRequests
from . import socketio
from flask_socketio import SocketIO, emit


@app.route('/get_webhook', methods=['POST'])
def webhook():
        uuid_id = uuid4()
        auth = request.authorization
        if auth:
            user_login = auth.username
            user_password = auth.password
        else:
            user_login = user_password = None
        if request.content_type == 'application/json':
            json = request.json
            decoded_xml = None
        elif request.content_type == 'application/xml' or 'text/xml':
            decoded_xml = bytes.decode(request.data, encoding='utf-8')
            json = None
        data_db_input = WebhookRequests(id=uuid_id, method=request.method, json_body=json,
                                            xml_body=decoded_xml, ip=request.remote_addr, content_type=request.content_type,
                                            login=user_login, password=user_password,
                                            user_agent=request.headers.get('User-Agent'))
        db.session.add(data_db_input)
        db.session.commit()
        json_to_js = {"id": str(uuid_id), "method": request.method, "json_body": json, "ip": request.remote_addr,
                               "xml_body": str(decoded_xml), "content_type": request.content_type, "login": user_login,
                               "password": user_password, "user_agent": request.headers.get('User-Agent')}
        print(json_to_js)
        socketio.emit('reply', json_to_js)
        return 'ok',  200



@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/webhook')
def webhook_main():
    page = request.args.get('page', 1, type=int)
    # last_request = WebhookRequests.query.order_by(WebhookRequests.date.desc()).all()
    last_request = WebhookRequests.query.order_by(WebhookRequests.date.desc()).paginate(page, app.config['REQUESTS_PER_PAGE'], False)
    next_page = url_for('webhook_main', page=last_request.next_num) \
        if last_request.has_next else None
    prev_page = url_for('webhook_main', page=last_request.prev_num) \
        if last_request.has_prev else None
    return render_template("index.html", last_request=last_request.items, next_page=next_page, prev_page=prev_page,
                           title='All Webhooks')


@app.route('/webhook/request/<string:id>')
def message_id(id):
    req = WebhookRequests.query.get(id)
    if req is None:
        return render_template("404_request.html", req=id)
    else:
        return render_template("detailed_request.html", req=req)


@app.route('/test_platform')
def test_platform():
    return render_template("test_platform.html")


@app.route('/speedchecker')
def speedchecker():
    return render_template("speedchecker.html")


@app.route('/cluster_status')
def cluster_status():
    return render_template("cluster_status.html")
