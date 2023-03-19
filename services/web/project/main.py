import os
from werkzeug.utils import secure_filename
from flask import render_template, send_from_directory, Flask, flash, request, redirect, url_for

import sms
import inference
import constants


app = Flask(__name__)

UPLOAD_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static/uploads"
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite://")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STATIC_FOLDER'] = f"{os.getenv('APP_FOLDER')}/project/static"

app.config["UPLOAD_FOLDER"] = f"{os.getenv('APP_FOLDER')}/project/static/uploads"
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024 * 1024


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)

        file = request.files["file"]
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("uploaded_file", filename=filename))

    return render_template("home.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    here = os.getcwd()
    image_path = os.path.join(here, app.config["UPLOAD_FOLDER"], filename)
    res = inference.query(image_path)
    found = False
    if "error" in res:
        label = "error"
        message = "Failed to make inference. Please try again."
    elif res["score"] >= constants.CONFIDENCE_SCORE:
        confidence_score = str(res["score"] * 100) + "%"
        label = constants.LABELS[res["label"]]
        message = (
            f"You donot have pnuemonia. The model is {confidence_score} confident in its result."
            if label == constants.LABELS["LABEL_0"]
            else f"You have pnuemonia. The model is {confidence_score} confident in its result. You might need to run more tests."
        )
        # Send message. NOTE: For now, I have used a constant phone number for message. The students later can change to input the desired number.
        sms.send_message(constants.SENDER, constants.RECEIVER, message)
        found = True
    else:
        label = "Not Detected"
        message = "Sorry! The model could not detect the result with higher confidence. You might want to run more tests."
    return render_template(
        "results.html",
        labels=label,
        old_filename=filename,
        filename=filename,
        message=message,
        found=found,
    )


@app.route("/uploads/<path:filename>")
def files(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)
