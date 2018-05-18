Conventions for the constants here:

The top few constants are directly from JHUGen mod_Parameters.

g2HZZ and similar: these are from
https://twiki.cern.ch/twiki/bin/view/CMS/Run2MCProductionforHiggsProperties
They are sqrt(sigma1/sigmai) for the given process,
calculated by JHUGen in 2015. They were used for all MC samples,
and are also used to calculate fai and discriminants.
fai is particularly important, since these numbers are published
in HIG-17-011 (at least for decay; for production they appear in
published plots for fa3, and supplemental plots for the others).
They are basically a convention at this point and should not be changed.

SMXS are from YR4.  It's documented exactly how to
get them from the excel spreadsheet.

JHUXS - these are measured from JHUGen.  Currently, if you take
sqrt(sigma1/sigmai) you should get something reasonably
consistent with gidecay (or giVBF or whatever), but that's
not guaranteed to be the case.  In particular, when we
change PDFs that will no longer be true for production cross
sections.

The JHUXS for SM are calculated for g1=1, and the pure anomalous
JHUXS are calculated for gi=1.  For the mixture xsecs,
READ CAREFULLY:

The numbers written explicitly in this file are calculated with
g1=1, gi=gidecay or giVBF or ....  This is to maximize statistics.
(Similarly, for the mixtures between two anomalous couplings, they
are calculated with gi=gi, gj=gj)
Later in this file, they are processed further: first, we subtract
(JHUXSa1 + gi**2 * JHUXSai) [or similar for the aiaj xsecs].
We are then left with pure inteference.

The numbers are then divided by gi (or gi*gj).

At this point, if __name__ == "__main__" we print some things
that are expected to be ~0.  Check these if you make any changes
in constants.  They include sigma1 - sigmai*gi**2, which should
be removed when we change pdfs, as mentioned above.

Then, some of these are defined to be exactly 0.  For example
any interference between scalar and pseudoscalar, without cuts.

This is what you get when you import these constants and use them
in python.
