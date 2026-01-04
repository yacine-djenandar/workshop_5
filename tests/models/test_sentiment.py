from textblob import TextBlob
import pytest
from src.models.sentiment import extract_sentiment
import csv

# testdata =["Borussia Dortmund’s loss was heartbreaking as they failed to gain momentums from their  two goals advance. Very disappointing results for our Algerian player Bensebaini."
#            , "Barcelona played brilliantly last Wednesday. Rafinia’s hat-trick was pure magic. Visca Barça!"]

testdata = []
with open('/home/yacine/python/workshop_5/workshop_5/data/soccer_sentiment_analysis.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        testdata.append(row)

testdata.append(["I really like sunny weather!"])

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):

    neg_sentiment = extract_sentiment(sample[0])

    assert neg_sentiment <= 0