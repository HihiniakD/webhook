from app import create_app, db
from app.models import WebhookRequests

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'WebhookRequests': WebhookRequests}


