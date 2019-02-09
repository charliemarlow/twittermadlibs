# Create docs
pydoc3 -w twittermadlibs
pydoc3 -w twittermadlibs.classifyWords
pydoc3 -w twittermadlibs.madlib
pydoc3 -w twittermadlibs.pullTweets
pydoc3 -w twittermadlibs.unique

# Move to docs folder
mv twittermadlibs.html                docs/twittermadlibs.html
mv twittermadlibs.classifyWords.html  docs/twittermadlibs.classifyWords.html
mv twittermadlibs.madlib.html        docs/twittermadlibs.madlib.html
mv twittermadlibs.pullTweets.html     docs/twittermadlibs.pullTweets.html
mv twittermadlibs.unique.html         docs/twittermadlibs.unique.html
