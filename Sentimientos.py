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

    # Print the sentiment
    st.write("Sentiment:", sentiment)

    # Display the polarity and subjectivity of the text
    st.write("Polarity:", sentiment.polarity)
    st.write("Subjectivity:", sentiment.subjectivity)
