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

grouped = df.groupby('Категория номера')['Внесена предоплата'].mean()

# Строим гистограмму
plt.figure(figsize=(10, 6))
plt.bar(grouped.index, grouped.values)
plt.xlabel('Категория номера')
plt.ylabel('Средняя внесенная предоплата')
plt.title('Зависимость средней предоплаты от типа номера')
plt.xticks(rotation=45)  # Поворачиваем метки оси X для лучшей читаемости
plt.show()