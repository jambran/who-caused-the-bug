import json
import os
import sys
import random
import datetime
from flask import Flask, request, jsonify, make_response
import matplotlib.pyplot as plt

app = Flask(__name__)


def get_df_intent(req):
    """Returns the intent name as defined in the DialogFlow app"""
    return req.get('queryResult').get('intent').get('displayName')


def get_df_utterance(req):
    """
    original user utterance
    :param req: request object from DF
    :return: string, user utterance
    """
    return req.get('originalDetectIntentRequest') \
        .get('payload') \
        .get('inputs')[0] \
        .get('rawInputs')[0] \
        .get('query')

def make_graph():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", '8080')))
