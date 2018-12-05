#!/usr/bin/env python

import os

from uncertainties import ufloat

from conventionsandSM import *

JHUXSVBFa1                 = ufloat(     968.88143,     0.42919631)
JHUXSVBFa2                 = ufloat(     13097.831,       3.335825)
JHUXSVBFa3                 = ufloat(     10910.237,      3.2662293)
JHUXSVBFL1                 = ufloat( 0.00020829261,  7.6725395e-08)
JHUXSVBFL1Zg               = ufloat( 5.2902139e-05,  2.2868933e-08)
JHUXSVBFa1a2               = ufloat(     2207.6738,     0.73510552)
JHUXSVBFa1a3               = ufloat(     1936.4327,     0.72879437)
JHUXSVBFa1L1               = ufloat(     2861.7003,      1.0169832)
JHUXSVBFa1L1Zg             = ufloat(     1574.5833,     0.70680555)
JHUXSVBFa2a3               = ufloat(      1937.588,     0.55595604)
JHUXSVBFa2L1               = ufloat(     2507.7202,     0.81000667)
JHUXSVBFa2L1Zg             = ufloat(     1739.4331,     0.57641118)
JHUXSVBFa3L1               = ufloat(     1940.0653,     0.72555356)
JHUXSVBFa3L1Zg             = ufloat(     1853.7644,     0.65261692)
JHUXSVBFL1L1Zg             = ufloat(     1401.9816,     0.52582956)

JHUXSZHa1                  = ufloat(     1436880.4,        41.3837)
JHUXSZHa2                  = ufloat( 1.1360424e+08,      4939.2461)
JHUXSZHa3                  = ufloat(      69241514,      2046.1655)
JHUXSZHL1                  = ufloat(     5.3610896,  0.00014112226)
JHUXSZHL1Zg                = ufloat(     3.4592999,  8.0055009e-05)
JHUXSZHa1a2                = ufloat(     678434.94,      47.185897)
JHUXSZHa1a3                = ufloat(     2873685.9,      91.470217)
JHUXSZHa1L1                = ufloat(     1091656.8,      30.521123)
JHUXSZHa1L1Zg              = ufloat(       3480087,      99.293532)
JHUXSZHa2a3                = ufloat(     2874232.1,      91.487587)
JHUXSZHa2L1                = ufloat(     4488018.1,      136.45286)
JHUXSZHa2L1Zg              = ufloat(     2297889.6,      60.444464)
JHUXSZHa3L1                = ufloat(       2874124,       87.77159)
JHUXSZHa3L1Zg              = ufloat(     2866940.9,      76.407376)
JHUXSZHL1L1Zg              = ufloat(       1763624,      47.312104)

JHUXSWHa1                  = ufloat(      14813072,      324.03722)
JHUXSWHa2                  = ufloat( 1.4845783e+09,      58842.575)
JHUXSWHa3                  = ufloat( 9.6943028e+08,      25961.992)
JHUXSWHL1                  = ufloat(     53.687994,   0.0012413086)
JHUXSWHa1a2                = ufloat(     7879980.3,      450.51374)
JHUXSWHa1a3                = ufloat(      29626131,      764.40517)
JHUXSWHa1L1                = ufloat(      12092167,      286.51514)
JHUXSWHa2a3                = ufloat(      29628463,        917.628)
JHUXSWHa2L1                = ufloat(      44769608,      1129.0058)
JHUXSWHa3L1                = ufloat(      29624425,      765.59044)

JHUXSHJJa2                 = ufloat(      14583.61,           0.94)
JHUXSHJJa3                 = ufloat(      14397.13,           0.97)
JHUXSHJJa2a3               = ufloat(       29169.2,            2.1)

JHUXSttHkappa              = ufloat(0.912135589,        0.00143032)
JHUXSttHkappatilde         = ufloat(0.35609194,        0.000492662)
JHUXSttHkappakappatilde    = ufloat(1.8231162489,       0.00254131)

JHUXSggZHa1                = ufloat(     55.231245,    0.013851438)
JHUXSggZHa2                = ufloat(     646688.83,      95.353549)
JHUXSggZHL1                = ufloat(  0.0011448724,  1.6894815e-07)
JHUXSggZHL1Zg              = ufloat( 1.6539803e-08,  3.5429326e-12)
JHUXSggZHa1a2              = ufloat(     40.049365,    0.008315672)
JHUXSggZHa1L1              = ufloat(     38.873281,   0.0080381603)
JHUXSggZHa1L1Zg            = ufloat(     113.62989,    0.032448764)
JHUXSggZHa2L1              = ufloat(     220.89541,    0.032586896)
JHUXSggZHa2L1Zg            = ufloat(     108.41597,    0.024144907)
JHUXSggZHL1L1Zg            = ufloat(      108.4218,    0.024102713)

JHUXSggZHkappa             = ufloat(     45.639566,   0.0095356748)
JHUXSggZHkappatilde        = ufloat(      50.83718,     0.00940342)

JHUXSggZHkappakappatilde   = ufloat(     91.269129,    0.017922304)

JHUXSggZHa1kappa           = ufloat(     10.422093,   0.0031661331)
JHUXSggZHa2kappa           = ufloat(     181.20091,    0.030181201)
JHUXSggZHL1kappa           = ufloat(     182.00828,    0.030399493)
JHUXSggZHL1Zgkappa         = ufloat(     98.241292,    0.024470784)

JHUXSggZHa1kappatilde      = ufloat(     100.84628,    0.021089319)
JHUXSggZHa2kappatilde      = ufloat(     100.86741,    0.015308484)
JHUXSggZHL1kappatilde      = ufloat(      100.8596,    0.015353585)
JHUXSggZHL1Zgkappatilde    = ufloat(     100.89172,    0.024879389)

execfile(os.path.join(os.path.dirname(__file__), "adjustdefinitions.py"))
