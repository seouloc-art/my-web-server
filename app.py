from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
   return '바인드 마운트 실시간 반영 성공! 🚀'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)