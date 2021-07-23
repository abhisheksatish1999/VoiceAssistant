from keras.preprocessing.text import Tokenizer
import gensim
from gensim.models import FastText
from gensim.test.utils import get_tmpfile
import numpy as np
import pandas as pd
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import re
import time
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
from nltk import WordPunctTokenizer

import wikipedia
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


class fasttext_QA:
    def __init__(self):
        self.dataset_dir='dataset/final_dataset.csv'
        self.model_dir='models/fasttext.model'
        self.sent_embedd_dir='models/embed/sent_embeddings.npy'
        self.embedding_size = 60
        self.window_size = 40
        self.min_word = 5
        self.down_sampling = 1e-2

    def load_model(self):
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('stopwords')
        #fname = get_tmpfile(self.model_dir)
        try:
            self.model = FastText.load(self.model_dir)
            print("----------------->>loaded_model<<-----------------")
        except Exception as E:
            print(E)
            print("----------------->>Start Training<<---------------")
            '''python = wikipedia.page("Python programming language").content

            artificial_intelligence = wikipedia.page("Artificial Intelligence").content
            deep_learning = wikipedia.page("Deep Learning").content
            neural_network = wikipedia.page("Neural Network").content
            data_structure = wikipedia.page("Data structure").content
            sorting = wikipedia.page("Sorting algorithm").content
            oop = wikipedia.page("Object-oriented programming").content
            pp = wikipedia.page("List of Python software").content
            algorithm = wikipedia.page("Algorithm").content
            maths1 = wikipedia.page("Euclidean algorithm").content
            maths2 = wikipedia.page("Greatest common divisor").content
            searching = wikipedia.page("Search algorithm").content
            extraword = "hcf and gcd are the same mathematical function, www stands for world wide web which is biggest network"
            print(('hcf' in maths1.split()))

            python = sent_tokenize(python)
            artificial_intelligence = sent_tokenize(artificial_intelligence)
            deep_learning = sent_tokenize(deep_learning)
            neural_network = sent_tokenize(neural_network)
            data_structure = sent_tokenize(data_structure)
            sorting = sent_tokenize(sorting)
            oop = sent_tokenize(oop)
            pp = sent_tokenize(pp)
            algorithm = sent_tokenize(algorithm)
            maths1 = sent_tokenize(maths1)
            maths2 = sent_tokenize(maths2)
            searching = sent_tokenize(searching)
            extraword = sent_tokenize(extraword)

            python.extend(artificial_intelligence)
            python.extend(deep_learning)
            python.extend(neural_network)
            python.extend(data_structure)
            python.extend(sorting)
            python.extend(oop)
            python.extend(pp)
            python.extend(algorithm)
            python.extend(maths1)
            python.extend(maths2)
            python.extend(searching)
            python.extend(extraword)

            final_corpus = [preprocess_text(sentence) for sentence in python if sentence.strip() != ""]
            word_punctuation_tokenizer = nltk.WordPunctTokenizer()
            word_tokenized_corpus = [word_punctuation_tokenizer.tokenize(sent) for sent in final_corpus]

            %%time
            ft_model = FastText(word_tokenized_corpus,
                                size=embedding_size,
                                window=window_size,
                                min_count=min_word,
                                sample=down_sampling,
                                sg=1,
                                iter=100)

            fname = get_tmpfile("/models/fasttext.model")
            ft_model.save(fname)
            print("------------->>Training Finished<<-----------------")
            print("Saved Model")
            self.model=ft_model'''


    def preprocess_text(self,document, min_length=2):
        en_stop = set(nltk.corpus.stopwords.words('english'))
        stemmer = WordNetLemmatizer()

        # Remove all special characters
        document = re.sub(r'\W', ' ', str(document))
        # Remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
        # Remove all single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
        # substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)
        # removing prefixed 'b'
        document = re.sub(r'^b\s+', '', document)
        # converting to lowercase
        document = document.lower()
        # lemmatization
        tokens = document.split()
        tokens = [stemmer.lemmatize(words) for words in tokens]
        tokens = [words for words in tokens if words not in en_stop]
        tokens = [word for word in tokens if len(word) > min_length]

        preprocessed_text = ' '.join(tokens)
        return preprocessed_text

    def get_answer(self,query):
        df = pd.read_csv(self.dataset_dir, encoding='unicode_escape')
        df.columns = ["questions", "answer"]
        sentence_embeddings = np.load(self.sent_embedd_dir, allow_pickle=True)

        user_q = self.preprocess_text(query, min_length=2)
        query_embedding = [self.model.wv[each] for each in user_q.split()]
        query_embedding = np.array(query_embedding).mean(axis=0)

        return self.retrieveAndprintFAQAnswer(query_embedding, sentence_embeddings, df, query)

    def retrieveAndprintFAQAnswer(self,question_embedding, sentence_embeddings, FAQdf, question):
        max_sim = -1
        index_sim = -1
        for index, faq_embedding in enumerate(sentence_embeddings):
            # print(FAQdf.iloc[index, 0])
            # print(faq_embedding)
            sim = cosine_similarity(faq_embedding.reshape(1, -1), question_embedding.reshape(1, -1))[0][0];
            # sim = cosine_similarity(faq_embedding, question_embedding)[0][0]
            # print(index,sim,self.sentences[index])
            if sim > max_sim:
                max_sim = sim
                index_sim = index
        # print("\n")
        print("question:", question)
        # print("\n")
        print("Score : ",max_sim)
        print("Retrieved: ", FAQdf.iloc[index_sim, 0])
        str1 = FAQdf.iloc[index_sim, 1]
        print(str1)
        if ("\n" in str1):
            x = str1.replace("\n", "<br />")
            return x
        else:
            return str1





if __name__ == "__main__":
    obj=fasttext_QA()
    obj.load_model()
    print(obj.get_answer("factorial program"))
    #time.sleep(3)
    #print(obj.get_answer("program for factorial"))
