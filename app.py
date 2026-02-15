from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/proactive", methods=["GET", "POST"])
def proactive():
    upload_path = app.config['UPLOAD_FOLDER']
    existing_images = os.listdir(upload_path)

    if request.method == "POST":
        file = request.files.get("image")
        slide = request.form.get("slide")

        if file and slide:
            filename = f"{slide}.png"
            file.save(os.path.join(upload_path, filename))

        return redirect(url_for("proactive"))

    return render_template("proactive.html", images=existing_images)


@app.route("/performance")
def performance():
    return render_template("performance.html")


if __name__ == "__main__":
    app.run(debug=True)
