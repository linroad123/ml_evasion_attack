import pickle
import numpy as np
p = pickle.load(open('waf/trained_waf_model', 'rb'))
a = vars(p)
print(a)