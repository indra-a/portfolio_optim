import numpy as np

#class Stock takes array of closing prices at the beginning and at the end of the year
#as well as array of dividend yield for that year if there is one and calculates geometric return and standard deviation
class Stock:
    def __init__(self, prices, dividends=False):
        self.prices = prices
        self.dividends = dividends
        if len(self.prices) != len(self.dividends):
            print("Price and dividend data don't match. Default padding")
            self.dividends = (len(self.prices)*[0]+self.dividends)[-len(self.prices):]

    def annual_returns(self):
        returns = []
        for i in range(0, len(self.prices)-1):
            returns.append((self.prices[i+1]-self.prices[i])/self.prices[i])
        if self.dividends != False:
            dividend_yield = [a/b for a,b in zip(self.dividends, self.prices)][1:]
            returns = [a+b for a,b in zip(returns, dividend_yield)]
        return(returns)
            
    def geometric_return(self, returns):
        return(np.prod([x+1 for x in returns])**(1/len(returns))-1)
    
    def standard_deviation(self, returns):
        mean = sum(returns)/len(returns)
        return(np.sqrt(sum([(x-mean)**2 for x in returns])/len(returns)))

#class portfolio takes matrix of returns for every stock, and array of their weights
class Portfolio:
    def __init__(self, returns, weights):
        self.returns = returns
        self.weights = weights
        if len(self.returns) != len(self.weights):
            EnvironmentError('Data is missing')
        if sum(self.weights) != 1:
            EnvironmentError('Weights are wrong!')
    
    def portfolio_return(self):
        geo_returns = []
        for i in self.returns:        
            geo_returns.append(np.prod([x+1 for x in i])**(1/len(i))-1)
        return(sum([a*b for a,b in zip(self.weights, geo_returns)]))

    def portfolio_volatility(self):
        sd_values = []
        for i in self.returns:
            mean = sum(i)/len(i)
            sd_values.append(np.sqrt(sum([(x-mean)**2 for x in i])/len(i)))
        weighted_average = [a*b for a,b in zip(self.weights, sd_values)]
        corr = np.corrcoef(self.returns)
        values = []
        for j in range(0, len(weighted_average)):
            values.append(sum([weighted_average[j]*weighted_average[x]*corr[j,x] for x in range(0,len(weighted_average))]))
        return(np.sqrt(sum(values)))

