from anomalouscouplingsconstants import *
import EFTmodel1 as eft

aidecay = {
      "g2": 1.65684,
      "g4": 2.55052,
      "g1prime2": -12100.42,
      "ghzgs1prime2": -7613.351302119843,
}


sigma2_old = (aidecay["g2"])**(-2)
sigma4_old = (aidecay["g4"])**(-2)
sigmaL1_old = (aidecay["g1prime2"])**(-2)
sigmaL1Zg_old = (aidecay["ghzgs1prime2"])**(-2)


g2 = 1
g4 = 0
gzprime2 = 0
#calculate ghzgs1prime2 from EFT
ghzgs1prime2 = eft.L1Zgamma(g2,g4,gzprime2)

sigma2_new = sigma2_old* (g2**2 * JHUXSHZZ2e2mua2 + g2*ghzgs1prime2 * JHUXSHZZ2e2mua2L1Zg + ghzgs1prime2**2 * JHUXSHZZ2e2muL1Zg)


print "EFT sigma_a2" ,sigma2_new




#and similar for sigmaL1_new.

g2 = 0
g4 = 0
gzprime2 = 1
#calculate ghzgs1prime2 from EFT
ghzgs1prime2 = eft.L1Zgamma(g2,g4,gzprime2)


sigmaL1_new = sigmaL1_old* (gzprime2**2 * JHUXSHZZ2e2muL1 + gzprime2*ghzgs1prime2 * JHUXSHZZ2e2muL1L1Zg + ghzgs1prime2**2 * JHUXSHZZ2e2muL1Zg)


print "EFT sigma_L1 :", sigmaL1_new


