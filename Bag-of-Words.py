from pyvi import ViUtils, ViTokenizer
from pyvi.ViPosTagger import ViPosTagger
from sklearn.feature_extraction.text import CountVectorizer


def Read_file():
    text = open('text.txt');
    raw = text.read();
    # print(raw);
    return raw;
def precessed_text():
    raw_pre = Read_file();

    processed_docs = str(ViUtils.remove_accents(raw_pre)).split('.');
    processed_text = [doc.lower() for doc in processed_docs]
    # print(processed_text)
    return (processed_text);
def vocabulary():
    text_pre = precessed_text();
    vocab = {}
    count = 0
    for doc in text_pre:
        for word in doc.split():
            if word not in vocab:
                count = count + 1
                vocab[word] = count
    # print(vocab)
    return vocab;

def bag_of_words():
    # look at the documents list
    text_pre = precessed_text();
    print("Our corpus: ", text_pre)

    count_vect = CountVectorizer()
    # Build a BOW representation for the corpus
    bow_rep = count_vect.fit_transform(text_pre)

    # Look at the vocabulary mapping
    print("Our vocabulary: ", count_vect.vocabulary_)

    # see the BOW rep for first 2 documents
    print("BoW representation for 'nhan vien y te': ", bow_rep[0].toarray())
    # print("BoW representation for 'man bites dog: ", bow_rep[1].toarray())
if __name__ == '__main__':
    Read_file()
    precessed_text()
    vocabulary()
    bag_of_words()