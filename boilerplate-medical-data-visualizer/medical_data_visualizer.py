import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv", delimiter=',')
# print(df)

# Add 'overweight' column
bmi = df['weight'] / pow (df['height'] / 100, 2)
df['overweight'] = bmi.apply(lambda x: 1 if x > 25 else 0)
# print(df['overweight'])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1 )
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)
# print(df[['cholesterol', 'gluc']])

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.

    # pd.melt reshapes the data by unpivot a dataframe from wide to long format
    # the center of retention around the above labels that everything around them

    # use cardio as identifier variable
    # the mentioned features are set to unpivot
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc' , 'smoke' , 'alco', 'active', 'overweight'])
    # print(df_cat)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # group the data by subset that each cardio has features with different values.
    df_cat = df_cat.value_counts(['cardio', 'variable', 'value']).sort_index(ascending=True).reset_index(name='total')
    # set a new column in dataframe with all the values in the series equal to 1
    # df_cat["total"] = 1
    # df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index =False).count()
    # print(df_cat)

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x = 'variable' , y = 'total', hue='value', col = 'cardio', data = df_cat, kind = "bar").fig
    # convert catplot to figure

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # remove outliers from the data by data cleaning
    # Clean the data 
    df_heat = df[
      (df['ap_lo'] <= df['ap_hi'])
    & (df['height'] >= df['height'].quantile(0.025)) 
    & (df['height'] <= df['height'].quantile(0.975)) 
    & (df['weight'] >= df['weight'].quantile(0.025)) 
    & (df['weight'] <= df['weight'].quantile(0.975))
    ]
    # print(df_heat)

    # statistical technique that show two variables are related
    # find the pairwise correlation of all columns in the dataframe
    # Calculate the correlation matrix 
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, vmax=.3, center=0, square=True, linewidths=.7, cbar_kws={"shrink": .5, 'ticks': [-0.08, 0.00, 0.08, 0.16, 0.24]}, annot=True, fmt=".1f")

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
