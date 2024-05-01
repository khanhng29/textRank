import gensim
import re
import gensim.models.keyedvectors as word2vec
w2v_model = word2vec.KeyedVectors.load('./w2v/w2v.model')

vocabulary = []
for word in w2v_model.key_to_index.keys():
    vocabulary.append(word)
print(len(vocabulary))
