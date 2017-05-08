import base64, json

from flask import Flask, jsonify, request

app = Flask(__name__)
application = app

@app.route("/")
def index():
    return "Docker Authz Plugin"

@app.route("/Plugin.Activate", methods=['POST'])
def activate():
    return jsonify({'Implements': ['authz']})

@app.route("/AuthZPlugin.AuthZReq", methods=['POST'])
def authz_request():
    print("AuthZ Request")
    print(request.data)

    plugin_request = json.loads(request.data)

    if 'RequestBody' in plugin_request:
        encoded_docker_request = plugin_request['RequestBody']
        docker_request = json.loads(base64.b64decode(encoded_docker_request))

        if docker_request['HostConfig']['Privileged'] != True:
            response = {"Allow": True,
                        "Msg":   "The request authorization succeeded."}
        else:
            response = {"Allow": False,
                        "Msg":   "The request authorization failed. THOU SHALT NOT SCHEDULE PRIVILEGED CONTAINERS",
                        "Err":   "Nope,no privileged containers."}
    else:
        response = {"Allow": True,
                      "Msg":   "The request authorization succeeded."}

    return jsonify(**response)

@app.route("/AuthZPlugin.AuthZRes", methods=['POST'])
def authz_response():
    print("AuthZ Response")
    response = {"Allow": True}
    return jsonify(**response)

if __name__ == "__main__":
    app.run()
