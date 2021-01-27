import pickle
import numpy as np
p = pickle.load(open('waf/trained_waf_model', 'rb'))
vars(p)
vec = p.steps[0][1]
clf = p.steps[1][1]
term_influence = vec.idf_ * clf.coef_
term_idx = np.argpartition(term_influence,1)[0][0]
vocab = dict([(v,k) for k,v in vec.vocabulary_.items()])
term_idx = np.argpartition(term_influence, 1)[0][0]
print(vocab[term_idx])