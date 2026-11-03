from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '안녕하세요! 제 첫 번째 웹 서버입니다! 🎉'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)