Custom Chatbot for Website Data Extraction and QnA

Overview

This project is a custom chatbot designed to extract data from a website and provide intelligent Question and Answer (QnA) capabilities. The chatbot leverages LangChain for managing conversational AI, Hugging Face embeddings for text processing, and FAISS for efficient vector storage and retrieval. The backend is built using Flask, and a basic HTML interface is used for testing the chatbot.

Features

Website Data Extraction: Scrapes relevant data from target websites.

Natural Language Processing (NLP): Processes and understands user queries.

Interactive QnA System: Provides responses based on extracted data.

Flask Backend: Manages chatbot requests and responses.

Basic HTML UI: A simple interface for testing chatbot functionality.

FAISS Vector Storage: Efficient search and retrieval of vectorized data.

LangChain Integration: Manages conversational AI workflows.

Hugging Face Embeddings: Provides high-quality vector representations for text.

Technologies Used

Python

Flask (Backend API)

LangChain (Conversational AI Management)

Hugging Face Transformers (Embeddings)

FAISS (Vector Storage and Retrieval)

BeautifulSoup & Scrapy (Web Scraping)

SQLite/PostgreSQL (Data Storage)

Basic HTML/CSS (Frontend UI for Testing)

Implementation

Web Scraping & Data Extraction:

Identify target website structure

Extract relevant text and data fields

Store extracted data in a structured format

NLP Processing & Question Answering:

Preprocess extracted text (tokenization, stopword removal, stemming/lemmatization)

Convert text into embeddings using Hugging Face models

Store embeddings in FAISS for efficient retrieval

Implement LangChain to manage chatbot responses

Backend API Development:

Develop REST API using Flask to handle chatbot requests

Integrate FAISS and LangChain for real-time QnA processing

Frontend Interface:

Develop a basic HTML interface for chatbot interaction

Display chatbot responses dynamically

How to Run

Prerequisites

Ensure you have Python 3.8+ installed along with required dependencies.

Installation

pip install -r requirements.txt

Running the API

python app.py

Accessing the Web Interface

Open index.html in a web browser to interact with the chatbot.

Future Enhancements

Support for multiple websites

Integration with external APIs for additional data sources

Improved response generation using large language models

Deploy as a cloud-based service with an enhanced UI

Contributors

Devam Singh

License

This project is open-source and available under the MIT License.

