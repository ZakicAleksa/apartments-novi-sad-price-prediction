import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn import ensemble
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score, mean_squared_error,mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.tree import  plot_tree

pd.pandas.set_option('display.max_rows', None)

if __name__ == '__main__':
    data = pd.read_csv('../diplomski/data/numeric_data_with_state.csv')
    z =data.drop('price', axis=1)
    X = data.drop('price', axis=1).values
    y = data['price'].values
    min_max_scaler = MinMaxScaler().fit(X)
    X = min_max_scaler.fit_transform(X.astype(float))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)
    params = {
        "n_estimators": 100,
        "max_depth": 5,
        "min_samples_split": 5,
        "learning_rate": 0.2,
        "loss": "squared_error",
    }
    clf = ensemble.GradientBoostingRegressor(**params)
    clf.fit(X_train, y_train)
    print("GradientBoostingRegressor score: ", clf.score(X_test, y_test))
    y_pred = clf.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print("The mean squared error (MSE) on test set: {:.4f}".format(mse))
    print('MAE:', mean_absolute_error(y_test, y_pred))
    test_score = np.zeros((params["n_estimators"],), dtype=np.float64)
    for i, y_pred in enumerate(clf.staged_predict(X_test)):
        test_score[i] = clf.loss_(y_test, y_pred)


    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    y_pr = model.predict(X_test)
    print("RandomForestRegressor: ", r2_score(y_test, y_pr))
    # plot_tree()
    # plt.show()
    #
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    print(clf.score(X_train, y_train))
    print(clf.score(X_test, y_test))


    feature_imp = pd.Series(clf.feature_importances_, index=z.columns).sort_values(ascending=False)
    print(feature_imp)

