#!/usr/bin/env python

from uncertainties import ufloat
from uncertainties.umath import sqrt

from conventionsandSM import *

JHUXSHZZ2L2la1             = ufloat(     7.1517044,  0.00027591496)
JHUXSHZZ2L2la2             = ufloat(     2.5850323,  0.00010874196)
JHUXSHZZ2L2la3             = ufloat(      1.095479,  5.6780596e-05)
JHUXSHZZ2L2lL1             = ufloat( 4.8755556e-08,    1.75784e-12)
JHUXSHZZ2L2lL1Zg           = ufloat( 1.2489117e-07,  5.6567346e-12)
JHUXSHZZ2L2la1a2           = ufloat(     26.074307,  0.00094875635)
JHUXSHZZ2L2la1a3           = ufloat(     14.277409,   0.0005409516)
JHUXSHZZ2L2la1L1           = ufloat(    0.23726108,  2.1955163e-05)
JHUXSHZZ2L2la1L1Zg         = ufloat(     13.220602,  0.00053706572)
JHUXSHZZ2L2la2a3           = ufloat(     14.221651,  0.00063763008)
JHUXSHZZ2L2la2L1           = ufloat(     2.3200652,  0.00014040255)
JHUXSHZZ2L2la2L1Zg         = ufloat(     13.391687,  0.00049246945)
JHUXSHZZ2L2la3L1           = ufloat(     14.264343,  0.00051778249)
JHUXSHZZ2L2la3L1Zg         = ufloat(     14.364768,  0.00054679129)
JHUXSHZZ2L2lL1L1Zg         = ufloat(     15.488892,  0.00063476605)

JHUXSHZZ2L2leL = 1.4347981E+01
JHUXSHZZ2L2leR = 1.3952140E+01

JHUXSHWWa1                 = ufloat(     312.04019,    0.021123201)
JHUXSHWWa2                 = ufloat(      242.6283,    0.018655548)
JHUXSHWWa3                 = ufloat(     100.79135,   0.0076985693)
JHUXSHWWL1                 = ufloat( 1.6475531e-06,  1.1297587e-10)
JHUXSHWWa1a2               = ufloat(     1149.9181,       0.085554)
JHUXSHWWa1a3               = ufloat(      624.7195,    0.046033017)
JHUXSHWWa1L1               = ufloat(     5.3585509,  0.00056067121)
JHUXSHWWa2a3               = ufloat(     624.55269,    0.046795651)
JHUXSHWWa2L1               = ufloat(     83.700384,   0.0062011144)
JHUXSHWWa3L1               = ufloat(     624.23611,    0.045827636)

JHUXSHWWL1Zg               = 0
JHUXSHWWa1L1Zg             = JHUXSHWWa1
JHUXSHWWa2L1Zg             = g2HWW**2 * JHUXSHWWa2
JHUXSHWWa3L1Zg             = g4HWW**2 * JHUXSHWWa3
JHUXSHWWL1L1Zg             = g1prime2HWW**2 * JHUXSHWWL1

#Subtract the pure component from the interference, then divide by (gi*gj)
JHUXSHZZ2L2la1a2   = (JHUXSHZZ2L2la1a2   -                  JHUXSHZZ2L2la1 - g2HZZ          **2 * JHUXSHZZ2L2la2  ) / (g2HZZ                            )
JHUXSHZZ2L2la1a3   = (JHUXSHZZ2L2la1a3   -                  JHUXSHZZ2L2la1 - g4HZZ          **2 * JHUXSHZZ2L2la3  ) / (g4HZZ                            )
JHUXSHZZ2L2la1L1   = (JHUXSHZZ2L2la1L1   -                  JHUXSHZZ2L2la1 - g1prime2HZZ    **2 * JHUXSHZZ2L2lL1  ) / (g1prime2HZZ                      )
JHUXSHZZ2L2la1L1Zg = (JHUXSHZZ2L2la1L1Zg -                  JHUXSHZZ2L2la1 - ghzgs1prime2HZZ**2 * JHUXSHZZ2L2lL1Zg) / (ghzgs1prime2HZZ                  )
JHUXSHZZ2L2la2a3   = (JHUXSHZZ2L2la2a3   - g2HZZ      **2 * JHUXSHZZ2L2la2 - g4HZZ          **2 * JHUXSHZZ2L2la3  ) / (g2HZZ           * g4HZZ          )
JHUXSHZZ2L2la2L1   = (JHUXSHZZ2L2la2L1   - g2HZZ      **2 * JHUXSHZZ2L2la2 - g1prime2HZZ    **2 * JHUXSHZZ2L2lL1  ) / (g2HZZ           * g1prime2HZZ    )
JHUXSHZZ2L2la2L1Zg = (JHUXSHZZ2L2la2L1Zg - g2HZZ      **2 * JHUXSHZZ2L2la2 - ghzgs1prime2HZZ**2 * JHUXSHZZ2L2lL1Zg) / (g2HZZ           * ghzgs1prime2HZZ)
JHUXSHZZ2L2la3L1   = (JHUXSHZZ2L2la3L1   - g4HZZ      **2 * JHUXSHZZ2L2la3 - g1prime2HZZ    **2 * JHUXSHZZ2L2lL1  ) / (g4HZZ           * g1prime2HZZ    )
JHUXSHZZ2L2la3L1Zg = (JHUXSHZZ2L2la3L1Zg - g4HZZ      **2 * JHUXSHZZ2L2la3 - ghzgs1prime2HZZ**2 * JHUXSHZZ2L2lL1Zg) / (g4HZZ           * ghzgs1prime2HZZ)
JHUXSHZZ2L2lL1L1Zg = (JHUXSHZZ2L2lL1L1Zg - g1prime2HZZ**2 * JHUXSHZZ2L2lL1 - ghzgs1prime2HZZ**2 * JHUXSHZZ2L2lL1Zg) / (g1prime2HZZ     * ghzgs1prime2HZZ)

JHUXSHWWa1a2       = (JHUXSHWWa1a2       -                    JHUXSHWWa1     - g2HWW            **2 * JHUXSHWWa2      ) / (g2HWW                                    )
JHUXSHWWa1a3       = (JHUXSHWWa1a3       -                    JHUXSHWWa1     - g4HWW            **2 * JHUXSHWWa3      ) / (g4HWW                                    )
JHUXSHWWa1L1       = (JHUXSHWWa1L1       -                    JHUXSHWWa1     - g1prime2HWW      **2 * JHUXSHWWL1      ) / (g1prime2HWW                              )
JHUXSHWWa1L1Zg     = 0
JHUXSHWWa2a3       = (JHUXSHWWa2a3       - g2HWW        **2 * JHUXSHWWa2     - g4HWW            **2 * JHUXSHWWa3      ) / (g2HWW                 * g4HWW            )
JHUXSHWWa2L1       = (JHUXSHWWa2L1       - g2HWW        **2 * JHUXSHWWa2     - g1prime2HWW      **2 * JHUXSHWWL1      ) / (g2HWW                 * g1prime2HWW      )
JHUXSHWWa2L1Zg     = 0
JHUXSHWWa3L1       = (JHUXSHWWa3L1       - g4HWW        **2 * JHUXSHWWa3     - g1prime2HWW      **2 * JHUXSHWWL1      ) / (g4HWW                 * g1prime2HWW      )
JHUXSHWWa3L1Zg     = 0
JHUXSHWWL1L1Zg     = 0

if __name__ == "__main__":
    print "All of the following should be 0:"
    print
    print "  decay:"
    print "    a1XS -           g2**2*    a2XS = {:%}".format((JHUXSHZZ2L2la1 - g2HZZ**2           * JHUXSHZZ2L2la2    ) / JHUXSHZZ2L2la1)
    print "    a1XS -           g4**2*    a3XS = {:%}".format((JHUXSHZZ2L2la1 - g4HZZ**2           * JHUXSHZZ2L2la3    ) / JHUXSHZZ2L2la1)
    print "    a1XS -     g1prime2**2*    L1XS = {:%}".format((JHUXSHZZ2L2la1 - g1prime2HZZ**2     * JHUXSHZZ2L2lL1    ) / JHUXSHZZ2L2la1)
    print "    a1XS - ghzgs1prime2**2*  L1ZgXS = {:%}".format((JHUXSHZZ2L2la1 - ghzgs1prime2HZZ**2 * JHUXSHZZ2L2lL1Zg  ) / JHUXSHZZ2L2la1)
    print "                        g4*  a1a3XS = {:%}".format((                 g4HZZ              * JHUXSHZZ2L2la1a3  ) / JHUXSHZZ2L2la1)
    print "                     g2*g4*  a2a3XS = {:%}".format((                 g2HZZ*g4HZZ        * JHUXSHZZ2L2la2a3  ) / JHUXSHZZ2L2la1)
    print "               g1prime2*g4*  a3L1XS = {:%}".format((                 g1prime2HZZ*g4HZZ  * JHUXSHZZ2L2la3L1  ) / JHUXSHZZ2L2la1)
    print "           ghzgs1prime2*g4*a3L1ZgXS = {:%}".format((             ghzgs1prime2HZZ*g4HZZ  * JHUXSHZZ2L2la3L1Zg) / JHUXSHZZ2L2la1)
    print
    print "  HWW:"
    print "    a1XS -           g2**2*    a2XS = {:%}".format((JHUXSHWWa1     - g2HWW**2           * JHUXSHWWa2        ) / JHUXSHWWa1    )
    print "    a1XS -           g4**2*    a3XS = {:%}".format((JHUXSHWWa1     - g4HWW**2           * JHUXSHWWa3        ) / JHUXSHWWa1    )
    print "    a1XS -     g1prime2**2*    L1XS = {:%}".format((JHUXSHWWa1     - g1prime2HWW**2     * JHUXSHWWL1        ) / JHUXSHWWa1    )
#   print "    a1XS - ghzgs1prime2**2*  L1ZgXS = {:%}".format((JHUXSHWWa1     - ghzgs1prime2HWW**2 * JHUXSHWWL1Zg      ) / JHUXSHWWa1    )
    print "                        g4*  a1a3XS = {:%}".format((                 g4HWW              * JHUXSHWWa1a3      ) / JHUXSHWWa1    )
    print "                     g2*g4*  a2a3XS = {:%}".format((                 g2HWW  *g4HWW      * JHUXSHWWa2a3      ) / JHUXSHWWa1    )
    print "               g1prime2*g4*  a3L1XS = {:%}".format((                g1prime2HWW  *g4HWW * JHUXSHWWa3L1      ) / JHUXSHWWa1    )
#   print "           ghzgs1prime2*g4*a3L1ZgXS = {:%}".format((            ghzgs1prime2HWW  *g4HWW * JHUXSHWWa3L1Zg    ) / JHUXSHWWa1    )
    print

#Set them to exactly 0

JHUXSHZZ2L2la1a3   = \
JHUXSHZZ2L2la2a3   = \
JHUXSHZZ2L2la3L1   = \
JHUXSHZZ2L2la3L1Zg = 0

JHUXSHWWa1a3   = \
JHUXSHWWa2a3   = \
JHUXSHWWa3L1   = \
JHUXSHWWL1Zg   = \
JHUXSHWWa1L1Zg = \
JHUXSHWWa2L1Zg = \
JHUXSHWWa3L1Zg = \
JHUXSHWWL1L1Zg = 0

#defined this way, just make sure
for _ in """
  JHUXSHZZ2L2la1a3 JHUXSHZZ2L2la2a3 JHUXSHZZ2L2la3L1 JHUXSHZZ2L2la3L1Zg
  JHUXSHWWa1a3 JHUXSHWWa2a3 JHUXSHWWa3L1
  JHUXSHWWL1Zg JHUXSHWWa1L1Zg JHUXSHWWa2L1Zg JHUXSHWWa3L1Zg JHUXSHWWL1L1Zg
""".split():
  assert globals()[_] == 0, (_, globals()[_])
for k, v in globals().items():
    if "__" in k: continue
    assert v is not None, k
del k, v, _

