#!/usr/bin/env python

# vim: expandtab tw=75

import pylab as pl

x = pl.linspace(0, 2*pl.pi, 151)
pl.figure()
pl.plot(x, pl.sin(x), linewidth=2)
pl.show()
