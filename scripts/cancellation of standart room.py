import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read Excel file
df = pd.read_excel('train.xlsx')

# Explore the data
print(df.head())
print(df.info())

df['Дата отмены'] = df['Дата отмены'].notna().astype(int)

types = ['Стандарт', 'Люкс', 'Апартаменты', 'Студия', 'Коттедж']
for t in types:
    df[t] = df['Категория номера'].str.contains(t).astype(int)
# Рассчитываем процент отмен для каждого типа номера
percentages = []
for type_name in types:
    cancelled = df.loc[df[type_name] == 1, 'Дата отмены'].sum()
    total = df[type_name].sum()
    percentage = (cancelled / total) * 100
    percentages.append(percentage)

# Строим гистограмму
plt.figure(figsize=(10, 6))
plt.bar(types, percentages)
plt.xlabel('Категория номера')
plt.ylabel('Процент отмен')
plt.title('Процент отмен бронирований по категориям номеров')
plt.xticks(rotation=45)
plt.show()