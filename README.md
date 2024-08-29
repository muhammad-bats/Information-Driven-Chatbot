# Bats Chatbot

--- 

Bats is a simple information driven chatbot that can engage in basic conversations with users, answering greetings, hospitality queries, and expressions of thanks. It can also attempt to respond to general queries using a provided text dataset.

## Features

- **Greetings**: Responds to common greetings such as "hello", "hi", etc.
- **Hospitality**: Responds to phrases like "how are you", "how you doing", etc.
- **Thanks**: Responds to expressions of gratitude such as "thank you", "thanks", etc.
- **General Queries**: Attempts to respond to user queries by analyzing a given text dataset using TF-IDF and cosine similarity.

## Pre-Requisites

The chatbot uses the following Python libraries:

- `python version: 3.10.14`
- `random`
- `string`
- `requests: 2.32.3`
- `numpy: 1.26.4`
- `scikit-learn: 1.5.1`
- `nltk: 3.8.1`

You can install the necessary packages using pip:

```bash
pip install requests numpy scikit-learn nltk
```

## Code Explanation

### 1. Downloading the Data

The python script allows the user to specifiy which text dataset to use for the chatbot, it allows the user to download and encode a new file from the web or use an existing text file for the dataset.

The `get_file` function takes a URL as input, downloads the PDF file from the provided URL, and saves it to the local file system. The user is prompted to enter the desired file name for saving the PDF. If the download is successful, the file is saved with the specified name; otherwise, an error message is displayed.

### 2. Pre-Defined Responses

The chatbot is designed to recognize certain user-inputs and respond with pre-defined outputs. These include *Greetings*, *Hospitality* and *Gratitude* inputs. The code includes lists of examples of user inputs and pre-defined responses for these intents. 

The `greeting` function checks if the user's input matches any greeting keywords. If it does, it returns a random greeting response.

The `hospitality` function checks if the user's input matches any hospitality keywords. If it does, it returns a random hospitality response.

The `thanks` function checks if the user's input matches any gratitude keywords. If it does, it returns a random gratitude response.

### 3. Text Processing

The text from the dataset is tokenzied and lemmatized.

The `sent_tokenzie` function tokenizes the text into a list of sentences

The `word_tokenzie` function tokenizes the text into a list of words

The `LemTokens` function applies lemmatization to each token in the list of words 

The `LemNormalize` normalizes text by converting it to lowercase, removing punctuation, tokenizing it, and then lemmatizing the tokens.

### 4. Response Generation

The `respponse` function generates a response by comparing the user's input with the dataset using TF-IDF and cosine similarity. It adds the user's input to the list of sentence tokens, computes the TF-IDF matrix, and finds the most similar sentence in the dataset.

### Main Loop 

The chatbot prompts the user to either download a new dataset or use an existing one.

If the chatbot is activated, it starts a loop where it interacts with the user, responding to inputs until the user types *Bye*.

The chatbot handles greetings, hospitality queries, expressions of thanks, and general queries using the provided dataset.

## How to use

1. Run the script: Start the chatbot by running the script in your Python environment.
2. Choose the Dataset: Choose whether to download a new dataset or use an existing one.
3. Interact: Engage with the chatbot by typing your queries.
4. Exit: Type "Bye" to end the conversation.

``` Example
Chatbot online
Use new data? yes
Enter url: http://example.com/document.txt
Enter file name you want example_text
File downloaded successfully
Activate Bats? yes
Activating Bats
Bats: Hello, I am Bats and I will answer your queries. If you wish to exit, type Bye!
bye
Bats: Bye
Deactivating Bats
``` 

## Notes

- Comment out `nltk.download('punkt')` and `nltk.download('wordnet')` after the first run to avoid re-downloading the datasets.
- To activate the chatbot, user input has to be '*yes*' for the script to run.
- Dataset file must be a text document

  ---
