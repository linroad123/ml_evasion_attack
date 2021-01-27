import pickle
import numpy as np
p = pickle.load(open('waf/trained_waf_model', 'rb'))
vars(p)
vec = p.steps[0][1]
clf = p.steps[1][1]
term_influence = vec.idf_ * clf.coef_
print(term_influence)