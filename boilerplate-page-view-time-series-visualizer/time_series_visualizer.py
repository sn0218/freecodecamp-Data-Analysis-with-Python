import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# parse the date by converting to pd datetime object
df['date'] = pd.to_datetime(df['date'])

# set 'date' to be dataframe index column
df = df.set_index('date')

# Clean data
# remove the extreme outliner of top 2.5% and bottom 2.5%
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot

    # create new figure
    fig = plt.figure(figsize=(20, 6))
    # Plot the time series line 
    plt.plot(df.index, df['value'], color='red', linewidth=1)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # set title and label of x axis and y axis
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Page Views', fontsize=12)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=14)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot

    # group the values by month by selecting dataframe index column using level parameter 
    # compute the average values by month
    df_bar = df.groupby(pd.Grouper(level='date', freq='M'))['value'].mean().rename('mean').to_frame()

    months = [
      'January',
      'February',
      'March',
      'April',
      'May',
      'June',
      'July',
      'August',
      'September',
      'October',
      'November',
      'December'
      ]

    # pivot with datetime index to construct pd dataframe
    df_bar = pd.pivot_table(df_bar, index=df_bar.index.year, columns=df_bar.index.month, values='mean')

    # set the dataframe index name
    df_bar.index.name = 'year'

    # rename columns headers and set the dataframe column name
    df_bar.columns = months
    df_bar.columns.name = 'Months'

    # Draw bar plot
    ax = df_bar.plot(kind='bar', xlabel='Years', ylabel='Average Page Views', figsize=(8, 7))

    fig = ax.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
  
    #print(df_box)

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(22, 8), dpi=100)

    sns.boxplot(y="value", x= "year", data=df_box, ax=axes[0], linewidth=0.5)
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel('Page Views')

    sns.boxplot(
      y="value",
      x= "month", 
      data=df_box, ax=axes[1],
      order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      linewidth=0.5,)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel('Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
