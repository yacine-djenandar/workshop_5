from textblob import TextBlob

def extract_sentiment(text: str):
    '''Extract sentiment using textblob.
    Polarity is within range [-1, 1]'''
    print("Yaaay I edited this file")
    
    text = TextBlob(text)

    return text.sentiment.polarity
