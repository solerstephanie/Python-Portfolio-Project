#Stephanie Soler//August 23 2024//StockProblemPortfolioProgram
from datetime import date, timedelta
import numpy
import pandas as pd
import pygal

class Stock:
    def __init__(self, symbol, purchase_price, current_price, quantity, purchase_date, purchase_id):
        self.symbol = symbol
        self.purchase_price = purchase_price
        self.current_price = current_price
        self.quantity = quantity
        self.purchase_date = purchase_date
        self.purchase_id = purchase_id

    def get_stock_data():     
        df = pd.read_json('/Users/stephaniesoler/Downloads/AllStocks.json')
        
        close_list = (df['Close'])
        symbol_list = (df['Symbol'])            
        dates_list = (list(df['Date']))
        date_obj = []
        for i in dates_list:
            date_obj.append(date.strftime(i, '%d-%m-%y'))
        new_dates = set(date_obj)
        dates = list(new_dates)
        aig_stock_value = []
        f_stock_value = []
        fb_stock_value = []
        goog_stock_value = []
        ibm_stock_value = []
        m_stock_value = []
        msft_stock_value = []
        rdsa_stock_value = []
        
        for i in symbol_list: 
            if i == "AIG":
                aig_stock_value.append(125 * close_list)
            elif i == "F": 
                f_stock_value.append(85 * close_list)
            elif i == "FB":
                fb_stock_value.append(400 * close_list)
            elif i == "GOOG":
                goog_stock_value.append(235 * close_list)
            elif i == "IBM":
                ibm_stock_value.append(150 * close_list)
            elif i == "M":
                m_stock_value.append(425 * close_list)
            elif i == "MSFT":
                msft_stock_value.append(85 * close_list)
            elif i == "RDS-A":
                rdsa_stock_value.append(80 * close_list)
            else:
                print('bad entry')
        
        date_chart = pygal.Line(x_label_rotation=20)
        date_chart.title = 'Stock Value Data'
        date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), [
            date(2015,7,1),
            date(2015,10,1),
            date(2016,4,1),
            date(2016,7,1),
            date(2016,10,1),
            date(2017,1,1),
            date(2017,4,1),
            date(2017,7,1)])
        date_chart.add('AIG', numpy.unique(aig_stock_value))
        date_chart.add('F', numpy.unique(f_stock_value))
        date_chart.add('FB', numpy.unique(fb_stock_value))
        date_chart.add('GOOG', numpy.unique(goog_stock_value))
        date_chart.add('IBM', numpy.unique(ibm_stock_value))
        date_chart.add('M', numpy.unique(m_stock_value))
        date_chart.add('MSFT', numpy.unique(msft_stock_value))
        date_chart.add('RDS-A', numpy.unique(rdsa_stock_value))
        date_chart.render_to_file('/Users/stephaniesoler/Downloads/SimpleStock1.svg')
        
class Investor:
    def __init__(self,investor_id, name, address, phone):
        self.investor_id = investor_id
        self.name = name
        self.address = address
        self.phone = phone
        self.stocks = []
    
    def __str__(self):
        return f"Investor ID: {self.investor_id}\nInvestor Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}"

# Instantiate Investor
investor = Investor("INV001", "Bob Smith", "123 Main St, City, State", "123-456-7890")

# Print Investor Information
print("Investor Information:")
print(investor)

# Print Information
print(Stock.get_stock_data())

