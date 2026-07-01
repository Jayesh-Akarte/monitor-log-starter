from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')

    if log == "info":
        app.logger.info("Info button pressed")

    elif log == "warning":
        app.logger.warning("Warning button pressed")

    elif log == "error":
        app.logger.error("Error button pressed")

    elif log == "critical":
        app.logger.critical("Critical button pressed")

    return render_template(
        "index.html",
        log=log
    )