# Stock Price Prediction
<br>
<img src='images/Stock-Price-Prediction.jpg' width = '100%' height='350px'>

## Project Overview

Investment firms, hedge funds and even individuals have been using financial models to understand market behaviour better and make profitable investments and trades. A wealth of information is available in the form of historical stock prices and company performance data, suitable for machine learning algorithms to process.

Can we predict stock prices with machine learning? Investors make educated guesses by analyzing data. They will read the news, study the company history, industry trends, and other data points that go into making a prediction. The prevailing theories are that stock prices are totally random and unpredictable, raising the question of why top firms like Morgan Stanley and Citigroup hire quantitative analysts to build predictive models. We have this idea of the trading floor being filled with adrenaline infuse men with loose ties running around yelling something into a phone. However, these days we are more likely to see rows of machine learning experts quietly sitting in front of computer screens. About 70% of all orders on Wall Street are now placed by software. We are now living in the age of algorithms.

This project utilizes the ARIMA model for base predictions and then built a Deep Learning model to improve it further. Stock prices are predicted for Tech Giants like Apple, Google, Tesla, Microsoft and Amazon.


## Dataset
Webscraped https://in.finance.yahoo.com using selenium and BeautifulSoup.

## Exploratory Data Analysis

### Closing Price v/s Time
<br>
<img src='images/Moving_Average.png'>

We can see from the above graph that Telsa shares have tremendous growth in the 2020-2021 period.
<br>
If we follow the news, it can be due to

1. Emission Credit Sales
2. Tesla entering the Fast-Growing Compact SUV Market
3. Starting production in China

For the rest of the Companies, we can see that COVID-19 is the primary factor affecting the 2020-2021 period.
<br>

### Histogram plot of Percentage Daily Return 
<br>
<img src='images/Daily_Returns.png'>

### Correlation between the stocks daily returns
<br>
<img src='images/Correlation_Plot.png'>
<br>
From the above plot, we can see that Microsoft and Google had the strongest correlation in stocks daily returns.

### Risk v/s Expected Returns
<br>
<img src='images/Risk_vs_Expected_Returns.png'>
<br>
From the above graph, we can see that Tesla has the highest expected returns and the highest risk factor. Google has the lowest expected returns and the lowest risk factor.

## Deep Learning Model

### Model
<br>
<img src='images/model.png'>
<br><br>
We train the model using the training dataset records and then use it to forecast the following week’s closing values (i.e., the next five values as a week consists of five working days). The forecasting is done in a multi-step manner with a walk-forward validation mode. <br><br> 
The details of the design of each layer and the overall architecture of the model are as follows :
<br>
The input data’s shape to the network’s input layer is (5, 1), indicating that the previous five values (i.e., one week’s data) of the time series are used as the input. Only one attribute of the data (i.e., the closing value) is considered. The input layer passes the data onto the LSTM layer with 200 nodes at the output, with the Leaky ReLU activation function is used in these nodes. The LSTM layer’s output is passed to another LSTM layer with 200 nodes at the output, with the Leaky ReLU as an activation function. This layer’s output is then passed onto a dense layer with 200 nodes at its input and output, with Leaky ReLU activation. This layer’s output is passed onto another dense layer with 200 nodes at its input and 100 nodes with a Leaky ReLU activation function at the output. This layer’s output is passed onto another dense layer with 100 nodes at its input and 50 nodes with a Leaky ReLU activation function at the output. The dense layer is finally connected to the output layer that is also fully-connected. The output layer has 50 nodes at its input and 5 nodes at the output. The 5 nodes at the output produce the forecasted values for the five days of the following week. Again the output layer uses Leaky ReLU as an activation function. The model uses MSE as the loss function and ADAM as the optimizer with a custom learning rate. 

### Custom Learning Rate 
<br>
<img src='images/Learning_Rate.png'>

## Results
<br>

|           | ARIMA Model (RMSE) | Deep Learning Model (RMSE) | 
| --------- | ------------------ | -------------------------- |
| Apple     | 6.40               | 4.82                       |
| Tesla     | 108.11             | 66.40                      |
| Google    | 210.40             | 115.66                     |
| Microsoft | 7.26               | 6.23                       |
| Amazon    | 113.18             | 87.48                      |

## References
1. Mehtab, S. (2020, September 20). Stock Price Prediction Using Machine Learning and LSTM-Based Deep Learning Models. ArXiv.Org. https://arxiv.org/abs/2009.10819
2. Chauhan, N. S. (2020, January). Stock Market Forecasting Using Time Series Analysis. KDnuggets. https://www.kdnuggets.com/2020/01/stock-market-forecasting-time-series-analysis.html
3. Dev, U. (2020, June 21). EDA of Stock Market using Time Series - Usharbudha Dev. Medium. https://usharbudha-dev09.medium.com/eda-of-stock-market-using-time-series-9662fd18bfc5
