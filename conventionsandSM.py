#!/usr/bin/env python

from uncertainties import ufloat
from uncertainties.umath import sqrt

M_Z = 91.1876
Ga_Z = 2.4952
aL = -0.53762
aR = 0.46238
e = 0.8431872482432357  # = cL_lep = cR_lep from mod_Parameters
L1 = 10000.

g2HZZ = 1.65684
g4HZZ = 2.55052
g1prime2HZZ = -12100.42
ghzgs1prime2HZZ = -7613.351302119843
eLHZZ = sqrt(7.2310297E+00 / 1.4347981E+01)
eRHZZ = sqrt(7.2310297E+00 / 1.3952140E+00)

g2HWW = 1.133582
g4HWW = 1.76132
g1prime2HWW = -13752.22
ghzgs1prime2HWW = -1000

g2VBF = 0.27196538
g4VBF = 0.297979018705
g1prime2VBF = -2158.21307286
ghzgs1prime2VBF = -4091.051456694223

g2ZH = 0.112481
g4ZH = 0.144057
g1prime2ZH = -517.788
ghzgs1prime2ZH = -642.9534550379002

g2WH = 0.0998956
g4WH = 0.1236136
g1prime2WH = -525.274
ghzgs1prime2WH = -1000

g2VH = 0.10430356645812816 #sqrt((JHUXSZHa1 + JHUXSWHa1*normalize_WH_to_ZH) / (JHUXSZHa2 + JHUXSWHa2*normalize_WH_to_ZH))
g4VH = 0.13053750671388425 #sqrt((JHUXSZHa1 + JHUXSWHa1*normalize_WH_to_ZH) / (JHUXSZHa3 + JHUXSWHa3*normalize_WH_to_ZH))
g1prime2VH = -522.3034453633128 #-sqrt((JHUXSZHa1 + JHUXSWHa1*normalize_WH_to_ZH) / (JHUXSZHL1 + JHUXSWHL1*normalize_WH_to_ZH))
ghzgs1prime2VH = -1027.387141119873 #-sqrt((JHUXSZHa1 + JHUXSWHa1*normalize_WH_to_ZH) / (JHUXSZHL1Zg + JHUXSWHL1Zg*normalize_WH_to_ZH))
nominal_normalize_WH_to_ZH = 0.15070409765374365

ghg4HJJ = 1.0062
kappa_tilde_ttH = 1.6

#https://twiki.cern.ch/twiki/pub/LHCPhysics/LHCHXSWG/Higgs_XSBR_YR4_update.xlsx
SMXSggH   = (44.14      #'YR4 SM 13TeV'!B24   (ggH cross section, m=125)
              *1000)    #                     (pb to fb)
SMBR2e2mu =  5.897E-05  #'YR4 SM BR'!CO25     (2e2mu BR, m=125)
SMXSVBF   = (3.782E+00  #'YR4 SM 13TeV'!B24   (VBF cross section, m=125)
              *1000)    #                     (pb to fb)
SMXSWH    = (1.373E+00  #'YR4 SM 13TeV'!R24   (WH cross section, m=125)
              *1000)    #                     (pb to fb)
SMXSWpH   = (8.400E-01  #'YR4 SM 13TeV'!X24   (W+H cross section, m=125)
              *1000)    #                     (pb to fb)
SMXSWmH   = (5.328E-01  #'YR4 SM 13TeV'!X24   (W-H cross section, m=125)
              *1000)    #                     (pb to fb)
SMXSZH    = (8.839E-01  #'YR4 SM 13TeV'!AB24  (ZH cross section, m=125)
              *1000)    #                     (pb to fb)
SMXSttH   = (5.071E-01  #'YR4 SM 13TeV'!AK24  (ttH cross section, m=125)
              *1000)    #                     (pb to fb)

SMXSggH2e2mu = SMXSggH * SMBR2e2mu
SMXSVBF2e2mu = SMXSVBF * SMBR2e2mu
SMXSZH2e2mu  = SMXSZH * SMBR2e2mu
SMXSWH2e2mu  = SMXSWH * SMBR2e2mu
SMXSWpH2e2mu = SMXSWpH * SMBR2e2mu
SMXSWmH2e2mu = SMXSWmH * SMBR2e2mu
SMXSttH2e2mu = SMXSttH * SMBR2e2mu
