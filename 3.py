import pickle
import numpy as np
p = pickle.load(open('waf/trained_waf_model', 'rb'))
payload = "<script>alert(1)</script>"
a = p.predict([payload])[0]
b = p.predict_proba([payload])[0]
print(a)
print(b)