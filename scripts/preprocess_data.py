import os
import pandas as pd
import numpy as np
import re

# Ścieżka do folderu z danymi
data_dir = 'data/enron'

# Lista do przechowywania e-maili i etykiet
emails = []
labels = []

# Przykład wczytywania e-maili z folderu
for root, dirs, files in os.walk(data_dir):
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(root, file), 'r', encoding='latin1') as f:
                email = f.read()
                emails.append(email)
                # Ustal etykietę na podstawie nazwy folderu lub innego kryterium
                labels.append(0)  # 0 - nie-phishing, 1 - phishing



# Utworzenie DataFrame
df = pd.DataFrame({'email': emails, 'label': labels})

# Zapisanie do pliku CSV
df.to_csv('data/emails.csv', index=False)
