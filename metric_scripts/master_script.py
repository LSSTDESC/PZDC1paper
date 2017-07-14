
from __future__ import print_function, absolute_import

import argparse
import numpy as np
import qp

""" Script for injesting and processing photometric redshift data for the DESC
PhotoZ Working Group Data Callenge 1 (DC1).

The goal is compute summary plots and
statistics from the output PDFs of various photometric redshift estimation
codes. This script should be generalized enough to handle the outputs from
all the different codes used to process the DC1 data. To this end we use the
qp software package to injest and process the PDF data to avoid multiple
transformations and approximations that may degrade the information in the
PDFs and complicate the interpretation of our computed summaries.

The summaries we will use include qualitative and quanitative measures. They
are:

Qualitative
-----------
QQ Plot - Plots of CDF quantiles of probability and N(z) against the true N(z)
    of the simulated data. This gives a comparison of the overal PDF for a
    given sample of galaxies.

Quantitative
------------
RMSE - Root mean squared error on the a single point redshift estimate. Does
    not give full information on the PDf. Useful to have but may be shelved.
Kolmogorov-Smirnoff
Anderson Darling/Cramer von Mises
Kullback-Leibler - Full sample PDF compared to true N(z) distribution.
"""


def get_config(input_config):
    pass

if __name__ == "__main__":
    pass