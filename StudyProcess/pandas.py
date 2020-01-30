#!/usr/bin/env 

import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
from pandas import Series

s = Series(np.random.randn(10)).cumsum()
s.plot(kind='bar')
plt.show()