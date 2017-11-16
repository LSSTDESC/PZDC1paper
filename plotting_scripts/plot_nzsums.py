#file to read in all the point pz data
#Oct 12, 2017
import sys,os
import numpy as np
import matplotlib.pyplot as plt


def main(argv):
    basepathpart = "./TESTDC1"
    codes = ("ANNZ2","BPZ","EAZY","FLEXZ","GPZ","METAPHOR","SKYNET","TPZ")
    labels = ("ANNz2","BPZ","EAZY","FlexZBoost","GPz","METAPhoR","SkyNet","TPZ")
    labeldict = dict(zip(codes,labels))
    
    nzvectorfile = "NZPLOT_vectors.out"
    
    numcodes = len(codes)
    numzs = 2001 #number of zbins in each NZPLOT_vectors.out file
    szvals = np.zeros([numcodes,numzs])
    pzvals = np.zeros([numcodes,numzs])
    z_array = np.zeros(numzs)

    for i,xfile in enumerate(codes):
        direcpath = "%s%s"%(basepathpart,xfile)
        fullpath = os.path.join(direcpath,nzvectorfile)
        #print fullpath
        data = np.loadtxt(fullpath,skiprows=1)
        if i == 0:
            z_array = data[:,0]
        szvals[i,:] = data[:,1]
        pzvals[i,:] = data[:,2]
        print "read in data for %s"%xfile
        


  
    numrows = 2
    numcols = 4


    fig,axes = plt.subplots(numcodes, sharex=True, sharey=True, figsize=(12,6))
    fig.subplots_adjust(hspace=0.0)
    fig.subplots_adjust(wspace=0.0)
    
    for i in range(numcodes):
        ax = plt.subplot(numrows,numcols,i+1)
        plt.plot(z_array,szvals[i],c='b',linestyle='-',linewidth=2,label="zspec KDE sum")
        tmplabel = "%s N(z) sum"%(labels[i])
        plt.plot(z_array,pzvals[i],color='r',linestyle='-',linewidth=2,label=tmplabel)
      
        ax.set_xlim([0.0,1.99])
        ax.set_ylim([0.0,1.99])
        ax.legend(loc="upper left",fontsize=12)
        if (i<(numcodes-5)):
            ax.set_xticklabels([])
        else:
            ax.set_xlabel("redshift",fontsize=18)
        if i%4==0:
            ax.set_ylabel("N(z)",fontsize=15)
        else:
            ax.set_yticklabels([])

   
    plt.savefig("NZsumplot_10codes.jpg",format='jpg')
    plt.show()

if __name__=="__main__":
    main(sys.argv)
