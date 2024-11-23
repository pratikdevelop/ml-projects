from textblob import TextBlob 
from nltk.corpus import stopwords
from newspaper import Article
url = 'https://www.lovetoknow.com/life/wellness/what-are-most-stressful-life-events'
article = Article(url)
article.download()
article.parse()
text = article.text
blob = TextBlob(text)
# blob.sentiment.polarity
print(blob.sentiment.polarity)
