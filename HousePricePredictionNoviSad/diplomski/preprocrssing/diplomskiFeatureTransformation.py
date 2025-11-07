import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


pd.pandas.set_option('display.max_rows', None)
pd.pandas.set_option('display.max_columns', None)
if __name__ == '__main__':
    df = pd.read_csv('../data/diplomskiCleanedDatawithStateCorrupted.csv')

    print(df['state'].value_counts())
    top_values = df['infrastructure'].value_counts().nlargest(10).index.tolist()

    # Step 2: Create a new DataFrame with one-hot encoding for the top values
    one_hot_encoded_df = pd.get_dummies(
        df['infrastructure'].apply(lambda x: x if x in top_values else None))
    df.drop(['infrastructure'], axis=1, inplace=True)

    # Step 3: Concatenate the new DataFrame with the original dataset
    df = pd.concat([df, one_hot_encoded_df], axis=1)



    categorical_features = [feature for feature in df.columns if df[feature].dtype == 'object']

    for feature in categorical_features:
        temp = df.groupby(feature)['price'].count() / len(df)
        temp_df = temp[temp > 0.002].index
        rare_var_label = f'Rare_var_{feature}'  # Unique label for each feature
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
    selected_columns = ['surface', 'rooms', 'floor', 'yearOfBuild']
    # data[selected_columns] = min_max.fit_transform(data[selected_columns])

    data.to_csv('numeric_data_corrupted.csv', index=False)





