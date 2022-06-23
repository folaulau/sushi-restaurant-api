from app import app

@app.route('/')
def hello():
    app.logger.info('hello')
    return 'Hello'

@app.route('/ping')
def ping():
    app.logger.info('ping')
    return {"status":"good"}