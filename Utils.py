# Average value function over lagged period
def lagged_avg(col, lag):
    import numpy as np
    val = col.loc[np.arange(0,lag)].mean()
    
    return val