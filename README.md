#Python Project for Data Science

## Project Overview
A Python program to gather data from Twitter, perform sentiment analysis and then make stock price predictions.

The first step is gathering Twitter data based on a specific query. Both the REST and Streaming API's from Twitter are available for use. Next, the user must select either Python NLTK or SimpleSentiPy for sentiment analysis. Following that, the data is run through a concept extraction function that pulls relevant named entities using SpaCy's NER tagger. These NER-tagged words and phrases get run run through a handler that gathers tweets on them, performs sentiment analysis on them, and finally extracts concepts from them.

Following concept extraction of related concepts, the Swi Method gets performed. The Swi Method is an way of determining how a concept affects the original query (either positively or negatively), as well as by how much. It returns an adjustment score that is applied to all observed sentiment scores before predictions are made. Currently, the system makes predictions based on the following models: ARIMA, Linear Regression, Bayesian Ridge Regression, Logistic Regression, Lasso Regression, Decision Tree Regression, Decision Tree Classification, Ridge Regression, and the Perceptron model.

### Dependencies
See DEPENDENCIES file.

