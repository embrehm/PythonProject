!pip install yfinance==0.1.67
#!pip install pandas==1.3.3
#!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
#!pip install plotly==5.3.1

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Function takes dataframe with stock data (contains Date and Close columns), a dataframe with revenue data (contains Date and Revenue columns), and the name of the stock.

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
    
# use ticker to extract tesla data

tesla_et = yf.Ticker('TSLA')
tesla_data = tesla_et.history(period='max')
tesla_data.reset_index(inplace=True)
tesla_data.head()

# use request and beautiful soup to scrape revenue data
tesla_url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'
html_data = requests.get(tesla_url).text
tesla_soup = BeautifulSoup(html_data, 'html5lib')

# extracted table "Tesla Quarterly Revenue" and create a dataframe for the results
quarterly_rev = tesla_soup.find(string ="Tesla Quarterly Revenue").find_parent('table');

tesla_revenue= pd.DataFrame(columns=["Date", "Revenue"])
for row in quarterly_rev.find_all('tr'):
    col = row.find_all('td')
    if col != [] :
        date = col[0].text
        revenue = col[1].text
        tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)

# remove comma and dollar sign from revenue column
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")

# remove all null and empty strings
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# GameStop Extraction
gameStop_et = yf.Ticker("GME")
gme_data = gameStop_et.history(period="max")
gme_data.reset_index(inplace=True)

gme_url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
html_data = requests.get(gme_url).text
gme_soup = BeautifulSoup(html_data, 'html5lib')

q_rev = gme_soup.find(string ="GameStop Quarterly Revenue").find_parent('table');

gme_revenue= pd.DataFrame(columns=["Date", "Revenue"])
for row in q_rev.find_all('tr'):
    col = row.find_all('td')
    if col != [] :
        date = col[0].text
        revenue = col[1].text
        gme_revenue = gme_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)

