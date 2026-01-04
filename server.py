from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/alerts/<filename>")
def serve_image(filename):
    return send_from_directory("alerts", filename)

if __name__ == "__main__":
    app.run(port=5000)

