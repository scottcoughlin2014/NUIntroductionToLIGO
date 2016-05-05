import numpy as np
import matplotlib.pyplot as plt
def stdNormal(x, mu, sig):
	return sci.norm.pdf(x, loc=mu, scale=sig)

def gaussianLikelihood(xlist, mu, sig):
	L = np.sum(np.log(stdNormal(xlist, mu, sig)))	
	if np.isnan(L):
		L = -10000000000.0
	return L


def MCMC_sample(N, mu, sigma, x0, step):
	import scipy.stats as sci
	x = np.zeros(N)
	x[0] = x0	
	for i in xrange(0, N - 1):
		x_proposed = np.random.normal(x[i], step)
		draw = np.random.uniform()

		if draw <= min(1, sci.norm.pdf(x_proposed, loc=mu, scale=sigma) / sci.norm.pdf(x[i], loc=mu, scale=sigma)):
			x[i+1] = x_proposed
		else:
			x[i+1] = x[i]
	return x	


def MCMC_infer():
        for i in xrange(0, N - 1):

                muProposed, sigProposed = np.random.multivariate_normal([mu_list[i], sig_list[i]], covar)
                draw = np.random.uniform()

                if np.log(draw) <= min(0.0, (gaussianLikelihood(data, muProposed, sigProposed) - gaussianLikelihood(data, mu_list[i], sig_list[i]))):
                        mu_list[i + 1] = muProposed
                        sig_list[i + 1] = sigProposed
                        log_likelihoods.append(gaussianLikelihood(data, mu_list[i+1], sig_list[i+1]))
                else:
                        mu_list[i + 1] = mu_list[i]
                        sig_list[i + 1] = sig_list[i]
        return(mu_list, sig_list)




def propose(ax=None):
	mu = 5.0
	sig = 0.01
	dat = np.random.normal(mu, sig, 10000)
	plt.hist(dat, bins=100)
	plt.xlabel('X Values')
	plt.ylabel('Occurances')
	plt.axvline(mu, lw=3, color='r', label='Real Mean')
	plt.axvline(mu-sig, lw=1, color='r', ls='-.')
	plt.axvline(mu+sig, lw=1, color='r', ls='-.')
	plt.legend()
	return 
		
