from newspaper import Article
import nltk
from gtts import gTTS
import os

# BBC News: Coronavirus: How can AI help fight the pandemic?
url = 'https://www.bbc.com/news/technology-51851292'

# Getting the article text using newspaper3k library
article = Article(url)
article.download()
article.parse()
nltk.download('punkt')

# Applying NLP
article.nlp()

# Storing the text of the article in article_text
article_text = article.text[:250]

print("First 250 character of the article: \n", article_text)

# Selecting the Article's Language
article_language = 'en' #English

# Applying Google Text-to-Speech
text_to_speech = gTTS(text=article_text, lang=article_language, slow=False)

# Saving the audio file
text_to_speech.save("text_to_speech_article.mp3")

# Playing the converted file
os.system("start text_to_speech_article.mp3")