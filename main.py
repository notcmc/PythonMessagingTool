import pickle
from flask import Flask, request, render_template_string, make_response
from twilio.rest import Client

app = Flask(__name__)

def load_auths_beta():
    with open("auths.pkl", "rb") as f:
        return pickle.load(f)

AUTHS = load_auths_beta()

@app.route("/")
def index():
    return "PythonMessagingTool server is up", 200

@app.route("/msgwrite", methods=["GET"])
def msgwrite():
    try:
        key = request.args.get("key")
        msg = request.args.get("msg")
        if key is None or msg is None:
            return "Invalid user input: `key` or `msg` is missing", 400
        if key not in AUTHS:
            return "Invalid user auth", 401
        sid, num_to, num_from = AUTHS[key]
        client = Client(sid, key)
        client.messages.create(
            to=num_to,
            from_=num_from,
            body=msg
        )
        return "Message accepted", 200
    except:
        return "Error", 500

if __name__ == "__main__":
    app.run(debug=True)
