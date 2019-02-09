# twittermadlibs - Python mad libs generator using unique Twitter accounts

## Dependencies
   twittermadlibs uses the following packages and modules:

   Tweepy: for handling Twitter API calls

   pydoc3: for creating HTML documentation

   TextBlob: for handling Natural Language Processing

   Built-in Modules:
   csv: for reading from CSV files

   os: for getting absolute paths of files

   random: for making random choices

   setup.py automatically attempts to install these packages if
   you do not already have them.

## Install and Documentation
   After installing dependencies, run install.sh to install Tweetsole. For bash:

   $ sh install.sh

   To create new HTML documentation, run:

   $ sh docs.sh

## Tweetsole App

   Twittermadlibs allows you to create mad libs from any public Twitter account.
   You can see what a Kanye West, Donald Trump, or Elon Musk mad libs
   would look like.

   This app uses Tweepy to pull tweets from the Twitter API. After cleaning the
   data, twittermadlibs sorts each list by parts of speech (i.e. singular nouns,
   comparative adjectives, etc). It then chooses words to place in the mad libs,
   and returns a fully completed mad libs. 
