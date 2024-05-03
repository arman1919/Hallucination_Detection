# LLM Hallucination Detection

This project involves analyzing text for correctness and logical coherence using various natural language processing (NLP) techniques and APIs.

## Files

### main.py

This file contains the main script for the text analysis project. Here's a brief overview of its functionality:

1. **delete_files**: A function to delete files in a specified folder path.
2. **split_text**: A function to split a text into smaller chunks with specified size and overlap.
3. **text**: A sample text for analysis.
4. **key_words**: Extracted keywords from the sample text.
5. **combined_text**: Combined text from various sources.
6. **vectorstore**: Creation of a vector store for the combined text.
7. **retriever**: Retrieval of vectors for analysis.
8. **template**: Template for the text analysis prompt.
9. **model**: Initialization of the OpenAI GPT-3.5 model.
10. **chain**: Pipeline for text analysis.
11. **answer**: Execution of the text analysis pipeline and printing the result.
12. **delete_files**: Deleting files in the specified folder after analysis.

### key_analysis.py

This file contains functions related to keyword extraction from text.

1. **extract_keywords**: Function to extract keywords from text using OpenAI's GPT-3.5 API.

### data_extraction.py

This file contains functions related to data extraction from Wikipedia.

1. **print_sections**: Function to print sections of a Wikipedia page.
2. **get_wiki_page**: Function to retrieve and save a Wikipedia page.

## Usage

To use this project:

1. Ensure you have the necessary APIs and packages installed.
2. Run `main.py` to perform text analysis.
3. Modify the input text and adjust parameters as needed for your analysis.

## Dependencies

- `langchain_community`
- `langchain_core`
- `langchain_openai`
- `openai`
- `requests`
- `json`
- `nltk`
- `wikipediaapi`