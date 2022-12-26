from flask_api import FlaskAPI
from random import randrange
import socket
import platform
import os
import netifaces as ni

app = FlaskAPI(__name__)


@app.route('/')
def test():
    return('<a href="./random">random</a><br><a href="./host">host</a>')


@app.route('/random')
def rando():
    return {'Random Number': randrange(1000000000000)}


@app.route('/host')
def hostinfo():
    docker = os.path.isfile('/.dockerenv')
    k8s = os.path.isdir('/var/run/secrets/kubernetes.io')
    if k8s:
        with open('/var/run/secrets/kubernetes.io/serviceaccount/namespace') as f:
            namespace = f.readlines()
    else:
        namespace = 'N/A'
        
    uname = platform.uname()
    network = [ni.ifaddresses(i) for i in ni.interfaces()]
    return {'Socket Hostname': socket.gethostname(),
            'Arch': platform.architecture(),
            'uname': uname,
            'docker': docker,
            'k8s': k8s,
            'kube namespace': namespace,
            'network': network,
            }


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
