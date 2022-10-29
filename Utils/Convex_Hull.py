import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.spatial import ConvexHull


def plot_portfolio_convex_hull(CovexHull_DF):
    
    """
    Where input dataframe is daily return . 

    CovexHull_DF Columns : Annual Std ,Returns 
                 Index   : Portfolio
    """

    CovexHull_Dataset   = CovexHull_DF.values 
    CovexHull_DF['Unbiased_Std']      = CovexHull_DF['Unbiased_Std']
    CovexHull_DF['Expected_Returns']  = CovexHull_DF['Expected_Returns']
    hull                              = ConvexHull(CovexHull_Dataset)

    Unbiased_Std    = CovexHull_DF['Unbiased_Std']
    Expected_Return = CovexHull_DF['Expected_Returns']

    # Figure
    fig,ax = plt.subplots(figsize=(18,6))
    ax.set_title('Assets Convex Hull')
    ax.scatter(Unbiased_Std,Expected_Return,color='blue')

    for i in range(Expected_Return.shape[0]):
        ax.annotate(CovexHull_DF.index[i],xy=(Unbiased_Std[i],Expected_Return[i]))

    for simplex in hull.simplices:
        plt.plot(CovexHull_Dataset[simplex, 0], CovexHull_Dataset[simplex, 1], 'k-')

    ax.set_ylabel('Asset Returns')
    ax.set_xlabel('Asset Std')


