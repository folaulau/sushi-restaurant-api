from app import app

@app.route('/')
def welcome():
    app.logger.info('welcome to sushi api')
    return {"message":"welcome to sushi api"}

@app.route('/ping')
def ping():
    app.logger.info('ping')
    return {"status":"up"}
