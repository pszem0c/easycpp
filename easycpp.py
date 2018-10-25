#!/usr/bin/python
import urllib.request
import json
import sys

baseUrl = "https://raw.githubusercontent.com/acharluk/easy-cpp-projects/master"

def createProject():
    try:
        res = urllib.request.urlopen("{}/templates/project/files.json".format(baseUrl)) 
        data = res.read().decode("utf-8")
        print(data)
    except:
        print("createProject: {}".format(sys.exc_info()[0]))

if __name__ == "__main__":
    createProject()
