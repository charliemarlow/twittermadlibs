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
        self.classifiedWords = words.tags
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
        #nouns = self.getPartOfSpeech(['singularNoun', 'pluralNoun'])

        singularNoun =      self.getPOSList(self.partOfSpeechArgs['singularNoun'])
        pluralNoun =        self.getPOSList(self.partOfSpeechArgs['pluralNoun'])
        regularAdj =        self.getPOSList(self.partOfSpeechArgs['regularAdj'])
        superlativeAdj =    self.getPOSList(self.partOfSpeechArgs['superlativeAdj'])
        comparativeAdj =    self.getPOSList(self.partOfSpeechArgs['comparativeAdj'])
        presentVerb =       self.getPOSList(self.partOfSpeechArgs['presentVerb'])
        pastVerb =          self.getPOSList(self.partOfSpeechArgs['pastVerb'])
        gerundVerb =        self.getPOSList(self.partOfSpeechArgs['gerundVerb'])
        comparativeAdv =    self.getPOSList(self.partOfSpeechArgs['comparativeAdv'])
        superlativeAdv =    self.getPOSList(self.partOfSpeechArgs['superlativeAdv'])

        wordsDict = {
            'singularNoun'      : singularNoun,
            'pluralNoun'        : pluralNoun,
            'regularAdj'        : regularAdj,
            'superlativeAdj'    : superlativeAdj,
            'comparativeAdj'    : comparativeAdj,
            'presentVerb'       : presentVerb,
            'pastVerb'          : pastVerb,
            'gerundVerb'        : gerundVerb,
            'comparativeAdv'    : comparativeAdv,
            'superlativeAdv'    : superlativeAdv
        }
        # return word_dict
        return wordsDict

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
