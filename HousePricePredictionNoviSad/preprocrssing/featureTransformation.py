import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


pd.pandas.set_option('display.max_rows', None)
pd.pandas.set_option('display.max_columns', None)
if __name__ == '__main__':
    df = pd.read_csv('../data/očišćenSet.csv')

    print(df['stanje'].value_counts())
    top_values = df['infrastruktura'].value_counts().nlargest(10).index.tolist()

    one_hot_encoded_df = pd.get_dummies(
        df['infrastruktura'].apply(lambda x: x if x in top_values else None))
    df.drop(['infrastruktura'], axis=1, inplace=True)


    df = pd.concat([df, one_hot_encoded_df], axis=1)



    categorical_features = [feature for feature in df.columns if df[feature].dtype == 'object']

    for feature in categorical_features:
        temp = df.groupby(feature)['cena'].count() / len(df)
        temp_df = temp[temp > 0.002].index
        rare_var_label = f'retka_vrednost_{feature}'  # Unique label for each feature
        df[feature] = np.where(df[feature].isin(temp_df), df[feature], rare_var_label)

    def category_onehot_multcols(multcolumns):
        df_final = df.copy()
        for fields in multcolumns:
            print(fields)
            df1 = pd.get_dummies(df[fields], drop_first=False)

            df_final.drop([fields], axis=1, inplace=True)

            df_final = pd.concat([df_final, df1], axis=1)
        return df_final


    print(df.head())
    print("========================================================================================================")
    data = category_onehot_multcols(categorical_features)
    print(data.head())

    min_max = MinMaxScaler()
    selected_columns = ['površina', 'broj soba', 'sprat', 'godina izgradnje']
    # data[selected_columns] = min_max.fit_transform(data[selected_columns])

    data.to_csv('../data/enkodovanSet.csv', index=False)





