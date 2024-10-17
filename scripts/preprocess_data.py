import pandas as pd
import re

# Ścieżka do pliku CSV z danymi
csv_file = 'data/emails.csv'

# Wczytaj dane z pliku CSV
data = pd.read_csv(csv_file)

# Wyświetl kilka pierwszych wierszy, aby zobaczyć strukturę danych
print(data.head())

# Zakładamy, że w kolumnie 'message' mamy tekst e-maili, a w 'label' mamy etykiety
if 'message' in data.columns and 'label' in data.columns:
    emails = data['message']
    labels = data['label']
else:
    raise ValueError("Nie znaleziono wymaganych kolumn w pliku CSV")

# Funkcja czyszcząca tekst e-maili
def clean_text(text):
    text = re.sub(r'\S+@\S+', '', text)  # usuń adresy e-mail
    text = re.sub(r'http\S+', '', text)  # usuń linki
    text = re.sub(r'\d+', '', text)  # usuń cyfry
    text = re.sub(r'[^A-Za-z\s]', '', text)  # usuń znaki specjalne
    text = text.lower()  # zamień na małe litery
    return text

# Przetwarzanie tekstów e-maili
emails_cleaned = emails.apply(clean_text)

# Dodaj nową kolumnę do danych z przetworzonymi e-mailami
data['message_cleaned'] = emails_cleaned

# Zapisz przetworzone dane do nowego pliku CSV
data.to_csv('data/emails_processed.csv', index=False)

print("Przetwarzanie zakończone. Dane zapisane w 'data/emails_processed.csv'.")
