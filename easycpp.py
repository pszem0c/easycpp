#!/usr/bin/python
import urllib.request
import json
import sys
import os
import argparse

args = None
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
        if args.dir != None:
            folder = ""
            if os.path.isabs(args.dir):
                folder = args.dir
            else:
                folder = "{}/{}".format(os.getcwd(), args.dir)
            downloadTemplate(files, templateName, folder)
        else:
            downloadTemplate(files, templateName, os.getcwd)
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

def createClass():
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project", help="creates new project", action="store_true")
    parser.add_argument("-d", "--dir", help="directory where new project will be created", action="store", dest="dir")
    parser.add_argument("-c", "--class", help="creates class", action="store_true", dest="createClass")
    args = parser.parse_args()
    if args.project:
        print("Creating easycpp project")
        #createProject()
    elif args.createClass:
        print("Creating class")
        createClass()
