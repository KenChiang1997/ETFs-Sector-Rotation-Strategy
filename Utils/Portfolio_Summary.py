import numpy as np 
import pandas as pd 
from dateutil import relativedelta




class Portfolio_Summary():

    def Annual_Return(Daily_Returns,freq_number):
        
        return np.round(np.mean(Daily_Returns) * freq_number,decimals=2)

    def Annual_Volitiliy(Daily_Returns,freq_number):

        return np.round(np.std(Daily_Returns) * np.sqrt(12),decimals=2)

    def Cumulative_Return(Daily_Returns):

        return np.round(np.cumsum(Daily_Returns)[-1],decimals=2)

    def Sharpe_Ratio(Daily_Returns,freq_number):

        u = np.mean(Daily_Returns) * freq_number
        sigma = np.std(Daily_Returns) * np.sqrt(freq_number)

        sharpe_ratio = u/sigma

        return np.round(sharpe_ratio,decimals=2)
        
    def Maximun_drawdown(Daily_Returns):

        max_drawdown = max(pd.Series(np.cumsum(Daily_Returns)).cummax().values - np.cumsum(Daily_Returns))
        
        return np.round(max_drawdown,decimals=2)

    def Calmar_Ratio(Daily_Returns,freq_number):

        u = np.mean(Daily_Returns) * freq_number
        max_drawdown = max(pd.Series(np.cumsum(Daily_Returns)).cummax().values - np.cumsum(Daily_Returns))

        Calmar_Ratio = u/max_drawdown

        return np.round(Calmar_Ratio,decimals=2)

    def Omega_Ratio(Daily_Returns,benchmark):

        Number_of_Win = len(np.where(Daily_Returns - benchmark > 0)[0])
        Number_of_Loss = len( np.where(Daily_Returns - benchmark < 0)[0])

        return Number_of_Win / Number_of_Loss

    def Value_at_Risk(Daily_Returns,confidence_level=0.95):

        type_1 = 1 - confidence_level
        var    = np.quantile(Daily_Returns,type_1)
            
        return  var


def Backtest_Summary(start_date,end_date,returns,freq,name=None):

    if freq == 'M':
        freq_number = 12 
    elif freq == "Y":
        freq_number = 1
    elif freq == "D":
        freq_number = 252

    delta = relativedelta.relativedelta(end_date, start_date)
    total_month = delta.years * 12 + delta.months
    start_date = str(start_date)[:10]
    end_date = str(end_date)[:10]

    BackTesint_Summary_Df = pd.DataFrame({

        "Start Date"        : [start_date], 
        "End   Date"        : [end_date], 
        "Total Periods"     : [str(total_month) +" Months"],
        "-"                 : ["-"],
        "Annual Return"     : [Portfolio_Summary.Annual_Return(returns,freq_number)], 
        "Anuual Volitiliy"  : [Portfolio_Summary.Annual_Volitiliy(returns,freq_number)], 
        "Cumulative Return" : [Portfolio_Summary.Cumulative_Return(returns)],
        "Sharpe Ratio"      : [Portfolio_Summary.Sharpe_Ratio(returns,freq_number)],
        "Calmar Ratio"      : [Portfolio_Summary.Calmar_Ratio(returns,freq_number)],
        "Maximum Drawdown"      : [ Portfolio_Summary.Maximun_drawdown(returns)],
        
    },index=[str(name)])

    return  BackTesint_Summary_Df.T
