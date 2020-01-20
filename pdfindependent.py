#!/usr/bin/env python

from __future__ import print_function
from __future__ import absolute_import
from uncertainties import ufloat
from uncertainties.umath import sqrt

from .conventionsandSM import *

JHUXSHZZ2e2mua1             = ufloat(     7.1517044,  0.00027591496) / 2
JHUXSHZZ2e2mua2             = ufloat(     2.5850323,  0.00010874196) / 2
JHUXSHZZ2e2mua3             = ufloat(      1.095479,  5.6780596e-05) / 2
JHUXSHZZ2e2muL1             = ufloat( 4.8755556e-08,    1.75784e-12) / 2
JHUXSHZZ2e2muL1Zg           = ufloat( 1.2489117e-07,  5.6567346e-12) / 2
JHUXSHZZ2e2mua1a2           = ufloat(     26.074307,  0.00094875635) / 2
JHUXSHZZ2e2mua1a3           = ufloat(     14.277409,   0.0005409516) / 2
JHUXSHZZ2e2mua1L1           = ufloat(    0.23726108,  2.1955163e-05) / 2
JHUXSHZZ2e2mua1L1Zg         = ufloat(     13.220602,  0.00053706572) / 2
JHUXSHZZ2e2mua2a3           = ufloat(     14.221651,  0.00063763008) / 2
JHUXSHZZ2e2mua2L1           = ufloat(     2.3200652,  0.00014040255) / 2
JHUXSHZZ2e2mua2L1Zg         = ufloat(     13.391687,  0.00049246945) / 2
JHUXSHZZ2e2mua3L1           = ufloat(     14.264343,  0.00051778249) / 2
JHUXSHZZ2e2mua3L1Zg         = ufloat(     14.364768,  0.00054679129) / 2
JHUXSHZZ2e2muL1L1Zg         = ufloat(     15.488892,  0.00063476605) / 2

JHUXSHZZ2e2mueL = 1.4347981E+01 / 2
JHUXSHZZ2e2mueR = 1.3952140E+01 / 2

def fractionofevents(k, n):
  """https://indico.cern.ch/event/66256/contributions/2071577/attachments/1017176/1447814/EfficiencyErrors.pdf"""
  k = 1.0 * k
  n = 1.0 * n
  return ufloat(k/n, sqrt((k+1)*(k+2)/((n+2)*(n+3)) - (k+1)**2/(n+2)**2))

JHUXSHZZ4la1                = JHUXSHZZ2e2mua1 / fractionofevents(481392, 2213962)
JHUXSHZZ4la2                = JHUXSHZZ2e2mua2 / fractionofevents(328041, 1457394)
JHUXSHZZ4la3                = JHUXSHZZ2e2mua3 / fractionofevents(335387, 1454067)
JHUXSHZZ4lL1                = JHUXSHZZ2e2muL1 / fractionofevents(328209, 1473060)
JHUXSHZZ4lL1Zg              = JHUXSHZZ2e2muL1Zg / fractionofevents(199932, 952440)
JHUXSHZZ4la1a2              = JHUXSHZZ2e2mua1a2 / fractionofevents(104189, 474877)
JHUXSHZZ4la1a3              = JHUXSHZZ2e2mua1a3 / fractionofevents(110420, 496912)
JHUXSHZZ4la1L1              = JHUXSHZZ2e2mua1L1 / fractionofevents(99542, 500000)
JHUXSHZZ4la1L1Zg            = JHUXSHZZ2e2mua1L1Zg / fractionofevents(107541, 500000)
#JHUXSHZZ4la2a3              = JHUXSHZZ2e2mua2a3 / fractionofevents(
#JHUXSHZZ4la2L1              = JHUXSHZZ2e2mua2L1 / fractionofevents(
#JHUXSHZZ4la2L1Zg            = JHUXSHZZ2e2mua2L1Zg / fractionofevents(
#JHUXSHZZ4la3L1              = JHUXSHZZ2e2mua3L1 / fractionofevents(
#JHUXSHZZ4la3L1Zg            = JHUXSHZZ2e2mua3L1Zg / fractionofevents(
#JHUXSHZZ4lL1L1Zg            = JHUXSHZZ2e2muL1L1Zg / fractionofevents(

del fractionofevents

JHUXSHWWa1                  = ufloat(     312.04019,    0.021123201)
JHUXSHWWa2                  = ufloat(      242.6283,    0.018655548)
JHUXSHWWa3                  = ufloat(     100.79135,   0.0076985693)
JHUXSHWWL1                  = ufloat( 1.6475531e-06,  1.1297587e-10)
JHUXSHWWa1a2                = ufloat(     1149.9181,       0.085554)
JHUXSHWWa1a3                = ufloat(      624.7195,    0.046033017)
JHUXSHWWa1L1                = ufloat(     5.3585509,  0.00056067121)
JHUXSHWWa2a3                = ufloat(     624.55269,    0.046795651)
JHUXSHWWa2L1                = ufloat(     83.700384,   0.0062011144)
JHUXSHWWa3L1                = ufloat(     624.23611,    0.045827636)

JHUXSHWWL1Zg                = 0
JHUXSHWWa1L1Zg              = JHUXSHWWa1
JHUXSHWWa2L1Zg              = g2HWW**2 * JHUXSHWWa2
JHUXSHWWa3L1Zg              = g4HWW**2 * JHUXSHWWa3
JHUXSHWWL1L1Zg              = g1prime2HWW**2 * JHUXSHWWL1

#Subtract the pure component from the interference, then divide by (gi*gj)
JHUXSHZZ2e2mua1a2   = (JHUXSHZZ2e2mua1a2   -                  JHUXSHZZ2e2mua1 - g2HZZ          **2 * JHUXSHZZ2e2mua2  ) / (g2HZZ                            )
JHUXSHZZ2e2mua1a3   = (JHUXSHZZ2e2mua1a3   -                  JHUXSHZZ2e2mua1 - g4HZZ          **2 * JHUXSHZZ2e2mua3  ) / (g4HZZ                            )
JHUXSHZZ2e2mua1L1   = (JHUXSHZZ2e2mua1L1   -                  JHUXSHZZ2e2mua1 - g1prime2HZZ    **2 * JHUXSHZZ2e2muL1  ) / (g1prime2HZZ                      )
JHUXSHZZ2e2mua1L1Zg = (JHUXSHZZ2e2mua1L1Zg -                  JHUXSHZZ2e2mua1 - ghzgs1prime2HZZ**2 * JHUXSHZZ2e2muL1Zg) / (ghzgs1prime2HZZ                  )
JHUXSHZZ2e2mua2a3   = (JHUXSHZZ2e2mua2a3   - g2HZZ      **2 * JHUXSHZZ2e2mua2 - g4HZZ          **2 * JHUXSHZZ2e2mua3  ) / (g2HZZ           * g4HZZ          )
JHUXSHZZ2e2mua2L1   = (JHUXSHZZ2e2mua2L1   - g2HZZ      **2 * JHUXSHZZ2e2mua2 - g1prime2HZZ    **2 * JHUXSHZZ2e2muL1  ) / (g2HZZ           * g1prime2HZZ    )
JHUXSHZZ2e2mua2L1Zg = (JHUXSHZZ2e2mua2L1Zg - g2HZZ      **2 * JHUXSHZZ2e2mua2 - ghzgs1prime2HZZ**2 * JHUXSHZZ2e2muL1Zg) / (g2HZZ           * ghzgs1prime2HZZ)
JHUXSHZZ2e2mua3L1   = (JHUXSHZZ2e2mua3L1   - g4HZZ      **2 * JHUXSHZZ2e2mua3 - g1prime2HZZ    **2 * JHUXSHZZ2e2muL1  ) / (g4HZZ           * g1prime2HZZ    )
JHUXSHZZ2e2mua3L1Zg = (JHUXSHZZ2e2mua3L1Zg - g4HZZ      **2 * JHUXSHZZ2e2mua3 - ghzgs1prime2HZZ**2 * JHUXSHZZ2e2muL1Zg) / (g4HZZ           * ghzgs1prime2HZZ)
JHUXSHZZ2e2muL1L1Zg = (JHUXSHZZ2e2muL1L1Zg - g1prime2HZZ**2 * JHUXSHZZ2e2muL1 - ghzgs1prime2HZZ**2 * JHUXSHZZ2e2muL1Zg) / (g1prime2HZZ     * ghzgs1prime2HZZ)

JHUXSHZZ4la1a2      = (JHUXSHZZ4la1a2      -                  JHUXSHZZ4la1    - g2HZZ          **2 * JHUXSHZZ4la2     ) / (g2HZZ                            )
JHUXSHZZ4la1a3      = (JHUXSHZZ4la1a3      -                  JHUXSHZZ4la1    - g4HZZ          **2 * JHUXSHZZ4la3     ) / (g4HZZ                            )
JHUXSHZZ4la1L1      = (JHUXSHZZ4la1L1      -                  JHUXSHZZ4la1    - g1prime2HZZ    **2 * JHUXSHZZ4lL1     ) / (g1prime2HZZ                      )
JHUXSHZZ4la1L1Zg    = (JHUXSHZZ4la1L1Zg    -                  JHUXSHZZ4la1    - ghzgs1prime2HZZ**2 * JHUXSHZZ4lL1Zg   ) / (ghzgs1prime2HZZ                  )
#JHUXSHZZ4la2a3      = (JHUXSHZZ4la2a3      - g2HZZ      **2 * JHUXSHZZ4la2    - g4HZZ          **2 * JHUXSHZZ4la3     ) / (g2HZZ           * g4HZZ          )
#JHUXSHZZ4la2L1      = (JHUXSHZZ4la2L1      - g2HZZ      **2 * JHUXSHZZ4la2    - g1prime2HZZ    **2 * JHUXSHZZ4lL1     ) / (g2HZZ           * g1prime2HZZ    )
#JHUXSHZZ4la2L1Zg    = (JHUXSHZZ4la2L1Zg    - g2HZZ      **2 * JHUXSHZZ4la2    - ghzgs1prime2HZZ**2 * JHUXSHZZ4lL1Zg   ) / (g2HZZ           * ghzgs1prime2HZZ)
#JHUXSHZZ4la3L1      = (JHUXSHZZ4la3L1      - g4HZZ      **2 * JHUXSHZZ4la3    - g1prime2HZZ    **2 * JHUXSHZZ4lL1     ) / (g4HZZ           * g1prime2HZZ    )
#JHUXSHZZ4la3L1Zg    = (JHUXSHZZ4la3L1Zg    - g4HZZ      **2 * JHUXSHZZ4la3    - ghzgs1prime2HZZ**2 * JHUXSHZZ4lL1Zg   ) / (g4HZZ           * ghzgs1prime2HZZ)
#JHUXSHZZ4lL1L1Zg    = (JHUXSHZZ4lL1L1Zg    - g1prime2HZZ**2 * JHUXSHZZ4lL1    - ghzgs1prime2HZZ**2 * JHUXSHZZ4lL1Zg   ) / (g1prime2HZZ     * ghzgs1prime2HZZ)

JHUXSHWWa1a2         = (JHUXSHWWa1a2        -                  JHUXSHWWa1      - g2HWW          **2 * JHUXSHWWa2       ) / (g2HWW                            )
JHUXSHWWa1a3         = (JHUXSHWWa1a3        -                  JHUXSHWWa1      - g4HWW          **2 * JHUXSHWWa3       ) / (g4HWW                            )
JHUXSHWWa1L1         = (JHUXSHWWa1L1        -                  JHUXSHWWa1      - g1prime2HWW    **2 * JHUXSHWWL1       ) / (g1prime2HWW                      )
JHUXSHWWa1L1Zg       = 0
JHUXSHWWa2a3         = (JHUXSHWWa2a3        - g2HWW      **2 * JHUXSHWWa2      - g4HWW          **2 * JHUXSHWWa3       ) / (g2HWW           * g4HWW          )
JHUXSHWWa2L1         = (JHUXSHWWa2L1        - g2HWW      **2 * JHUXSHWWa2      - g1prime2HWW    **2 * JHUXSHWWL1       ) / (g2HWW           * g1prime2HWW    )
JHUXSHWWa2L1Zg       = 0
JHUXSHWWa3L1         = (JHUXSHWWa3L1        - g4HWW      **2 * JHUXSHWWa3      - g1prime2HWW    **2 * JHUXSHWWL1       ) / (g4HWW           * g1prime2HWW    )
JHUXSHWWa3L1Zg       = 0
JHUXSHWWL1L1Zg       = 0

if __name__ == "__main__":
    print("==============================================")
    print("All of the following should be around 0")
    print("(if they're huge that indicates a mistake)")
    print("(but if they're not within errors that's fine)")
    print("==============================================")
    print()
    print("  decay to 2e2mu:")
    print("    a1XS -           g2**2*    a2XS = {:%}".format((JHUXSHZZ2e2mua1 - g2HZZ**2           * JHUXSHZZ2e2mua2    ) / JHUXSHZZ2e2mua1))
    print("    a1XS -           g4**2*    a3XS = {:%}".format((JHUXSHZZ2e2mua1 - g4HZZ**2           * JHUXSHZZ2e2mua3    ) / JHUXSHZZ2e2mua1))
    print("    a1XS -     g1prime2**2*    L1XS = {:%}".format((JHUXSHZZ2e2mua1 - g1prime2HZZ**2     * JHUXSHZZ2e2muL1    ) / JHUXSHZZ2e2mua1))
    print("    a1XS - ghzgs1prime2**2*  L1ZgXS = {:%}".format((JHUXSHZZ2e2mua1 - ghzgs1prime2HZZ**2 * JHUXSHZZ2e2muL1Zg  ) / JHUXSHZZ2e2mua1))
    print("                        g4*  a1a3XS = {:%}".format((                 g4HZZ              * JHUXSHZZ2e2mua1a3  ) / JHUXSHZZ2e2mua1))
    print("                     g2*g4*  a2a3XS = {:%}".format((                 g2HZZ*g4HZZ        * JHUXSHZZ2e2mua2a3  ) / JHUXSHZZ2e2mua1))
    print("               g1prime2*g4*  a3L1XS = {:%}".format((                 g1prime2HZZ*g4HZZ  * JHUXSHZZ2e2mua3L1  ) / JHUXSHZZ2e2mua1))
    print("           ghzgs1prime2*g4*a3L1ZgXS = {:%}".format((             ghzgs1prime2HZZ*g4HZZ  * JHUXSHZZ2e2mua3L1Zg) / JHUXSHZZ2e2mua1))
    print()
    print("  decay to any 4l:")
    print("    a1XS -           g2**2*    a2XS = {:%}".format((JHUXSHZZ4la1    - g2HZZ**2           * JHUXSHZZ4la2       ) / JHUXSHZZ4la1   ))
    print("    a1XS -           g4**2*    a3XS = {:%}".format((JHUXSHZZ4la1    - g4HZZ**2           * JHUXSHZZ4la3       ) / JHUXSHZZ4la1   ))
    print("    a1XS -     g1prime2**2*    L1XS = {:%}".format((JHUXSHZZ4la1    - g1prime2HZZ**2     * JHUXSHZZ4lL1       ) / JHUXSHZZ4la1   ))
    print("    a1XS - ghzgs1prime2**2*  L1ZgXS = {:%}".format((JHUXSHZZ4la1    - ghzgs1prime2HZZ**2 * JHUXSHZZ4lL1Zg     ) / JHUXSHZZ4la1   ))
    print("                        g4*  a1a3XS = {:%}".format((                  g4HZZ              * JHUXSHZZ4la1a3     ) / JHUXSHZZ4la1   ))
#    print "                     g2*g4*  a2a3XS = {:%}".format((                  g2HZZ*g4HZZ        * JHUXSHZZ4la2a3     ) / JHUXSHZZ4la1   )
#    print "               g1prime2*g4*  a3L1XS = {:%}".format((                  g1prime2HZZ*g4HZZ  * JHUXSHZZ4la3L1     ) / JHUXSHZZ4la1   )
#    print "           ghzgs1prime2*g4*a3L1ZgXS = {:%}".format((              ghzgs1prime2HZZ*g4HZZ  * JHUXSHZZ4la3L1Zg   ) / JHUXSHZZ4la1   )
    print()
    print("  HWW:")
    print("    a1XS -           g2**2*    a2XS = {:%}".format((JHUXSHWWa1      - g2HWW**2           * JHUXSHWWa2         ) / JHUXSHWWa1     ))
    print("    a1XS -           g4**2*    a3XS = {:%}".format((JHUXSHWWa1      - g4HWW**2           * JHUXSHWWa3         ) / JHUXSHWWa1     ))
    print("    a1XS -     g1prime2**2*    L1XS = {:%}".format((JHUXSHWWa1      - g1prime2HWW**2     * JHUXSHWWL1         ) / JHUXSHWWa1     ))
#   print "    a1XS - ghzgs1prime2**2*  L1ZgXS = {:%}".format((JHUXSHWWa1      - ghzgs1prime2HWW**2 * JHUXSHWWL1Zg       ) / JHUXSHWWa1     )
    print("                        g4*  a1a3XS = {:%}".format((                  g4HWW              * JHUXSHWWa1a3       ) / JHUXSHWWa1     ))
    print("                     g2*g4*  a2a3XS = {:%}".format((                  g2HWW  *g4HWW      * JHUXSHWWa2a3       ) / JHUXSHWWa1     ))
    print("               g1prime2*g4*  a3L1XS = {:%}".format((                 g1prime2HWW  *g4HWW * JHUXSHWWa3L1       ) / JHUXSHWWa1     ))
#   print "           ghzgs1prime2*g4*a3L1ZgXS = {:%}".format((             ghzgs1prime2HWW  *g4HWW * JHUXSHWWa3L1Zg     ) / JHUXSHWWa1     )
    print()

#Set them to exactly 0

JHUXSHZZ2e2mua1a3   = \
JHUXSHZZ2e2mua2a3   = \
JHUXSHZZ2e2mua3L1   = \
JHUXSHZZ2e2mua3L1Zg = 0

JHUXSHZZ4la1a3      = \
JHUXSHZZ4la2a3      = \
JHUXSHZZ4la3L1      = \
JHUXSHZZ4la3L1Zg    = 0

JHUXSHWWa1a3    = \
JHUXSHWWa2a3    = \
JHUXSHWWa3L1    = \
JHUXSHWWL1Zg    = \
JHUXSHWWa1L1Zg  = \
JHUXSHWWa2L1Zg  = \
JHUXSHWWa3L1Zg  = \
JHUXSHWWL1L1Zg  = 0

#defined this way, just make sure
for _ in """
  JHUXSHZZ2e2mua1a3 JHUXSHZZ2e2mua2a3 JHUXSHZZ2e2mua3L1 JHUXSHZZ2e2mua3L1Zg
  JHUXSHZZ4la1a3    JHUXSHZZ4la2a3    JHUXSHZZ4la3L1    JHUXSHZZ4la3L1Zg
  JHUXSHWWa1a3  JHUXSHWWa2a3  JHUXSHWWa3L1
  JHUXSHWWL1Zg  JHUXSHWWa1L1Zg  JHUXSHWWa2L1Zg  JHUXSHWWa3L1Zg  JHUXSHWWL1L1Zg
""".split():
  assert globals()[_] == 0, (_, globals()[_])
for k, v in list(globals().items()):
    if "__" in k: continue
    assert v is not None, k
del k, v, _

if __name__ == "__main__":
    print("=================================================================")
    print("pure cross sections are for ai=1.")
    print("interference cross sections are for ai=aj=1, minus the pure terms")
    print("=================================================================")
    print()
    print("============")
    print("H->ZZ->2e2mu")
    print("============")
    print()
    print("a1:    ", JHUXSHZZ2e2mua1)
    print("a2:    ", JHUXSHZZ2e2mua2)
    print("a3:    ", JHUXSHZZ2e2mua3)
    print("L1:    ", JHUXSHZZ2e2muL1)
    print("L1Zg:  ", JHUXSHZZ2e2muL1Zg)
    print()
    print("a1a2:  ", JHUXSHZZ2e2mua1a2)
    print("a1a3:  ", JHUXSHZZ2e2mua1a3)
    print("a1L1:  ", JHUXSHZZ2e2mua1L1)
    print("a1L1Zg:", JHUXSHZZ2e2mua1L1Zg)
    print("a2a3:  ", JHUXSHZZ2e2mua2a3)
    print("a2L1:  ", JHUXSHZZ2e2mua2L1)
    print("a2L1Zg:", JHUXSHZZ2e2mua2L1Zg)
    print("a3L1:  ", JHUXSHZZ2e2mua3L1)
    print("a3L1Zg:", JHUXSHZZ2e2mua3L1Zg)
    print("L1L1Zg:", JHUXSHZZ2e2muL1L1Zg)
    print()
    print("=========")
    print("H->ZZ->4l")
    print("(e, m, t)")
    print("=========")
    print()
    print("a1:    ", JHUXSHZZ4la1)
    print("a2:    ", JHUXSHZZ4la2)
    print("a3:    ", JHUXSHZZ4la3)
    print("L1:    ", JHUXSHZZ4lL1)
    print("L1Zg:  ", JHUXSHZZ4lL1Zg)
    print()
    print("a1a2:  ", JHUXSHZZ4la1a2)
    print("a1a3:  ", JHUXSHZZ4la1a3)
    print("a1L1:  ", JHUXSHZZ4la1L1)
    print("a1L1Zg:", JHUXSHZZ4la1L1Zg)
#    print "a2a3:  ", JHUXSHZZ4la2a3
#    print "a2L1:  ", JHUXSHZZ4la2L1
#    print "a2L1Zg:", JHUXSHZZ4la2L1Zg
#    print "a3L1:  ", JHUXSHZZ4la3L1
#    print "a3L1Zg:", JHUXSHZZ4la3L1Zg
#    print "L1L1Zg:", JHUXSHZZ4lL1L1Zg
    print()
    print("=====")
    print("H->WW")
    print("=====")
    print()
    print("a1:    ", JHUXSHWWa1)
    print("a2:    ", JHUXSHWWa2)
    print("a3:    ", JHUXSHWWa3)
    print("L1:    ", JHUXSHWWL1)
    print()
    print("a1a2:  ", JHUXSHWWa1a2)
    print("a1a3:  ", JHUXSHWWa1a3)
    print("a1L1:  ", JHUXSHWWa1L1)
    print("a2a3:  ", JHUXSHWWa2a3)
    print("a2L1:  ", JHUXSHWWa2L1)
    print("a3L1:  ", JHUXSHWWa3L1)
