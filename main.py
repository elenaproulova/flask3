from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    context = {
        "caption": "Главная",
        "link": "Информация"
    }
    return render_template('home.html', **context)

@app.route("/about/")
def blog():
    context = {
        "caption": "Обо мне",
        "link": "Подробнее об этом"
    }
    return render_template('about.html', **context)


if __name__ == "__main__":
    app.run()