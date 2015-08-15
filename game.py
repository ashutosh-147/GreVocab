#!/usr/bin/python

import random
import json

gameType = 1

class Vocab:

    def __init__(self):
        self.wordFile = "words.json"
        self.start = 1
        self.end = 600
        self.numGames = 10
        self.numChoices = 5
        self.game = 4

        self.words = {}
        with open(self.wordFile) as f:
            self.words = json.load(f)

        self.wordList = {}
        totalAttempts = 0
        totalCorrect = 0
        wordsAttempted = 0
        for key in self.words:
            if self.start <= self.words[key]['index'] <= self.end:
                self.wordList[key] = self.words[key]
                totalAttempts += self.words[key]['attempts']
                totalCorrect += self.words[key]['correct']
                if self.words[key]['attempts'] > 0:
                    wordsAttempted += 1

        print "Total words: %d" % (len(self.wordList))
        print "Total attempts: %d" % (totalAttempts)
        print "Total correct: %d" % (totalCorrect)
        print "Total words Attemped: %d" % (wordsAttempted)
        
        avgAttempts = float(totalAttempts) / len(self.wordList)
        
        print "Average attempts: %f" % (avgAttempts) 
        
        self.chosenWords = []
        for key in self.wordList:
            if len(self.chosenWords) >= self.numGames:
                break
            if self.wordList[key]['lastStatus'] == False:
                self.chosenWords.append(key)
        for key in self.wordList:
            if len(self.chosenWords) >= self.numGames:
                break
            if self.wordList[key]['attempts'] == 0:
                self.chosenWords.append(key)


        for key in self.wordList:
            if len(self.chosenWords) >= self.numGames:
                break
            if self.wordList[key]['attempts'] < avgAttempts:
                self.chosenWords.append(key)

        while len(self.chosenWords) < self.numGames:
            randWord = random.choice(self.wordList.keys())
            if randWord not in self.chosenWords:
                self.chosenWords.append(randWord)
        
        random.shuffle(self.chosenWords)

        question = 0
        for word in self.chosenWords:
            question += 1
            print ""
            print "Question %d of %d:" % (question, self.numGames)
            answer = self.playGame(word)
            self.checkAnswer(word, answer)

        with open(self.wordFile, 'w') as f:
            json.dump(self.words, f)

            

    def playGame(self, word):
        if self.game == 1:
            return self.game1(word)
        elif self.game == 2:
            return self.game2(word)
        elif self.game == 3:
            return self.game3(word)
        else:
            return self.game4(word)

    def game1(self, word):
        definitions = []
        definitions.append(self.wordList[word]['definition'])
        
        while len(definitions) < self.numChoices:
            definition = self.wordList[random.choice(self.wordList.keys())]['definition']
            if definition not in definitions:
                definitions.append(definition)
        
        random.shuffle(definitions)
        answer = definitions.index(self.wordList[word]['definition'])
        
        print "Word: " + word
        print ""
        for i in range(len(definitions)):
            print "%d: %s" % (i+1, definitions[i])
        print ""
        return answer

    def game2(self, word):
        words = []
        words.append(word)
        while len(words) < self.numChoices:
            randWord = random.choice(self.wordList.keys())
            if randWord not in words:
                words.append(randWord)
            
        random.shuffle(words)
        answer = words.index(word)
        
        print "Definition: " + self.wordList[word]['definition']
        print ""
        for i in range(len(words)):
            print "%d: %s" % (i+1, words[i])
        print ""
        return answer

    def game3(self, word):
        if random.randint(1,2) == 1:
            return self.game1(word)
        else:
            return self.game2(word)

    def game4(self, word):
        print word
        raw_input("")
        print self.words[word]['definition']

        return 0

    def getUserInput(self):
        userInput = raw_input("Your answer: ")
        try:
            userIntInput = int(userInput)
            if 1 <= userIntInput <= self.numChoices:
                return userIntInput-1
            else:
                raise
        except:
            print "please give number between 1 and %d" % (self.numChoices)
            return self.getUserInput()

    def checkAnswer(self, word, answer):
        if self.getUserInput() == answer:
            self.updateWord(word, True)
            print "Correct!"
        else:
            self.updateWord(word, False)
            print "Incorrect. Correct Answer is:"
            print "%s - %s" % (word, self.wordList[word]['definition'])
            raw_input("")

    def updateWord(self, word, correct):
        self.words[word]['attempts'] += 1
        if correct:
            self.words[word]['correct'] += 1
        self.words[word]['lastStatus'] = correct

Vocab()

def game1():
    wordList = loadWordList()
    chosenWord = random.choice(wordList.keys())
    definitions = []
    definitions.append(wordList[chosenWord]['definition'])

    while len(definitions) < 5:
        definition = wordList[random.choice(wordList.keys())]['definition']
        if definition not in definitions:
            definitions.append(definition)
    random.shuffle(definitions)

    print ""
    print "Word: " + chosenWord
    print ""
    for i in range(len(definitions)):
        print "%d: %s" % (i+1, definitions[i])
    print ""
    userAnswer = raw_input("Your answer: ")

    if int(userAnswer)-1 == definitions.index(wordList[chosenWord]['definition']):
        print "Correct!"
    else:
        print "Incorrect. The actual definition is:"
        print wordList[chosenWord]['definition']
        raw_input("")

def game2():
    wordList = loadWordList()
    chosenWord = random.choice(wordList.keys())
    definition = wordList[chosenWord]['definition']

    choices = []
    choices.append(chosenWord)
    while len(choices) < 5:
        randomWord = random.choice(wordList.keys())
        if randomWord not in choices:
            choices.append(randomWord)
    random.shuffle(choices)

    print ""
    print "Definition: " + definition
    print ""
    for i in range(len(choices)):
        print "%d: %s" % (i+1, choices[i])
    print ""
    userAnswer = raw_input("Your answer: ")

    if int(userAnswer)-1 == choices.index(chosenWord):
        print "Correct!"
    else:
        print "Incorrect. The actual word was: " + chosenWord
        raw_input("")
