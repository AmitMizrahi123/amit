from flask import Flask, render_template
import os


app = Flask(__name__, template_folder="templates")
app.config.from_mapping(SECRET_KEY=os.environ.get('SECRET_KEY') or 'dev_key')


@app.route('/')
def zohar():
    return render_template('zohar.html')


@app.route('/more_pictures')
def more_pictures():
    return render_template('zoharVideo.html')


if __name__ == '__main__':
    app.run(debug=True)