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

df['Разница между бронированием и заездом'] = (df['Заезд'] - df['Дата бронирования']).dt.days
df_filtered = df[(df['Разница между бронированием и заездом'] > 0) & (df['Разница между бронированием и заездом'] < 100)]
# Группируем DataFrame по продолжительности поездки и считаем количество отмен
grouped = df_filtered.groupby('Разница между бронированием и заездом')['Дата отмены'].sum()

plt.figure(figsize=(10, 6))
plt.bar(grouped.index, grouped.values)  # Используем plt.bar для гистограммы
plt.xlabel('Разница между заездом и бронированием (дней)')
plt.ylabel('Количество отмен')
plt.title('Количество отмен бронирований по разнице между заездом и бронированием')
plt.xticks(np.arange(min(grouped.index), max(grouped.index) + 9, 10))
plt.show()