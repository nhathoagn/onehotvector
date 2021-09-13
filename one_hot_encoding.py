from pyvi import ViUtils, ViTokenizer
from pyvi.ViPosTagger import ViPosTagger


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

def get_onehot_vector(somestring):
    vocabb = vocabulary();
    onehot_encoded = []
    for word in somestring.split():
        temp = [0]*len(vocabb)
        if word in vocabb:
            temp[vocabb[word]-1] = 1 # -1 is to take care of the fact indexing in array starts from 0 and not 1
        onehot_encoded.append(temp)
    print(onehot_encoded)

    return onehot_encoded
if __name__ == '__main__':
    Read_file()
    precessed_text()
    vocabulary()
    get_onehot_vector("nhan vien y te")