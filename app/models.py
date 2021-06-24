from app import db
from sqlalchemy.dialects.postgresql import JSON, TEXT
from sqlalchemy.dialects import postgresql
from datetime import datetime

class WebhookRequests(db.Model):
    __tablename__ = 'base_webhook'

    id = db.Column(db.String(), primary_key=True)
    method = db.Column(db.String(), nullable=False)
    json_body = db.Column(JSON)
    xml_body = db.Column(TEXT)
    ip = db.Column(postgresql.INET)
    content_type = db.Column(db.String())
    login = db.Column(db.VARCHAR())
    password = db.Column(db.VARCHAR())
    user_agent = db.Column(db.VARCHAR())
    # date = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    date = db.Column(db.DateTime, default=datetime.utcnow)


    def __init__(self, id, method, json_body, xml_body, ip, content_type, login, password, user_agent):
        self.id = id
        self.method = method
        self.json_body = json_body
        self.xml_body = xml_body
        self.ip = ip
        self.content_type = content_type
        self.login = login
        self.password = password
        self.user_agent = user_agent


    def __repr__(self):
        return '<WebhookRequests %r>' % self.id