import json
import sys
from pprint import pprint 

def print_json(path, obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            print_json(path + "/" + k, v)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            print_json(path + "[%d]" % i, v)
    else:
        print(path, str(obj))

obj = json.load(sys.stdin)
print_json("", obj)
