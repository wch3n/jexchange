#!/usr/bin/env python3

from jexchange import coeff
import numpy as np
from os import path

order = 1
confs = ['scf', 'afm']

cj = []
energy = []

for _conf in confs:
    a =  coeff.HSCoeff(path.join('../tests/Mn2In2O7', _conf, 'vasprun.xml'), order)
    _cj = a.calc_cj()
    _cj = np.append(_cj,1)
    cj.append(_cj)
    energy.append(a.energy)
   
print(np.linalg.lstsq(cj, energy)[0])
