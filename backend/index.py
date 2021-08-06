from subprocess import Popen, TimeoutExpired, PIPE
from flask import Flask, render_template, jsonify, abort, request
import os

app = Flask(__name__, static_folder="../dist/static", template_folder="../dist")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")

@app.route("/api/v0.0.1/lsblk")
def lsblk():
    result = os.popen("lsblk --json").read()
    return result

@app.route("/api/v0.0.1/format", methods=["POST"])
def format():
    result = os.popen(". /legacy/format_ext4.sh").read()
    return result

# хотелось бы template literal, а не подсовывать bash.
#
# @app.route("/api/v0.0.1/args", methods=["POST"])
# def args():
#     fs = "ext4"
#     args = "--fs"
#     result = os.popen(F"mkfs.{fs} {args}").read()
#     return result

@app.route("/api/v0.0.1/mount", methods=["POST"])
def mount():
    result = os.popen("mount ${deviceFile} ${destinationDirectory}").read()
    return result

@app.route("/api/v0.0.1/unmount", methods=["POST"])
def unmount():
    result = os.popen("umount ${deviceFile}").read()
    return result

@app.route("/api/v0.0.1/args")
def args():
    args = "--fs"
    result = os.popen(F"lsblk {args}").read()
    return result

#
# Обработчики ошибок
################################################################################


@app.errorhandler(400)
def bad_request(error):
    return jsonify(success=False, message=error.description), 400


@app.errorhandler(500)
def server_error(error):
    return jsonify(success=False, message=error.description), 500
