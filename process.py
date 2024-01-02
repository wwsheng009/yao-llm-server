from text2vec import SentenceModel 

import const
model = SentenceModel(const.DefaultModel)


def Embedding(txt):
    sentence = txt
    vec = model.encode(sentence)
    return vec.tolist()