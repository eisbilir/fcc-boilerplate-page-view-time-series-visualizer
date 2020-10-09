import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",header=0,index_col="date",parse_dates=["date"])

# Clean data
df = df[(df.value<df.value.quantile(.975)) & (df.value>df.value.quantile(.025))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(32,10))
    sns.lineplot(data=df,x="date",y="value")
    ax.tick_params(labelsize=20)
    ax.set_xlabel("Date",fontsize=20)
    ax.set_ylabel("Page Views",fontsize=20)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019",fontsize=30)
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = [d.year for d in df_bar.index]
    df_bar['month'] = [d.strftime('%B') for d in df_bar.index]
    df_bar=df_bar.groupby(["year","month"]).mean().reset_index()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(8,8))
    sns.barplot(data=df_bar,x="year",y="value",hue="month",hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],palette=sns.color_palette())
    ax.set(xlabel="Years",ylabel="Average Page Views")
    ax.legend(loc="upper left",title="Months")
   
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig,ax=plt.subplots(1,2,figsize=(25,9))
    sns.boxplot(data=df_box,x='year',y='value',ax=ax[0])
    sns.boxplot(data=df_box,x='month',y='value',ax=ax[1], order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    ax[0].set_title("Year-wise Box Plot (Trend)",fontsize=30)
    ax[1].set_title("Month-wise Box Plot (Seasonality)",fontsize=30)
    ax[0].set_ylabel("Page Views",fontsize=20)
    ax[1].set_ylabel("Page Views",fontsize=20)
    ax[0].set_xlabel("Year",fontsize=20)
    ax[1].set_xlabel("Month",fontsize=20)
    ax[0].tick_params(labelsize=15)
    ax[1].tick_params(labelsize=15)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
