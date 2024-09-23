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

df_filtered = df[df['Номеров'] < 6]
grouped = df_filtered.groupby('Номеров')['Дата отмены'].agg(['sum', 'count'])
# Рассчитываем процент отмен для каждого количества номеров
grouped['Процент отмен'] = (grouped['sum'] / grouped['count']) * 100

# Строим гистограмму
plt.figure(figsize=(10, 6))
plt.bar(grouped.index, grouped['Процент отмен'])
plt.xlabel('Количество номеров')
plt.ylabel('Процент отмен %')
plt.title('Процент отмен бронирований по количеству номеров')
plt.show()
'''
grouped = df.groupby('Номеров')['Дата отмены'].sum()

plt.figure(figsize=(10, 6))
plt.bar(grouped.index, grouped.values)
plt.xlabel('Количество номеров')
plt.ylabel('Количество отмен')
plt.title('Количество отмен бронирований по количеству номеров')
plt.show()'''