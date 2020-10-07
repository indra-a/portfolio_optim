import yfinance as yf

ticker = yf.Ticker('AMZN')
ticker = ticker.history(period = '10y')
ticker.groupby(ticker.index.year).apply(pd.Series.tail,1)

stocks_to_portfolio = ['AMZN', 'AAPL', 'SBUX', 'SO', 'INTC', 'CSCO', 'MET']
return_matrix = []
stock_char = []
for i in stocks_to_portfolio:
    stock = yf.Ticker(i)
    stock = stock.history(period='10y')
    data = stock.groupby(stock.index.year).apply(pd.Series.tail,1)
    prices = list(data['Close'])
    stock = Stock(prices)
    stock_char.append([i, stock.geometric_return(stock.annual_returns()), stock.standard_deviation(stock.annual_returns())])
    return_matrix.append(stock.annual_returns())
stock_char

plot_data = []
n = 0
while n < 5000:
    weight = list(np.random.dirichlet(np.ones(len(return_matrix)), size= 1)[0])
    port = Portfolio(return_matrix)
    plot_data.append([weight, port.portfolio_return(weight), port.portfolio_volatility(weight)])
    n += 1
    
def optimal_portfolio(self, desired_return):
        bounds = ((0.0, 1.0),) * len(self.returns)
        init = list(np.random.dirichlet(np.ones(len(self.returns)), size= 1)[0])
        optimal_weights = optimize.minimize(self.portfolio_volatility, init, method='SLSQP',
            constraints=({'type': 'eq', 'fun': lambda inputs: 1.0 - np.sum(inputs)},
            {'type': 'eq', 'fun': lambda inputs: desired_return - self.portfolio_return(weights=inputs)}), bounds = bounds)
        return optimal_weights.x
      
port = Portfolio(return_matrix)
port.optimal_portfolio(0.2)
