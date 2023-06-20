import streamlit as st
from textblob import TextBlob

# Title of the app
st.title("Sentiment Analysis App")

# Text area for user input
text = st.text_area("Enter your text here:")

# Button to analyze the sentiment
if st.button("Analyze Sentiment"):
    # Create a TextBlob object from the user input
    blob = TextBlob(text)

    # Get the sentiment of the text
    sentiment = blob.sentiment

    # Check if the sentiment is positive or negative
    if sentiment.polarity > 0:
        sentiment_text = "Positive"
    elif sentiment.polarity < 0:
        sentiment_text = "Negative"
    else:
        sentiment_text = "Neutral"

    # Print the sentiment
    st.write("Sentiment:", sentiment_text)

    # Display the polarity and subjectivity of the text
    st.write("Polarity:", sentiment.polarity)
    st.write("Subjectivity:", sentiment.subjectivity)
