# Machine Learning -- Evasion Attacks


## Background

An Evasion Attacks refers to an attack that deceives the target system by constructing specific input samples without changing the target machine learning system. For example, an attacker can modify the non-critical characteristics of a malware sample so that it is judged as a benign sample by an anti-virus system, thereby bypassing detection. The sample specially constructed by the attacker in order to carry out Evasion Attacks is usually called the "adversarial sample". As long as a machine learning model does not learn the discriminative rules perfectly, it is possible for an attacker to construct adversarial examples to deceive the machine learning system.

The integrity of the AI model is mainly reflected in the complete and undisturbed learning and prediction process of the model, and the output results conform to the normal performance of the model. This is the basis for researchers to believe in the output of the AI model, and it is also the most vulnerable part of the AI model.

Attacks against the integrity of AI models are usually called "adversarial attacks." Adversarial attacks are usually divided into two categories, one is Evasion Attacks from the model, and the other is the data poisoning attack from the data.

## Usage

### 1.py
As an attacker, we have obtained the model waf/trained_waf_model for detection, and can access the serialized scikit-learn pipeline object, and can check each stage of the model pipeline.

First, we load the trained model, and then use python's built-in vars() to view the steps included in the pipeline.


### 2.py
By the output of 1.py, you can see that the pipeline object has two steps, one is TfidfVectorizer and the other is LogisticRegression classifier.

We specify a typical xss payload to test whether the model works.

### 3.py
First, you need to find a specific string token that can help maximize the impact of the classifier.

We check the token vocabulary of the vectorizer by observing the vocabulary attributes

### 4.py
As can be seen from the running results of 3.py, each token is associated with a specific weight, and these weights will be fed to the classifier as a feature of a single document.

The coefficients of the trained LogisticRegression classifier can be accessed through the coef_ attribute. We print out these two arrays and try to understand their meaning.

### 5.py
As a result, the weight of each item of IDF and the LogisticRegression coefficient are printed separately, and their product can determine the degree of influence of each item on the overall predicted probability. We multiply it and print it in the code below

### 6.py
Next, we sort each item according to the confidence level. Here we use numpy.argpartition() to sort and convert the value to the index of vec.idf_, so that we can get from the vectorizer's token dictionary (which is the previously printed vec.vocabulary_) found the corresponding token string. Then print out the sorted results

### 7.py
It can be seen that the token at the index of 81937 has the greatest positive impact on the confidence of the prediction (the more this string appears, the more likely the corresponding payload will be determined to be 0, that is, the payload of a non-xss attack), then We extract the token corresponding to this index from the token dictionary

### 8.py
Will adding this token to the previously tested payload cause the discriminator to judge it as 0.

From the results, we can see that the model still considers the payload added with "t/s" to be an xss attack, but in the second line you can see that the confidence level of xss at this time is 0.9999816, which is lower than the previous one. It shows that actually adding "t/s" could lower the confidence level.

### 9.py
We continue to add "t/s" to the payload. After adding 258 times of "t/s" to the payload, the model finally judged it as 0, that is, it is not an xss attack. From the confidence level, it can also be seen that the confidence level of xss is less than 0.5

### 10.py
Further print out the character string at this time. Although the payload at this time has t/s, if we manually judge it, we will still think that this is an effective xss attack. In other words, this payload is indeed effective, but it escapes the detection of the model. This payload is what we mentioned earlier Adversarial sample.
