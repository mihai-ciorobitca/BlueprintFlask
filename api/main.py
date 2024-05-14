from flask import Flask, render_template
from api.blueprints import home, admin, login
import traceback
from flask_caching import Cache

app = Flask(__name__, template_folder="blueprints/templates")
cache = Cache(app, config={"CACHE_TYPE": "simple"})

app.register_blueprint(home.home_blueprint)
app.register_blueprint(login.login_blueprint)
app.register_blueprint(admin.admin_blueprint)

@app.route("/prime")
@cache.cached(timeout=100)
def prime():
    i = 0
    nr = 2
    while i <= 100:
        test = True
        for j in range(2, nr//2):
            if nr % j == 0:
                break
        if test:
            i += 1
        nr += 1
    return str(nr)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def page_404(error):
    return render_template("404.html")

@app.errorhandler(500)
def page_500(error):
    return render_template("500.html", error=traceback.format_exc())