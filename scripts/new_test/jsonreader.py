import json
from pprint import pprint

def readJson(jsonstr):
  data = json.loads(jsonstr)
  return data["hypotheses"][0]["utterance"]

