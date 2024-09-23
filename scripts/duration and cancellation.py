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

df['Продолжительность'] = (df['Выезд'] - df['Заезд']).dt.days
df_filtered = df[df['Продолжительность'] <= 12]
# Группируем DataFrame по продолжительности поездки и считаем количество отмен
grouped = df_filtered.groupby('Продолжительность')['Дата отмены'].sum()

plt.figure(figsize=(10, 6))
plt.bar(grouped.index, grouped.values)  # Используем plt.bar для гистограммы
plt.xlabel('Продолжительность поездки (дней)')
plt.ylabel('Количество отмен')
plt.title('Количество отмен бронирований по продолжительности поездки')
plt.show()