from flask import Flask, request, render_template

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def form():
    message = ''
    if request.method == 'POST':
        data = request.form['data']
        message = f'Otrzymano dane: {data}'
    return render_template('form.html', message=message)

if __name__ == '__main__':
    application.run(debug=True)
