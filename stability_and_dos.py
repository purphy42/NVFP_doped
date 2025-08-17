from siman.impurity import make_interface, make_interface2
from siman.calc_manage import get_structure_from_matproj, smart_structure_read, get_structure_from_matproj_new
from siman.geo import create_surface2, replic
from siman.analysis import interface_en, suf_en
import numpy as np
from siman.calc_manage import add, res, res_loop
from siman.header import * 
from siman.neb import add_neb
import random
from siman import header
from siman import thermo
from scipy import interpolate
import copy
import os, re
from structures import *


fontsize = 20
figsize = (10, 10)
ylim = (-2, 2)


# add('inter', '9_bulk_mp', 1, input_st = st_inter.end, it_folder = 'dos', up="up2", run = 1, cluster = 'razor128') 

# add('deinter', '9_bulk_mp', 1, input_st = st_deinter.end, it_folder = 'dos', up="up2", run = 2, cluster = 'razor128') 

# add('al.dist', '9_bulk_mp', 1, input_st = st_al_dist.end, it_folder = 'dos', up="up2", run = 2, cluster = 'razor128') 

# add('some_na', '9_bulk_mp', 1, input_st = st_some_na.end, it_folder = 'dos', up="up2", run = 2, cluster = 'razor128') 

# add('al_some_na', '9_bulk_mp', 1, input_st = st_al_some_na.end, it_folder = 'dos', up="up2", run = 2, cluster = 'razor128') 

# add('al_some_na_dead', '9_bulk_mp', 1, input_st = st_al_some_na_dead.end, it_folder = 'dos', up="up2", run = 2, cluster = 'razor128') 

# DOS

# add('al_some_na_dead', '9bulk_dos', 1, input_st = st_al_some_na_dead.end, it_folder = 'stability', up="up2", run = 2, cluster = 'razor128') 

# add('al_some_na', '9bulk_dos', 1, input_st = st_al_some_na.end, it_folder = 'stability', up="up2", run = 2, cluster = 'razor128') 

# add('some_na', '9bulk_dos', 1, input_st = st_some_na.end, it_folder = 'stability', up="up2", run = 2, cluster = 'razor128') 

# add('al.dist', '9bulk_dos', 1, input_st = st_al_dist.end, it_folder = 'stability', up="up2", run = 2, cluster = 'razor128') 

# add('deinter', '9bulk_dos', 1, input_st = st_deinter.end, it_folder = 'stability', up="up2", run = 2, cluster = 'razor128') 

# add('inter', '9bulk_dos', 1, input_st = st_inter.end, it_folder = 'stability', up="up2", run = 2, cluster = 'razor128') 




# RESULTS

# res('inter', '9_bulk_mp', 1,  cluster = 'razor128') 

# res('deinter', '9_bulk_mp', 1,  cluster = 'razor128') 

# res('al.dist', '9_bulk_mp', 1,  cluster = 'razor128') 

# res('some_na', '9_bulk_mp', 1,  cluster = 'razor128') 

# res('al_some_na', '9_bulk_mp', 1,  show='op', cluster = 'razor128') 

# res('al_some_na_dead', '9_bulk_mp', 1,  cluster = 'razor128') 

# db['some_na', '9_bulk_mp', 1].run('9_bulk_mp', "full_chg", run=2, cluster="razor128")
# db['some_na.ifc', '9_bulk_mp', 1].res(show='op', cluster="razor128")


if 0:
    st_al_dist = db['al.dist', '9bulk_dos', 1].copy()
	# int_neg.end.write_poscar("dos/int_dos_neg.vasp")
	# int_neg.end.jmol()
	# atoms_neg = [80, 97, 48, 53, 65, 13, 3, 8]
    els = st_al_dist.init.get_elements()
    els_al = [idx for idx, el in enumerate(els) if el == "Al"]
    els_v = [idx for idx, el in enumerate(els) if el == "V"]
    
    atoms_neg = els_al
    st_al_dist.dos(iatoms = atoms_neg, x_nbins = None, ylim = ylim, xlim = (-8, 4),
        fontsize = fontsize, corner_letter  = 0, image_name = 'dos/al_dist',
        orbitals = ["s", 'p', 'd'], fig_format = 'png', show_dos_at_Fermi="p" )

    st_al_dist.dos(iatoms = els_v, x_nbins = None, ylim = ylim, xlim = (-8, 4),
        fontsize = fontsize, corner_letter  = 0, image_name = 'dos/al_dist_v',
        orbitals = ["s", 'p', 'd'], fig_format = 'png', show_dos_at_Fermi="p" )




