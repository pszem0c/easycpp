#!/usr/bin/python
import urllib.request
import json
import sys
import os

baseUrl = "https://raw.githubusercontent.com/pszem0c/easycpp/master"

def createProject():
    try:
        res = urllib.request.urlopen("{}/templates/project/files.json".format(baseUrl)) 
        data = json.loads(res.read().decode("utf-8"))
        templates = list(data["templates"].keys())
        selected = 0 # other templates?
        selectedTemplate = templates[0]
        selectFolderAndDownload(data, selectedTemplate)
    except:
        print("createProject: {}".format(sys.exc_info()[0]))

def selectFolderAndDownload(files, templateName):
    try:
        # other dirs?
        downloadTemplate(files, templateName, os.getcwd())
    except:
        print("folder and download: {}".format(sys.exc_info()[0]))

def downloadTemplate(files, templateName, folder):
    try:
        for directory in files["directories"]:
            os.mkdir("{}/{}".format(folder, directory))
        for f in files["templates"][templateName]:
            res = urllib.request.urlopen("{}/templates/project/{}".format(baseUrl, f))
            open("{}/{}".format(folder, files["templates"][templateName][f]), "wb").write(res.read())
    except:
        print(" download: {}".format(sys.exc_info()[0]))

if __name__ == "__main__":
    createProject()
