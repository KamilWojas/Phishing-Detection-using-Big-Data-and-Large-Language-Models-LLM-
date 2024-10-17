import pandas as pd
import re

# Ścieżka do pliku CSV z surowymi danymi
csv_file = 'data/emails.csv'

# Wczytaj dane z pliku CSV
data = pd.read_csv(csv_file)

# Wyświetl kilka pierwszych wierszy, aby zobaczyć strukturę danych
print(data.head())

# Zakładamy, że w kolumnie 'message' mamy tekst e-maili, ale brakuje 'label'
if 'message' in data.columns:
    emails = data['message']
    # Dodaj kolumnę 'label', zakładając, że wszystkie wiadomości są nie-phishingowe (label = 0)
    labels = [0] * len(emails)
else:
    raise ValueError("Nie znaleziono kolumny 'message' w pliku CSV")

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

# Dodaj nową kolumnę do danych z przetworzonymi e-mailami i etykietami
data['message_cleaned'] = emails_cleaned
data['label'] = labels  # Dodanie kolumny z etykietami

# Zapisz przetworzone dane do nowego pliku CSV
data.to_csv('data/emails_processed.csv', index=False)

print("Przetwarzanie zakończone. Dane zapisane w 'data/emails_processed.csv'.")
