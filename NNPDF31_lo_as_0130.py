#!/usr/bin/env python

import os

from uncertainties import ufloat

from conventionsandSM import *

JHUXSVBFa1                 = ufloat(     941.57048,     0.34686523)
JHUXSVBFa2                 = ufloat(     12619.356,      2.6989174)
JHUXSVBFa3                 = ufloat(     10519.885,      2.5837494)
JHUXSVBFL1                 = ufloat(  0.0002001356,  6.1467931e-08)
JHUXSVBFL1Zg               = ufloat( 5.2176724e-05,  1.6982223e-08)
JHUXSVBFa1a2               = ufloat(     2134.1946,     0.58901234)
JHUXSVBFa1a3               = ufloat(     1875.0082,     0.58136703)
JHUXSVBFa1L1               = ufloat(     2770.2344,     0.82519024)
JHUXSVBFa1L1Zg             = ufloat(     1542.4263,     0.58679609)
JHUXSVBFa2a3               = ufloat(     1867.2564,     0.44950073)
JHUXSVBFa2L1               = ufloat(     2411.1352,     0.64292253)
JHUXSVBFa2L1Zg             = ufloat(     1697.2068,     0.48036423)
JHUXSVBFa3L1               = ufloat(     1865.7634,     0.58980359)
JHUXSVBFa3L1Zg             = ufloat(     1806.4448,     0.54648598)
JHUXSVBFL1L1Zg             = ufloat(     1368.6758,     0.42579034)

JHUXSZHa1                  = ufloat(     1497785.3,       40.51122)
JHUXSZHa2                  = ufloat( 1.1957892e+08,      23179.304)
JHUXSZHa3                  = ufloat(      73262678,      2013.3648)
JHUXSZHL1                  = ufloat(     5.7277356,  0.00014175093)
JHUXSZHL1Zg                = ufloat(       3.70418,  8.1970284e-05)
JHUXSZHa1a2                = ufloat(     717663.93,       146.4283)
JHUXSZHa1a3                = ufloat(     3018127.9,      89.080721)
JHUXSZHa1L1                = ufloat(     1162376.6,      29.996439)
JHUXSZHa1L1Zg              = ufloat(       3676698,      100.29216)
JHUXSZHa2a3                = ufloat(     3033429.4,      109.98754)
JHUXSZHa2L1                = ufloat(     4747697.2,      167.46891)
JHUXSZHa2L1Zg              = ufloat(     2441401.6,      62.878625)
JHUXSZHa3L1                = ufloat(     3055861.7,      87.227326)
JHUXSZHa3L1Zg              = ufloat(     3051625.3,      75.215698)
JHUXSZHL1L1Zg              = ufloat(     1886096.8,      48.159171)

JHUXSWHa1                  = ufloat(      15366303,      301.19426)
JHUXSWHa2                  = ufloat(  1.558994e+09,      157847.17)
JHUXSWHa3                  = ufloat(  1.023799e+09,      21979.733)
JHUXSWHL1                  = ufloat(     58.457074,   0.0012385951)
JHUXSWHa1a2                = ufloat(  float("nan"),   float("nan"))
JHUXSWHa1a3                = ufloat(      31010468,      669.34236)
JHUXSWHa1L1                = ufloat(      13144777,      283.47367)
JHUXSWHa2a3                = ufloat(      31204114,      975.07201)
JHUXSWHa2L1                = ufloat(      47596734,      1124.0434)
JHUXSWHa3L1                = ufloat(      31773358,      677.46665)

#JHUGen returned nan several hundred times for WHa1a2.
#Try to estimate it from other numbers
#(in a function to avoid exposing local variables)
def JHUXSWHa1a2():
  import NNPDF30_lo_as_0130, numpy
  WH31_over_WH30 = [
    JHUXSWHa1 / NNPDF30_lo_as_0130.JHUXSWHa1,
    JHUXSWHa2 / NNPDF30_lo_as_0130.JHUXSWHa2,
    JHUXSWHa3 / NNPDF30_lo_as_0130.JHUXSWHa3,
    JHUXSWHL1 / NNPDF30_lo_as_0130.JHUXSWHL1,
    (JHUXSWHa1L1 - JHUXSWHa1           - JHUXSWHL1 * g1prime2WH**2) /         g1prime2WH  / NNPDF30_lo_as_0130.JHUXSWHa1L1,
    (JHUXSWHa2L1 - JHUXSWHa2 * g2WH**2 - JHUXSWHL1 * g1prime2WH**2) / (g2WH * g1prime2WH) / NNPDF30_lo_as_0130.JHUXSWHa2L1,
  ]
  ZH31_over_ZH30 = [
    JHUXSZHa1 / NNPDF30_lo_as_0130.JHUXSZHa1,
    JHUXSZHa2 / NNPDF30_lo_as_0130.JHUXSZHa2,
    JHUXSZHa3 / NNPDF30_lo_as_0130.JHUXSZHa3,
    JHUXSZHL1 / NNPDF30_lo_as_0130.JHUXSZHL1,
    (JHUXSZHa1L1 - JHUXSZHa1           - JHUXSZHL1 * g1prime2ZH**2) /         g1prime2ZH  / NNPDF30_lo_as_0130.JHUXSZHa1L1,
    (JHUXSZHa2L1 - JHUXSZHa2 * g2ZH**2 - JHUXSZHL1 * g1prime2ZH**2) / (g2ZH * g1prime2ZH) / NNPDF30_lo_as_0130.JHUXSZHa2L1,
  ]
  WH31_ZH30_over_WH30_ZH31 = [
    WH / ZH for WH, ZH in zip(WH31_over_WH30, ZH31_over_ZH30)
  ]
  average = numpy.mean(WH31_ZH30_over_WH30_ZH31)
  averageerror = average.std_dev
  average = average.nominal_value
  stddev = numpy.std([_.nominal_value for _ in WH31_ZH30_over_WH30_ZH31])
  averageerror = (averageerror ** 2 + stddev ** 2) ** .5

  interference = ufloat(average, averageerror) * (
    (JHUXSZHa1a2 - JHUXSZHa1 - JHUXSZHa2 * g2ZH**2) / g2ZH
  ) * (
    NNPDF30_lo_as_0130.JHUXSWHa1a2 / NNPDF30_lo_as_0130.JHUXSZHa1a2
  )

  return interference * g2WH + JHUXSWHa1 + JHUXSWHa2 * g2WH**2

JHUXSWHa1a2 = JHUXSWHa1a2()

JHUXSHJJa2                 = ufloat(     14872.334,      4.6483102)
JHUXSHJJa3                 = ufloat(     14679.974,      4.7524727)
JHUXSHJJa2a3               = ufloat(     29728.575,      9.4642949)

JHUXSttHkappa              = ufloat(     3.1444673,  0.00029462345)
JHUXSttHkappatilde         = ufloat(     1.2078654,  0.00010920319)
JHUXSttHkappakappatilde    = ufloat(     6.2361268,   0.0005487899)

execfile(os.path.join(os.path.dirname(__file__), "adjustdefinitions.py"))
