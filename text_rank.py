from preprocessing import process_text, process_after
# from preprocessing import processed_text
import numpy as np
# from nltk.corpus import brown
from nltk.cluster.util import cosine_distance
from operator import itemgetter
# from test import summary_list


def pagerank(A, eps=0.0001, d=0.85, max_iter=1000):
    P = np.ones(len(A)) / len(A)
    iter_count = 0
    while iter_count < max_iter:
        new_P = np.ones(len(A)) * (1 - d) / len(A) + d * A.T.dot(P)
        delta = abs(new_P - P).sum()
        if delta <= eps:
            return new_P
        P = new_P
        iter_count += 1
    print("Warning: PageRank algorithm did not converge within {} iterations.".format(max_iter))
    return new_P

def build_similarity_matrix(sentences):
    S = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue

            S[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2])

    # Normalize the rows to ensure no division by zero
    for idx in range(len(S)):
        row_sum = S[idx].sum()
        if row_sum != 0:
            S[idx] /= row_sum

    return S

def sentence_similarity(sent1, sent2):
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for w in sent1:
        vector1[all_words.index(w)] += 1

    for w in sent2:
        vector2[all_words.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)

from operator import itemgetter



def textrank(sentences, top_n=3):
    S = build_similarity_matrix(sentences)
    sentence_ranks = pagerank(S)

    # Sort the sentence ranks
    ranked_sentence_indexes = [item[0] for item in sorted(enumerate(sentence_ranks), key=lambda item: -item[1])]
    selected_sentences = sorted(ranked_sentence_indexes[:top_n])
    # print(itemgetter(*selected_sentences)(sentences))
    summary = itemgetter(*selected_sentences)(sentences)
    return summary

sentences = []
text_rank_sum = []  # Initialize an empty list to store word counts

# for text in processed_text:
#     sentences.append(process_after(textrank(text)))

# for sentence in sentences:
#     word_count = len(sentence.split())  # Count the number of words in the sentence
#     text_rank_sum.append(word_count)  # Append the word count to the list

# # Print or further process the word_counts list
# print(text_rank_sum)

# count = 0
# for sentence in sentences:
#     print(sentence)
#     count += 1
# print("-----------------------------------")





