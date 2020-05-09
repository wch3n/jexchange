#!/usr/bin/env python3

from jexchange import coeff
import numpy as np

# FM SCF (order=1 for the first NN)
fm = coeff.HSCoeff('./tests/Mn2In2O7/scf/vasprun.xml', order=1)
cj_fm = fm.calc_cj()

# AFM SCF
af = coeff.HSCoeff('./tests/Mn2In2O7/afm/vasprun.xml', order=1)
cj_af = af.calc_cj()

# solve the linear equations for j1:
# cj_fm*j1 + E0 = E_fm
# cj_af*j1 + E0 = E_af
cj_fm = np.append(cj_fm,1)
cj_af = np.append(cj_af,1)
cj = np.array([cj_fm, cj_af])
energy = np.array([fm.energy, af.energy])

j1, e0 = np.linalg.solve(cj, energy)
print(j1)
