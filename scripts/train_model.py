import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Wczytaj przetworzone dane z CSV
data = pd.read_csv('data/emails_processed.csv')

# Sprawdź kilka pierwszych wierszy, aby upewnić się, że dane zostały wczytane poprawnie
print(data.head())

# Zakładamy, że w kolumnie 'message_cleaned' mamy tekst e-maili, a w 'label' etykiety (0 - nie phishing, 1 - phishing)
X = data['message_cleaned']  # Przetworzone e-maile
y = data['label']  # Etykiety

# Podziel dane na zbiory treningowy i testowy (80% trening, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Wyświetl rozmiar zbiorów treningowego i testowego
print(f'Rozmiar zbioru treningowego: {len(X_train)}')
print(f'Rozmiar zbioru testowego: {len(X_test)}')

# Inicjalizacja CountVectorizer
vectorizer = CountVectorizer()

# Dopasowanie vectorizera do zbioru treningowego i przekształcenie tekstu na liczby
X_train_vec = vectorizer.fit_transform(X_train)

# Przekształcenie zbioru testowego za pomocą tego samego vectorizera
X_test_vec = vectorizer.transform(X_test)

# Inicjalizacja modelu Naive Bayes
model = MultinomialNB()

# Trenowanie modelu na danych treningowych
model.fit(X_train_vec, y_train)

# Predykcja na zbiorze testowym
y_pred = model.predict(X_test_vec)

# Wyświetlenie dokładności modelu
accuracy = accuracy_score(y_test, y_pred)
print(f'Dokładność modelu: {accuracy * 100:.2f}%')

# Wyświetlenie szczegółowego raportu klasyfikacji
print(classification_report(y_test, y_pred))
