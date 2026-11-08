from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
   return '우와! 진짜로 바뀌었어요! 🎉'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)