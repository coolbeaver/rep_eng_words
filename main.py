from flask import Flask, render_template, request, session

from word_classes import Word

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

word = Word()


@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    data = word.select_random_word()
    if 'num' not in session:
        session['num'] = 1
    if request.method == 'POST':
        print(request.form['ans'])
        session['num'] = session.get('num') + 1
        return render_template('index.html', eng=data[0], rus=data[1], num=session.get('num'))

    return render_template('index.html', eng=data[0], rus=data[1], num=session.get('num'))


if __name__ == '__main__':
    app.run()
