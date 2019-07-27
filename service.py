import connexion
from flask import Flask, jsonify
from connexion.resolver import RestyResolver

from resources import definitions as defn

if __name__ == "__main__":
    app = connexion.App(__name__, specification_dir=defn.SWAGGER_DIR)
    app.add_api(defn.SWAGGER_CONF,resolver=RestyResolver('api'))
    app.run(port=defn.SERVICE_PORT)