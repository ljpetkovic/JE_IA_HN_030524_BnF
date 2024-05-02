from keyphrase_vectorizers import KeyphraseCountVectorizer
from keybert import KeyBERT
from flair.embeddings import TransformerDocumentEmbeddings
import os

# Ensure paths are correctly set
path = '../corpus/'
input_file_name = 'corpus_autres.txt'
output_file_name = '../output/autres_kpv_5000.txt'

# Init French KeyBERT model
kw_model = KeyBERT(model=TransformerDocumentEmbeddings('google-bert/bert-base-multilingual-cased'))

# Adjust the POS pattern to be less restrictive
vectorizer = KeyphraseCountVectorizer(spacy_pipeline='fr_core_news_lg', pos_pattern='<N.*>+<ADJ.*>*', stop_words='french')

with open(os.path.join(path, input_file_name), 'r') as input_file, \
     open(os.path.join(path, output_file_name), 'w') as output_file:
    raw_data = input_file.readlines()
    start = 0
    end = 5000
    while start < len(raw_data):  # Ensure we process all data
        data = " ".join(raw_data[start:end]).replace('\n', ' ')  # Join lines and handle newlines
        start = end
        end += 5000
        try:
            # Get French keyphrases
            kp = kw_model.extract_keywords(data, vectorizer=vectorizer)
            for k in kp:
                output_file.write(str(k) + '\n')
        except ValueError as e:
            print(f"An error occurred while processing chunks starting at line {start}: {e}")
            # Optionally write a message or handle the error as needed
            # output_file.write("No keyphrases extracted for a chunk.\n")
