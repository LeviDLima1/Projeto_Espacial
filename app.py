from app import app
if __name__ == '__main__': #executar a aplicação Flask app
    app.run(host='127.0.0.1',debug=False, port=5000)