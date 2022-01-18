import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    #print(df.head())
    #print(df.describe())
    #print(df.info())

    # Create scatter plot
    plt.figure()
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], label='Original Data')


    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # fit the linear model
    res = linregress(x, y)

    # create predicted years by pandas series
    x_pred = pd.Series(range(1880 ,2051, 1))
    y_pred = res.intercept + res.slope * x_pred
    # plot the fitted line
    plt.plot(x_pred, y_pred, 'r', label='fitted line predicted from 1880')
   

    # Create second line of best fit

    # extract the data from year 2000 through the most recent year
    df_2000 = df[df['Year'] >= 2000]
    x2 = df_2000['Year']
    y2 = df_2000['CSIRO Adjusted Sea Level']

    # fit the linear model
    res2 = linregress(x2, y2)
    x_pred2 = pd.Series(range(2000, 2051, 1))
    y_pred2 = res2.intercept + res2.slope * x_pred2

    # plot the fitted line
    plt.plot(x_pred2, y_pred2, 'g', label='fitted line predicted from 2000')


    # Add labels and title
    plt.legend(loc="upper left")
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()