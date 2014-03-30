## Libraries

from __future__ import division

import numpy as np
import scipy.stats as stats
import numpy.random
import pylab
import matplotlib.pyplot as plt
from numpy.random import normal
from functools import partial
from numpy import *


def central_limit_theorem():
  """
  Just drawing graph for random values
  """
  sample_size = 5
  averages = [numpy.average(numpy.random.randint(1, 100, sample_size) )for i in xrange(100)]
  pylab.hist(averages)
  pylab.show()

def show_gaussian_histogram(x):
  """
  Drawing gaussian histogram
  """
  gaussian_numbers = normal(size=1000)
  plt.hist(gaussian_numbers,bins=20,normed=x)
  ## Bins show the number of bins and normed=true is for normalization
  plt.title("Gaussian Histogram with Normalization = %s"%x)
  plt.xlabel("Value")
  plt.ylabel("Frequency")
  plt.show()

def clt_observation():
  """
    Central limit theorem shown by taking one flat samples and one
    exponential samples
  """
  N=10000 #number of samples
  nobb=101 # number of bin boundaries
  n=np.array([1,2,3,5,10,100]) # number of samples to average over

  exp_mean=3 # mean of exponential distribution

  dist=[partial(np.random.random),partial(np.random.exponential,exp_mean)]
  title_names=["Flat", "Exponential (mean=%.1f)" % exp_mean]
  drange=np.array([[0,1],[0,10]]) # ranges of distributions
  means=np.array([0.5,exp_mean]) # means of distributions
  var=np.array([1/12,exp_mean**2]) # variances of distributions

  binrange=np.array([np.linspace(p,q,nobb) for p,q in drange])
  ln,ld=len(n),len(dist)
  plt.figure(figsize=((ld*6)+1,(ln*1.8)+1))

  for i in xrange(ln): # loop over number of n samples to average over
      for j in xrange(ld): # loop over the different distributions
          plt.subplot(ln,ld,i*ld+1+j)
          plt.hist(np.mean(dist[j]((N,n[i])),1),binrange[j],normed=True)
          plt.xlim(drange[j])
          if j==0:
              plt.ylabel('n=%i' % n[i],fontsize=15)        
          if i==0:
              plt.title(title_names[j], fontsize=15)
          else:
              clt=(1/(np.sqrt(2*np.pi*var[j]/n[i])))*exp(-(((binrange[j]-means[j])**2)*n[i]/(2*var[j])))
              plt.plot(binrange[j],clt,'r',linewidth=2)     
  plt.show()

central_limit_theorem()
show_gaussian_histogram(True)
show_gaussian_histogram(False)
clt_observation()

