from flask import Flask, render_template  

app = Flask(__name__)

@app.route("/", defaults={"path":"index.html"})
@app.route("/<path:path>")
def static_file(path):
    try:
        return app.send_static_file(path)
    except:
        return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)