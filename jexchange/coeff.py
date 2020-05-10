# coding: utf-8

import numpy as np
from pymatgen.io.vasp.outputs import Vasprun
from itertools import compress

class HSCoeff:
    '''Calculate the coefficients for the exchange interactions with 
       the Heisenberg model among the nearest neighbors up to the specific order.'''
    def __init__(self,xml,order=1):
        r = Vasprun(xml)
        s = r.structures[0]

        # remove nonmagnetic species from the structure
        magmom = r.incar['MAGMOM']
        _nm_sites = np.abs(magmom) < 0.8
        _nm_species = set(list(compress(r.atomic_symbols, _nm_sites)))
        s.remove_species(list(_nm_species))
        spin = list(compress(magmom, np.invert(_nm_sites)))
        spin /= np.abs(spin)

        # determine the NN shells up to the specific order
        rn = 1.0
        rns = []
        while order > 0:
            rn += 0.4
            _nn = s.get_neighbors_in_shell(s.sites[0].coords,rn,0.2)
            if len(_nn) == 0:
                pass
            else:
                rns.append(rn)
                order -= 1
            
        self.spin = spin
        self.s = s
        self.rns = rns
        self.energy = r.final_energy/len(spin)

    def calc_cj(self):
        cj = np.zeros(len(self.rns))
        for jn, r in enumerate(self.rns):
            for idx, site_p in enumerate(self.s.sites):
                nn_sites = [nn_info[2] for nn_info in \
                    self.s.get_neighbors_in_shell(site_p.coords,r,0.2,include_index=True)]
                for n in nn_sites:
                    cj[jn] += self.spin[idx]*self.spin[n] 
            cj[jn] /= self.s.num_sites
        return cj
