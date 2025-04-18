from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    context = {
        "link": "Информация"
    }
    return render_template('home.html', **context)

@app.route("/about/")
def blog():
    context = {
        "link": "Подробнее об этом"
    }
    return render_template('about.html', **context)


if __name__ == "__main__":
    app.run()