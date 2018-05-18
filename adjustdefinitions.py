"""
This should be loaded with execfile after defining the constants
"""

#Subtract the pure component from the interference, then divide by (gi*gj)

JHUXSVBFa1a2       = (JHUXSVBFa1a2       -                        JHUXSVBFa1     - g2VBF            **2 * JHUXSVBFa2      ) / (g2VBF                                )
JHUXSVBFa1a3       = (JHUXSVBFa1a3       -                        JHUXSVBFa1     - g4VBF            **2 * JHUXSVBFa3      ) / (g4VBF                                )
JHUXSVBFa1L1       = (JHUXSVBFa1L1       -                        JHUXSVBFa1     - g1prime2VBF      **2 * JHUXSVBFL1      ) / (g1prime2VBF                          )
JHUXSVBFa1L1Zg     = (JHUXSVBFa1L1Zg     -                        JHUXSVBFa1     - ghzgs1prime2VBF  **2 * JHUXSVBFL1Zg    ) / (ghzgs1prime2VBF                      )
JHUXSVBFa2a3       = (JHUXSVBFa2a3       - g2VBF            **2 * JHUXSVBFa2     - g4VBF            **2 * JHUXSVBFa3      ) / (g2VBF             * g4VBF            )
JHUXSVBFa2L1       = (JHUXSVBFa2L1       - g2VBF            **2 * JHUXSVBFa2     - g1prime2VBF      **2 * JHUXSVBFL1      ) / (g2VBF             * g1prime2VBF      )
JHUXSVBFa2L1Zg     = (JHUXSVBFa2L1Zg     - g2VBF            **2 * JHUXSVBFa2     - ghzgs1prime2VBF  **2 * JHUXSVBFL1Zg    ) / (g2VBF             * ghzgs1prime2VBF  )
JHUXSVBFa3L1       = (JHUXSVBFa3L1       - g4VBF            **2 * JHUXSVBFa3     - g1prime2VBF      **2 * JHUXSVBFL1      ) / (g4VBF             * g1prime2VBF      )
JHUXSVBFa3L1Zg     = (JHUXSVBFa3L1Zg     - g4VBF            **2 * JHUXSVBFa3     - ghzgs1prime2VBF  **2 * JHUXSVBFL1Zg    ) / (g4VBF             * ghzgs1prime2VBF  )
JHUXSVBFL1L1Zg     = (JHUXSVBFL1L1Zg     - g1prime2VBF      **2 * JHUXSVBFL1     - ghzgs1prime2VBF  **2 * JHUXSVBFL1Zg    ) / (g1prime2VBF       * ghzgs1prime2VBF  )

JHUXSZHa1a2        = (JHUXSZHa1a2        -                    JHUXSZHa1      - g2ZH             **2 * JHUXSZHa2       ) / (g2ZH                                 )
JHUXSZHa1a3        = (JHUXSZHa1a3        -                    JHUXSZHa1      - g4ZH             **2 * JHUXSZHa3       ) / (g4ZH                                 )
JHUXSZHa1L1        = (JHUXSZHa1L1        -                    JHUXSZHa1      - g1prime2ZH       **2 * JHUXSZHL1       ) / (g1prime2ZH                           )
JHUXSZHa1L1Zg      = (JHUXSZHa1L1Zg      -                    JHUXSZHa1      - ghzgs1prime2ZH   **2 * JHUXSZHL1Zg     ) / (ghzgs1prime2ZH                       )
JHUXSZHa2a3        = (JHUXSZHa2a3        - g2ZH         **2 * JHUXSZHa2      - g4ZH             **2 * JHUXSZHa3       ) / (g2ZH              * g4ZH             )
JHUXSZHa2L1        = (JHUXSZHa2L1        - g2ZH         **2 * JHUXSZHa2      - g1prime2ZH       **2 * JHUXSZHL1       ) / (g2ZH              * g1prime2ZH       )
JHUXSZHa2L1Zg      = (JHUXSZHa2L1Zg      - g2ZH         **2 * JHUXSZHa2      - ghzgs1prime2ZH   **2 * JHUXSZHL1Zg     ) / (g2ZH              * ghzgs1prime2ZH   )
JHUXSZHa3L1        = (JHUXSZHa3L1        - g4ZH         **2 * JHUXSZHa3      - g1prime2ZH       **2 * JHUXSZHL1       ) / (g4ZH              * g1prime2ZH       )
JHUXSZHa3L1Zg      = (JHUXSZHa3L1Zg      - g4ZH         **2 * JHUXSZHa3      - ghzgs1prime2ZH   **2 * JHUXSZHL1Zg     ) / (g4ZH              * ghzgs1prime2ZH   )
JHUXSZHL1L1Zg      = (JHUXSZHL1L1Zg      - g1prime2ZH   **2 * JHUXSZHL1      - ghzgs1prime2ZH   **2 * JHUXSZHL1Zg     ) / (g1prime2ZH        * ghzgs1prime2ZH   )

JHUXSWHa1a2        = (JHUXSWHa1a2        -                    JHUXSWHa1      - g2WH             **2 * JHUXSWHa2       ) / (g2WH                                     )
JHUXSWHa1a3        = (JHUXSWHa1a3        -                    JHUXSWHa1      - g4WH             **2 * JHUXSWHa3       ) / (g4WH                                     )
JHUXSWHa1L1        = (JHUXSWHa1L1        -                    JHUXSWHa1      - g1prime2WH       **2 * JHUXSWHL1       ) / (g1prime2WH                               )
JHUXSWHa1L1Zg      = 0
JHUXSWHa2a3        = (JHUXSWHa2a3        - g2WH         **2 * JHUXSWHa2      - g4WH             **2 * JHUXSWHa3       ) / (g2WH                  * g4WH             )
JHUXSWHa2L1        = (JHUXSWHa2L1        - g2WH         **2 * JHUXSWHa2      - g1prime2WH       **2 * JHUXSWHL1       ) / (g2WH                  * g1prime2WH       )
JHUXSWHa2L1Zg      = 0
JHUXSWHa3L1        = (JHUXSWHa3L1        - g4WH         **2 * JHUXSWHa3      - g1prime2WH       **2 * JHUXSWHL1       ) / (g4WH                  * g1prime2WH       )
JHUXSWHa3L1Zg      = 0
JHUXSWHL1L1Zg      = 0

JHUXSHJJa2a3       = (JHUXSHJJa2a3       -                        JHUXSHJJa2     - ghg4HJJ          **2 * JHUXSHJJa3      ) / (ghg4HJJ                              )

JHUXSttHkappakappatilde = (JHUXSttHkappakappatilde - JHUXSttHkappa - kappa_tilde_ttH**2 * JHUXSttHkappatilde) / kappa_tilde_ttH

normalize_WH_to_ZH = SMXSWH / JHUXSWHa1 / (SMXSZH / JHUXSZHa1)

if __name__ == "__main__":
    print "All of the following should be 0:"
    print
    print "  VBF:"
    print "    a1XS -           g2**2*    a2XS = {:%}".format((JHUXSVBFa1     - g2VBF**2           * JHUXSVBFa2        ) / JHUXSVBFa1    )
    print "    a1XS -           g4**2*    a3XS = {:%}".format((JHUXSVBFa1     - g4VBF**2           * JHUXSVBFa3        ) / JHUXSVBFa1    )
    print "    a1XS -     g1prime2**2*    L1XS = {:%}".format((JHUXSVBFa1     - g1prime2VBF**2     * JHUXSVBFL1        ) / JHUXSVBFa1    )
#   print "    a1XS - ghzgs1prime2**2*  L1ZgXS = {:%}".format((JHUXSVBFa1     - ghzgs1prime2VBF**2 * JHUXSVBFL1Zg      ) / JHUXSVBFa1    )
    print "                        g4*  a1a3XS = {:%}".format((                 g4VBF              * JHUXSVBFa1a3      ) / JHUXSVBFa1    )
    print "                     g2*g4*  a2a3XS = {:%}".format((                 g2VBF  *g4VBF      * JHUXSVBFa2a3      ) / JHUXSVBFa1    )
    print "               g1prime2*g4*  a3L1XS = {:%}".format((                g1prime2VBF  *g4VBF * JHUXSVBFa3L1      ) / JHUXSVBFa1    )
#   print "           ghzgs1prime2*g4*a3L1ZgXS = {:%}".format((            ghzgs1prime2VBF  *g4VBF * JHUXSVBFa3L1Zg    ) / JHUXSVBFa1    )
    print
    print "  ZH:"
    print "    a1XS -           g2**2*    a2XS = {:%}".format((JHUXSZHa1      - g2ZH**2            * JHUXSZHa2         ) / JHUXSZHa1     )
    print "    a1XS -           g4**2*    a3XS = {:%}".format((JHUXSZHa1      - g4ZH**2            * JHUXSZHa3         ) / JHUXSZHa1     )
    print "    a1XS -     g1prime2**2*    L1XS = {:%}".format((JHUXSZHa1      - g1prime2ZH**2      * JHUXSZHL1         ) / JHUXSZHa1     )
    print "    a1XS - ghzgs1prime2**2*  L1ZgXS = {:%}".format((JHUXSZHa1      - ghzgs1prime2ZH**2  * JHUXSZHL1Zg       ) / JHUXSZHa1     )
    print "                        g4*  a1a3XS = {:%}".format((                 g4ZH               * JHUXSZHa1a3       ) / JHUXSZHa1     )
    print "                     g2*g4*  a2a3XS = {:%}".format((                 g2ZH   *g4ZH       * JHUXSZHa2a3       ) / JHUXSZHa1     )
    print "               g1prime2*g4*  a3L1XS = {:%}".format((                g1prime2ZH   *g4ZH  * JHUXSZHa3L1       ) / JHUXSZHa1     )
    print "           ghzgs1prime2*g4*a3L1ZgXS = {:%}".format((            ghzgs1prime2ZH   *g4ZH  * JHUXSZHa3L1Zg     ) / JHUXSZHa1     )
    print
    print "  WH:"
    print "    a1XS -           g2**2*    a2XS = {:%}".format((JHUXSWHa1      - g2WH**2            * JHUXSWHa2         ) / JHUXSWHa1     )
    print "    a1XS -           g4**2*    a3XS = {:%}".format((JHUXSWHa1      - g4WH**2            * JHUXSWHa3         ) / JHUXSWHa1     )
    print "    a1XS -     g1prime2**2*    L1XS = {:%}".format((JHUXSWHa1      - g1prime2WH**2      * JHUXSWHL1         ) / JHUXSWHa1     )
#   print "    a1XS - ghzgs1prime2**2*  L1ZgXS = {:%}".format((JHUXSWHa1      - ghzgs1prime2WH**2  * JHUXSWHL1Zg       ) / JHUXSWHa1     )
    print "                        g4*  a1a3XS = {:%}".format((                 g4WH               * JHUXSWHa1a3       ) / JHUXSWHa1     )
    print "                     g2*g4*  a2a3XS = {:%}".format((                 g2WH   *g4WH       * JHUXSWHa2a3       ) / JHUXSWHa1     )
    print "               g1prime2*g4*  a3L1XS = {:%}".format((                g1prime2WH   *g4WH  * JHUXSWHa3L1       ) / JHUXSWHa1     )
#   print "           ghzgs1prime2*g4*a3L1ZgXS = {:%}".format((            ghzgs1prime2WH   *g4WH  * JHUXSWHa3L1Zg     ) / JHUXSWHa1     )
    print "    WpHXS + WmHXS - WHXS            = {:%}".format((SMXSWpH2L2l + SMXSWmH2L2l - SMXSWH2L2l                        ) / SMXSWH2L2l    )
    print
    print "  HJJ:"
    print "    a2XS -           g4**2*    a3XS = {:%}".format((JHUXSHJJa2     - ghg4HJJ**2         * JHUXSHJJa3        ) / JHUXSHJJa2    )
    print "                        g4*  a2a3XS = {:%}".format((                 ghg4HJJ            * JHUXSHJJa2a3      ) / JHUXSHJJa2    )
    print
    print "  ttH:"
    kt = kappa_tilde_ttH
    JHUXSttHk = JHUXSttHkappa
    JHUXSttHkt = JHUXSttHkappatilde
    JHUXSttHkkt = JHUXSttHkappakappatilde
    print "     kXS -           k~**2*    k~XS = {:%}".format((JHUXSttHk      - kt**2              * JHUXSttHkt        ) / JHUXSttHk     )
    print "                        k~*   kk~XS = {:%}".format((                 kt                 * JHUXSttHkkt       ) / JHUXSttHk     )
    print
    print "  VH:"
    print "    a1XS -           g2**2*    a2XS  = {:%}".format((JHUXSZHa1 + JHUXSWHa1*normalize_WH_to_ZH - g2VH              **2 * (JHUXSZHa2   + JHUXSWHa2  *normalize_WH_to_ZH)) / (JHUXSZHa1 + JHUXSWHa1*normalize_WH_to_ZH))
    print "    a1XS -           g4**2*    a3XS  = {:%}".format((JHUXSZHa1 + JHUXSWHa1*normalize_WH_to_ZH - g4VH              **2 * (JHUXSZHa3   + JHUXSWHa3  *normalize_WH_to_ZH)) / (JHUXSZHa1 + JHUXSWHa1*normalize_WH_to_ZH))
    print "    a1XS -     g1prime2**2*    L1XS  = {:%}".format((JHUXSZHa1 + JHUXSWHa1*normalize_WH_to_ZH - g1prime2VH    **2 * (JHUXSZHL1   + JHUXSWHL1  *normalize_WH_to_ZH)) / (JHUXSZHa1 + JHUXSWHa1*normalize_WH_to_ZH))
    print "    a1XS - ghzgs1prime2**2*  L1ZgXS  = {:%}".format((JHUXSZHa1 + JHUXSWHa1*normalize_WH_to_ZH - ghzgs1prime2VH**2 * (JHUXSZHL1Zg                                 )) / (JHUXSZHa1 + JHUXSWHa1*normalize_WH_to_ZH))
    del kt, JHUXSttHk, JHUXSttHkt, JHUXSttHkkt

#Set them to exactly 0

JHUXSVBFa1a3   = \
JHUXSVBFa2a3   = \
JHUXSVBFa3L1   = \
JHUXSVBFa3L1Zg = 0

JHUXSZHa1a3    = \
JHUXSZHa2a3    = \
JHUXSZHa3L1    = \
JHUXSZHa3L1Zg  = 0

JHUXSWHa1a3    = \
JHUXSWHa2a3    = \
JHUXSWHa3L1    = \
JHUXSWHL1Zg    = \
JHUXSWHa1L1Zg  = \
JHUXSWHa2L1Zg  = \
JHUXSWHa3L1Zg  = \
JHUXSWHL1L1Zg  = 0

JHUXSHJJa2a3   = 0

JHUXSttHkappakappatilde = 0

#defined this way, just make sure
for _ in """
  JHUXSVBFa1a3 JHUXSVBFa2a3 JHUXSVBFa3L1 JHUXSVBFa3L1Zg
  JHUXSZHa1a3 JHUXSZHa2a3 JHUXSZHa3L1 JHUXSZHa3L1Zg
  JHUXSWHa1a3 JHUXSWHa2a3 JHUXSWHa3L1
  JHUXSHJJa2a3 JHUXSttHkappakappatilde
  JHUXSWHL1Zg JHUXSWHa1L1Zg JHUXSWHa2L1Zg JHUXSWHa3L1Zg JHUXSWHL1L1Zg
""".split():
  assert globals()[_] == 0, (_, globals()[_])
for k, v in globals().items():
    if "__" in k: continue
    assert v is not None, k
del k, v, _
