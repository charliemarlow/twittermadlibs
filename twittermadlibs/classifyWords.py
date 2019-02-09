from textblob import TextBlob


class classifyWords:

    def __init__(self, words):
        '''
        Sets up classifyWords class
        Initializes member variable of words, every word that needs
        to be classified as adjective, noun, verb, etc.
        :param words: a TextBlob object
        '''

        # Check parameters
        if(words is None):
            print("List of words is empty")
            quit()

        self.words = words
        self.classifiedWords = self.classifyPartsOfSpeech()
        self.partOfSpeechArgs = {
            'singularNoun'      : ["NN", "NNP"],
            'pluralNoun'        : ["NNS", "NNPS"],
            'regularAdj'        : ["JJ"],
            'superlativeAdj'    : ["JJS"],
            'comparativeAdj'    : ["JJR"],
            'presentVerb'       : ["VB", "VBP", "VBZ"],
            'pastVerb'          : ["VBN", "VBD"],
            'gerundVerb'        : ["VBG"],
            'comparativeAdv'    : ["RBR"],
            'superlativeAdv'    : ["RBS"]
        }

    def createWordDictionary(self):
        '''
        Creates a dictionary of dictionaries for each
        generalized part of partsOfSpeech
        :return: a dictionary of dictionaries
        '''

        # Get dict of nouns
        nouns = self.getPartOfSpeech(['singularNoun', 'pluralNoun'])

        # Get dict of adjectives
        adjectives = self.getPartOfSpeech(['regularAdj', 'superlativeAdj', 'comparativeAdj'])

        # Get dict of verbs
        verbs = self.getPartOfSpeech(['presentVerb', 'pastVerb', 'gerundVerb'])

        # Get dict of Adverbs
        adverbs = self.getPartOfSpeech(['comparativeAdv', 'superlativeAdv'])

        # create word_dict
        partsOfSpeech = {
            'noun'          : nouns,
            'adjective'     : adjectives,
            'verb'          : verbs,
            'adverb'        : adverbs
        }

        # return word_dict
        return partsOfSpeech

    def getPartOfSpeech(self, arguments):
        '''
        Takes arguments and returns a dict of those parts of speech
        For example, if it takes ['singularNoun', 'pluralNoun']
        It return a dict with two entries: singularNoun and pluralNoun
        Each entry is a list of every singular noun and plural noun respectively

        :param arguments: a list of part of speech arguments
        :return: a dictionary of lists with an entry for each argument
        '''
        dict = {}
        for arg in arguments:
            dict[arg] = self.getPOSList(self.partOfSpeechArgs[arg])

        return dict

    def getPOSList(self, arguments):
        '''
        Gets a list of a particular part of speech

        :param arguments: a list of TextBlob parts of speech
        :return: a list of words matching the arguments
        '''

        # validate input
        if(arguments is None):
            print("Error in getPOSList: param arguments is None")
            quit()

        words = self.classifiedWords
        partsOfSpeech = []

        # for each argument, add to the list a new list of words
        # that matches the arguments POS type
        for arg in arguments:
            # get every instance of the part of speech
            argumentPOS = [word[0] for word in words if arg in word]
            # concatenate lists together
            partsOfSpeech = partsOfSpeech + argumentPOS

        return partsOfSpeech


    def classifyPartsOfSpeech(self):
        '''
        Classifies words as parts of speech
        :return: a list of tuples containing a word and part of speech
        '''
        return self.words.tags

    def classifyNounPhrases(self):
        '''
        Classifies words as noun classifyNounPhrases
        :return: a list of noun phrases
        '''
        return self.words.noun_phrases
