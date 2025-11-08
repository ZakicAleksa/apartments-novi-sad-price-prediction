import pandas as pd
from sklearn import ensemble
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.model_selection import GridSearchCV
import numpy as np
import pickle

if __name__ == '__main__':
    data = pd.read_csv('../data/enkodovanSet.csv')

    Z = data.drop('cena', axis=1)
    X = data.drop('cena', axis=1).values
    y = data['cena'].values

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    n_estimators = [int(x) for x in np.linspace(start=100, stop=500, num=8)]
    max_depth = [2, 3, 4, 5, 6]
    min_samples_split = [2, 3, 4]
    min_samples_leaf = [1, 2, 3]
    learning_rate = [float(x) for x in np.linspace(start=0.05, stop=0.3, num=6)]
    loss = ["squared_error", "absolute_error"]

    params = {
        'learning_rate': 0.15000000000000002,
        'loss': 'absolute_error',
        'max_depth': 5,
        'min_samples_leaf': 3,
        'min_samples_split': 4,
        'n_estimators': 500
    }

    paramss = {
        'learning_rate': 0.1,
        'loss': 'squared_error',
        'max_depth': 3,
        'min_samples_leaf': 1,
        'min_samples_split': 2,
        'n_estimators': 100
    }

    # {'learning_rate': 0.15000000000000002,
    #  'loss': 'absolute_error',
    #  'max_depth': 5,
    #  'min_samples_leaf': 3,
    #  'min_samples_split': 4,
    #  'n_estimators': 500}

    # gb = ensemble.GradientBoostingRegressor()
    # gradient_boost_regressor_grid = GridSearchCV(estimator=gb, param_grid=params, cv=5, verbose=2, n_jobs=8)
    # gradient_boost_regressor_grid.fit(x_train, y_train)
    # print(gradient_boost_regressor_grid.best_params_)

# --------------------------------
#     scoring = {'MAE': make_scorer(mean_absolute_error), 'R2': make_scorer(r2_score)}
#
#     grid_search = GridSearchCV(model, param_grid, scoring=scoring, refit='R2', cv=5)
#
# -------------------



    gb = ensemble.GradientBoostingRegressor(**params)
    gb.fit(x_train, y_train)

    y_pred = gb.predict(x_test)
    pickle.dump(gb, open("../models/model.pkl", "wb"))

    print("Gradinet boosting regressor R2: ", r2_score(y_test, y_pred))
    print('MAE:', mean_absolute_error(y_test, y_pred))

    # feature_importances = gb.feature_importances_
    # print("\nFeature importances:")
    # for feature, importance in zip(Z.columns, feature_importances):
    #     print(f"{feature}: {importance:.4f}")