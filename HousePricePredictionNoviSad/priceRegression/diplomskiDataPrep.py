import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
import matplotlib
import matplotlib.font_manager as fm

pd.pandas.set_option('display.max_columns', None)
from tabulate import tabulate
if __name__ == '__main__':

    pd.set_option('display.max_rows', None)
    data = pd.read_csv('../scraping/categoricPredictionDiplomskii.csv')



    print(data['sobe'].value_counts())



    # summary_table = tabulate(data.describe(include='all'), headers='keys', tablefmt='grid')
    # print(summary_table)

    # bins = range(25, 501,10)
    # numeric_columns = data.select_dtypes(include=['number'])
    # plt.rcParams['font.family'] = 'Arial'
    # plt.figure(figsize=(8, 6))  # Create a new figure for each histogram
    # plt.hist(data['povrsina'], bins=bins, edgecolor='k')  # Adjust the number of bins as needed
    # plt.xlabel('povrsina')
    # plt.ylabel('Frequency')
    #
    # plt.grid(True)
    # plt.show()