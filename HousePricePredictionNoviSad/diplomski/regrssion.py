import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn import ensemble
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score



pd.pandas.set_option('display.max_rows', None)
if __name__ == '__main__':
    df = pd.read_csv('data/diplomskiCleanedData.csv')


    categorical_features = [feature for feature in df.columns if df[feature].dtype == 'O']

    # for feature in categorical_features:
    #     temp = df.groupby(feature)['price'].count() / len(df)
    #     temp_df = temp[temp > 0.002].index
    #     df[feature] = np.where(df[feature].isin(temp_df), df[feature], 'Rare_var')

    # print(df['address'].value_counts())



# ******************************************************************************************************************************



    # print(df['parking'].value_counts())

    def category_onehot_multcols(multcolumns):
        df_final = df.copy()
        i = 0
        for fields in multcolumns:

            print(fields)
            df1 = pd.get_dummies(df[fields], drop_first=True)

            df.drop([fields], axis=1, inplace=True)
            if i == 0:
                df_final = df1.copy()
            else:

                df_final = pd.concat([df_final, df1], axis=1)
            i = i + 1

        df_final = pd.concat([df, df_final], axis=1)

        return df_final
    #
    # categorical_features = [feature for feature in df.columns if df[feature].dtype == 'O']

    data = category_onehot_multcols(categorical_features)
    final_df = data.loc[:, ~data.columns.duplicated()]
    # print(final_df.shape)
    # final_df.info()
    # print(final_df['price'].describe())
    final_df.to_csv('numeric_data.csv', index=False)
    # ******************************************************************************************************************************


    X = final_df.drop('price', axis=1).values
    y = final_df['price'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
    lm = Ridge(alpha=20)
    lm.fit(X_train, y_train)
    print(lm.score(X_test, y_test))
    print("Slope:")
    print(lm.coef_)
    print("Intercept:")
    print(lm.intercept_)
    intercept = lm.intercept_
    slope = lm.coef_

    clf = ensemble.GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2,
                                             learning_rate=0.1, loss='ls')
    clf.fit(X_train, y_train)
    print("GradientBoostingRegressor:")
    print(clf.score(X_test, y_test))
    model = RandomForestRegressor(n_estimators=300)
    model.fit(X_train, y_train)
    y_pr = model.predict(X_test)
    print("RandomForestRegressor:")
    print(r2_score(y_test, y_pr))