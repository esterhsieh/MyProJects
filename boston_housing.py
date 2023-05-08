"""
File: boston_housing_competition_decisionTree.py
Name: 依汝
--------------------------------
This file demonstrates how to analyze boston
housing dataset. Students will upload their
results to kaggle.com and compete with people
in class!

You are allowed to use pandas, sklearn, or build the
model from scratch! Go data scientists!
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model, preprocessing, model_selection, metrics, svm, tree, ensemble
import matplotlib.ticker as ticker

TRAIN_FILE = 'boston_housing/train.csv'                    # Training set filename
TEST_FILE = 'boston_housing/test.csv'                      # Test set filename


# CRIM： 按城鎮劃分的人均犯罪率
# ZN： 大於25000平方英尺的住宅用地比例
# INDUS： 每個城鎮非零售業務英畝比例
# CHAS ： 查理斯河流 啞變數 （靠近河流為1; 否則為0）
# NOX： 一氧化氮濃度 （百萬分之）
# RM： 每個住宅的房間數
# AGE： 1940年之前建造的自由單位
# DIS： 與5個波士頓就業中心的加權距離
# RAD： 高速公里同行能力指數
# PTRATIO： 按城鎮劃分的師生比例
# B： 1000（Bk — 0.63）²， 按城鎮劃分的非裔人口結構比例
# LSTAT： 低收入人口百分比
# MEDV： 自有住房的中位數價值（單位：1000美元）


def main():
    data = pd.read_csv(TRAIN_FILE)
    print(data.head())
    print(data.isnull().sum())
    # print(np.isnan(data))

    train_data, val_data = model_selection.train_test_split(data, train_size=0.7, random_state=42)
    # Extract true labels
    labels_train = train_data.medv
    labels_val = val_data.medv

    # Extract features
    x_train = train_data[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'black', 'lstat']]
    x_val = val_data[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'black', 'lstat']]
    print(x_train.shape[1])

    # Standardization or Normalization
    standardizer = preprocessing.StandardScaler()
    s_x_train = standardizer.fit_transform(x_train)
    s_x_val = standardizer.fit_transform(x_val)
    normalizer = preprocessing.MinMaxScaler()
    n_x_train = normalizer.fit_transform(x_train)
    n_x_val = normalizer.fit_transform(x_val)

    # LinearRegression
    linear_h = linear_model.LinearRegression()
    weights_linear = linear_h.fit(n_x_train, labels_train)
    predict_linear_train = weights_linear.predict(n_x_train)
    r2_score_linear_train = metrics.r2_score(labels_train, predict_linear_train)
    adj_r2_score_linear_train = 1 - (1 - r2_score_linear_train) * ((len(labels_train) - 1) /
                                                                   (len(labels_train) - n_x_train.shape[1] - 1))
    rmse_linear_train = (np.sqrt(metrics.mean_squared_error(labels_train, predict_linear_train)))
    predict_linear_val = weights_linear.predict(n_x_val)
    r2_score_linear_val = metrics.r2_score(labels_val, predict_linear_val)
    adj_r2_score_linear_val = 1 - (1 - r2_score_linear_val) * ((len(labels_val) - 1) /
                                                               (len(labels_val) - n_x_val.shape[1] - 1))
    rmse_linear_val = (np.sqrt(metrics.mean_squared_error(labels_val, predict_linear_val)))
    print('='*10, '<Linear Regression>', '='*10)
    print('Adjusted R-squared (train): ', adj_r2_score_linear_train)
    print('Adjusted R-squared (val): ', adj_r2_score_linear_val)
    print("RMSE (train): ", rmse_linear_train)
    print("RMSE (val): ", rmse_linear_val, '\n')

    # Support Vector Regression (SVR)
    svr_h = svm.SVR()
    weights_svr = svr_h.fit(s_x_train, labels_train)
    predict_svr_train = weights_svr.predict(s_x_train)
    r2_score_svr_train = metrics.r2_score(labels_train, predict_svr_train)
    adj_r2_score_svr_train = 1 - (1 - r2_score_svr_train) * ((len(labels_train) - 1) /
                                                             (len(labels_train) - s_x_train.shape[1] - 1))
    rmse_svr_train = (np.sqrt(metrics.mean_squared_error(labels_train, predict_svr_train)))
    predict_svr_val = weights_svr.predict(s_x_val)
    r2_score_svr_val = metrics.r2_score(labels_val, predict_svr_val)
    adj_r2_score_svr_val = 1 - (1 - r2_score_svr_val) * ((len(labels_val) - 1) /
                                                         (len(labels_val) - s_x_val.shape[1] - 1))
    rmse_svr_val = (np.sqrt(metrics.mean_squared_error(labels_val, predict_svr_val)))
    print('=' * 10, '<Support Vector Regression (SVR)>', '=' * 10)
    print('Adjusted R-squared (train): ', adj_r2_score_svr_train)
    print('Adjusted R-squared (val): ', adj_r2_score_svr_val)
    print("RMSE (train): ", rmse_svr_train)
    print("RMSE (val): ", rmse_svr_val, '\n')

    # Decision Tree Regression
    d_tree_h = tree.DecisionTreeRegressor(max_depth=5, min_samples_leaf=6, random_state=42)
    d_tree_weights = d_tree_h.fit(x_train, labels_train)
    predict_tree_train = d_tree_weights.predict(x_train)
    r2_score_tree_train = metrics.r2_score(labels_train, predict_tree_train)
    adj_r2_score_tree_train = 1 - (1 - r2_score_tree_train) * ((len(labels_train) - 1) /
                                                               (len(labels_train) - x_train.shape[1] - 1))
    rmse_tree_train = (np.sqrt(metrics.mean_squared_error(labels_train, predict_tree_train)))
    predict_tree_val = d_tree_weights.predict(x_val)
    r2_score_tree_val = metrics.r2_score(labels_val, predict_tree_val)
    adj_r2_score_tree_val = 1 - (1 - r2_score_tree_val) * ((len(labels_val) - 1) /
                                                          (len(labels_val) - x_val.shape[1] - 1))
    rmse_tree_val = (np.sqrt(metrics.mean_squared_error(labels_val, predict_tree_val)))
    print('=' * 10, '<Decision Tree Regression>', '=' * 10)
    print('Adjusted R-squared (train): ', adj_r2_score_tree_train)
    print('Adjusted R-squared (val): ', adj_r2_score_tree_val)
    print("RMSE (train): ", rmse_tree_train)
    print("RMSE (val): ", rmse_tree_val, '\n')

    # Random Forest Regression
    forest = ensemble.RandomForestRegressor(n_estimators=500, max_depth=5, random_state=42)
    forest_weights = forest.fit(x_train, labels_train)
    predict_forest_train = forest_weights.predict(x_train)
    r2_score_forest_train = metrics.r2_score(labels_train, predict_forest_train)
    adj_r2_score_forest_train = 1 - (1 - r2_score_forest_train) * ((len(labels_train) - 1) /
                                                                   (len(labels_train) - x_train.shape[1] - 1))
    rmse_forest_train = (np.sqrt(metrics.mean_squared_error(labels_train, predict_forest_train)))
    predict_forest_val = forest_weights.predict(x_val)
    r2_score_forest_val = metrics.r2_score(labels_val, predict_forest_val)
    adj_r2_score_forest_val = 1 - (1 - r2_score_forest_val) * ((len(labels_val) - 1) /
                                                               (len(labels_val) - x_val.shape[1] - 1))
    rmse_forest_val = (np.sqrt(metrics.mean_squared_error(labels_val, predict_forest_val)))
    print('=' * 10, '<Random Forest Regression>', '=' * 10)
    print('Adjusted R-squared (train): ', adj_r2_score_forest_train)
    print('Adjusted R-squared (val): ', adj_r2_score_forest_val)
    print("RMSE (train): ", rmse_forest_train)
    print("RMSE (val): ", rmse_forest_val, '\n')

    models = [('Linear Regression', adj_r2_score_linear_train, adj_r2_score_linear_val, rmse_linear_train, rmse_linear_val),
              ('Support Vector Regression', adj_r2_score_svr_train, adj_r2_score_svr_val, rmse_svr_train, rmse_svr_val),
              ('Decision Tree Regression', adj_r2_score_tree_train, adj_r2_score_tree_val, rmse_tree_train, rmse_tree_val),
              ('Random Forest Regression', adj_r2_score_forest_train, adj_r2_score_forest_val, rmse_forest_train, rmse_forest_val)]
    models_df = pd.DataFrame(data=models, columns=['Model', 'Adjusted R-squared (train)', 'Adjusted R-squared (val)',
                                                   'RMSE (train)', 'RMSE (val)'])

    # Adjusted R-squared fig
    fig, axes = plt.subplots(2, 1, figsize=(14, 6))
    fig.canvas.set_window_title('Adjusted R-squared barchart')
    models_df.sort_values(by=['Adjusted R-squared (train)'], ascending=False, inplace=True)
    sns.barplot(x='Adjusted R-squared (train)', y='Model', data=models_df, palette='Blues_d', ax=axes[0], width=0.6)
    axes[0].set_xlabel('RAdjusted R-squared (train)', size=14)
    axes[0].set_ylabel('Model', size=14)
    axes[0].set_xlim(0, 1.0)

    models_df.sort_values(by=['Adjusted R-squared (val)'], ascending=False, inplace=True)
    sns.barplot(x='Adjusted R-squared (val)', y='Model', data=models_df, palette='Reds_d', ax=axes[1], width=0.6)
    axes[1].set_xlabel('Adjusted R-squared (val)', size=14)
    axes[1].set_ylabel('Model', size=14)
    axes[1].set_xlim(0, 1.0)
    plt.subplots_adjust(hspace=0.5, left=0.2)
    plt.show()

    # RMSE fig
    fig1 = plt.figure(figsize=(10, 6))
    fig1.canvas.set_window_title('RMSE of train and val')
    ax = fig1.add_subplot(1, 1, 1)
    ax.scatter(x='Model', y='RMSE (train)', data=models_df, marker='o', s=100)
    ax.scatter(x='Model', y='RMSE (val)', data=models_df, marker='o', s=100)
    plt.xlabel('Model', size=14)
    plt.ylabel('RMSE', size=14)
    plt.legend(['RMSE (train)', 'RMSE (val)'])
    plt.show()
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    # plt.xticks(rotation=45)


if __name__ == '__main__':
    main()