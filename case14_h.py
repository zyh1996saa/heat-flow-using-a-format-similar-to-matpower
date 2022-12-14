import numpy as np

def case14_h():
    
    
    case = {'version':1}
    """
        branch data format
        from_bus_num,to_bus_num,length(m),diameter(mm),lambda(W/mK)#热传导系数
    """
    case['branch'] = np.array([
        [1,2,297.6,125,0.321],
        [2,3,212.5,40,0.21],
        [3,4,301.5,40,0.21],
        [3,5,194.5,100,0.327],
        [5,11,131.3,40,0.189],
        [2,6,505.4,65,0.236],
        [6,7,212.3,40,0.21],
        [7,8,322.8,40,0.21],
        [8,9,187.7,40,0.21],
        [9,10,102.8,100,0.327],
        [11,10,129.1,40,0.31],
        [12,2,316.1,100,0.327],
        [13,5,196.2,80,0.278],
        [14,7,120.2,100,0.31]
    ])
    
    case['mq'] = np.array([
        0.6,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ])
    
    return case