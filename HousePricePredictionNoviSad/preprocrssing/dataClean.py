import pandas as pd

pd.pandas.set_option('display.max_rows', None)
pd.pandas.set_option('display.max_columns', None)
if __name__ == '__main__':
    df = pd.read_csv('../data/kategoričneVrednostiNumerisane.csv')

    df.drop(['Unnamed: 0'], axis=1, inplace=True)

    # print(len(df))
    print(df.isnull().sum())
    print(df['stanje'].value_counts())





    df = df[df['cena'] > 10000 ]
    df['tip'] = df['tip'].fillna("missing")
    df['lift'] = df['lift'].fillna("missing")
    df['godina izgradnje'] = df['godina izgradnje'].fillna(int(round(df['godina izgradnje'].mean())))






    df.to_csv('../data/očišćenSet.csv', index=False)