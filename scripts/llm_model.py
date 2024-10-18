import pandas as pd
import torch
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments

# Wczytaj dane
train_df = pd.read_csv('data/train.csv')
test_df = pd.read_csv('data/test.csv')

# Inicjalizacja tokenizer'a
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Tokenizacja danych
def tokenize(batch):
    return tokenizer(batch['email'], padding=True, truncation=True)

train_encodings = tokenizer(list(train_df['email']), truncation=True, padding=True, max_length=512)
test_encodings = tokenizer(list(test_df['email']), truncation=True, padding=True, max_length=512)

# Konwersja etykiet
import numpy as np

train_labels = list(train_df['label'])
test_labels = list(test_df['label'])

# Utworzenie obiektów Dataset
class EmailDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item
    def __len__(self):
        return len(self.labels)

train_dataset = EmailDataset(train_encodings, train_labels)
test_dataset = EmailDataset(test_encodings, test_labels)

# Inicjalizacja modelu
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

# Ustawienia treningu
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=1,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=8,
    evaluation_strategy='epoch',
    logging_dir='./logs',
    logging_steps=10,
)

# Definicja trenera
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

# Trenowanie modelu
trainer.train()

# Ewaluacja modelu
trainer.evaluate()
