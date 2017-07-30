import numpy as np
import qp
import matplotlib.pyplot as plt


class EvaluateMetric(object):
    def __init__(self,ensemble_obj,truths):
        """an object that takes a qp Ensemble of N PDF objects and an array of
        N "truth" specz's, will be used to calculate PIT and QQ, plus more stuff
        later
        Parameters:
        ensemble_obj: qp ensemble 
            a qp ensemble object containing the N PDFs
        truths: numpy array 
            1D numpy array with the N spec-z values
        """

#        if ensemble_obj==None or truths==None:
#            print 'Warning: inputs not complete'
        self.ensemble_obj = ensemble_obj
        self.truths = truths
        

    def PIT(self,using='gridded',dx=0.0001):
         """ computes the Probability Integral Transform (PIT), described in 
        Tanaka et al. 2017(ArXiv 1704.05988), which is the integral of the 
        PDF from 0 to zref.
        Parameters:
        using: string
             which parameterization to evaluate
        dx: float
             step size used in integral
        Returns
        -------
        ndarray
             The values of the PIT for each ensemble object
        """
         if len(self.truths) != self.ensemble_obj.n_pdfs:
             print 'Warning: number of zref values not equal to number of ensemble objects'
             return
         n = self.ensemble_obj.n_pdfs
         pitlimits = np.zeros([n,2])
         pitlimits[:,1] = self.truths
         return self.ensemble_obj.integrate(limits=pitlimits,using=using,dx=dx)

    def QQplot(self,using,dx=0.0001,Nquants=101):
        """Quantile quantile plot for the ensemble using the PIT values, 
        simply take the percentiles of the values in order to get the Qdata
        quantiles
        Parameters:
        using: string
            which parameterization to evaluate
        dx: float
            step size for integral
        Nquants: int
            the number of quantile bins to compute, default 100
        Returns
        -------
        matplotlib plot of the quantiles
        """
        pits = self.PIT(using=using,dx=dx)
        quants = np.linspace(0.,100.,Nquants)
        QTheory = quants/100.
        Qdata = np.percentile(pits,quants)
        plt.figure(figsize=(10,10))
        plt.plot(QTheory,Qdata,c='b',linestyle='-',linewidth=3,label='QQ')
        plt.plot([0,1],[0,1],color='k',linestyle='-',linewidth=2)
        plt.xlabel("Qtheory",fontsize=18)
        plt.ylabel("Qdata",fontsize=18)
        plt.legend()
        plt.savefig("QQplot.jpg")
        return
