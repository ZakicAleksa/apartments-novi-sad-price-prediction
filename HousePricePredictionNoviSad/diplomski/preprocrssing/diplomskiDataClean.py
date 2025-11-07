import pandas as pd

pd.pandas.set_option('display.max_rows', None)
pd.pandas.set_option('display.max_columns', None)
if __name__ == '__main__':
    df = pd.read_csv('../data/diplomskiSaStanjemSet.csv')

    df.drop(['Unnamed: 0'], axis=1, inplace=True)

    # print(len(df))
    print(df.isnull().sum())
    print(df['state'].value_counts())





    df = df[df['price'] > 10000 ]
    df['type'] = df['type'].fillna("missing")
    df['elevator'] = df['elevator'].fillna("missing")
    df['yearOfBuild'] = df['yearOfBuild'].fillna(int(round(df.yearOfBuild.mean())))






    # df.to_csv('diplomskiCleanedDataWithStateCorrupted.csv', index=False)