#!/usr/bin/python

import random
import json

def printFile():
    with open("words.json") as f:
        words = json.load(f)
    print json.dumps(words, indent=2)

def convert2json():
    inputFile = "lists/extracted"
    outputFile = "words.json"
    out = {}
    i = 1
    with open(inputFile) as f:
        for line in f:
            word = line.rstrip().split(":")
            out[word[0].decode('latin-1')] = { "definition": word[1].decode('latin-1'), "attempts": 0, "correct": 0, "index":i }
            i += 1

    #print json.dumps(out, indent=2)
    with open(outputFile, 'w') as f:
        json.dump(out, f)

def printWords(start, end):
    with open("words.json") as f:
        words = json.load(f)
    for i in range(start, end+1):
        if (i-1) % 10 == 0:
            print ""
        for key in words:
            if words[key]['index'] == i:
                print "%s : %s" % (key, words[key]['definition'])

def printWordInfo(start, end):
    with open("words.json") as f:
        words = json.load(f)
    for i in range(start, end+1):
        for key in words:
            if words[key]['index'] == i:
                print key + ":"
                print words[key]
                print ""

def resetList():
    with open("words.json") as f:
        words = json.load(f)
    for key in words:
        words[key]['attempts'] = 0
        words[key]['lastStatus'] = True
        words[key]['correct'] = 0
    print words

def addField():
    wordFile = "words.json"
    with open(wordFile) as f:
        words = json.load(f)

    for word in words:
        words[word]['lastStatus'] = True

    with open(wordFile, 'w') as f:
        json.dump(words, f)

printWordInfo(1,20)
