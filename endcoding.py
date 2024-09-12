import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

dt = 'data.csv'
df = pd.read_csv(dt, delimiter=';')

print('data sebelum di endsocoding : ')
print(df)

LE = LabelEncoder()
df['gender_endcode'] = LE.fit_transform(df['gender'])

one_hot = pd.get_dummies(df['kota'], prefix='kota')

df_encoded = pd.concat([df, one_hot], axis=1)

df_encoded.drop(columns=['gender', 'kota'], inplace=True)

print('data setelah endcoding : ')
print(df_encoded)

df_encoded.to_csv('encoded_data.csv', index=False)
print("File encoded_data.csv berhasil disimpan.")
