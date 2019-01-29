
#GOT FROM https://stackoverflow.com/questions/18683821/generating-random-correlated-x-and-y-points-using-numpy
#But I'm sure this will also be interesting: https://quantcorner.wordpress.com/2018/02/09/generation-of-correlated-random-numbers-using-python/
#And this one too: https://scipy-cookbook.readthedocs.io/items/CorrelatedRandomSamples.html

import numpy as np
from matplotlib.pyplot import scatter,show
from scipy.stats import pearsonr


def generateCorrelatedData(corr):
	xx = np.array([-0.51, 51.2])
	yy = np.array([0.33, 51.6])
	means = [xx.mean(), yy.mean()]  
	stds = [xx.std() / 3, yy.std() / 3]

	covs = [[stds[0]**2          , stds[0]*stds[1]*corr], 
        [stds[0]*stds[1]*corr,           stds[1]**2]] 

	x,y = np.random.multivariate_normal(means, covs, 1000).T
	return x,y

if __name__ == "__main__":
	valx,valy = generateCorrelatedData(0.8)
	scatter(valx,valy,s=5)
	show()

	print (pearsonr(valx,valy))
