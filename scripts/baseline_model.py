import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Wczytaj dane
train_df = pd.read_csv('data/train.csv')
test_df = pd.read_csv('data/test.csv')

# Wektoryzacja tekstu
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(train_df['email'])
X_test_vec = vectorizer.transform(test_df['email'])


# Trenowanie modelu
model = LogisticRegression()
model.fit(X_train_vec, train_df['label'])

# Predykcja
y_pred = model.predict(X_test_vec)

# Ewaluacja
print(classification_report(test_df['label'], y_pred))
