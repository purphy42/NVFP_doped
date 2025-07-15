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


if 1:
    # BULK STRUCTURES
    st_int = smart_structure_read("structures/POSCAR_NaVPO4F_su_s10_1u_100_end")

    st_deint = smart_structure_read("structures/POSCAR_VPO4F_id_su_Na_s10_Na_1u_100_end")

    add('bulk.inter', '9_bulk', 1, input_st = st_int, it_folder = 'bulk', calc_method = 'uniform_scale', 
    				n_scale_images=10, scale_region = (-5, 5), cluster = 'razor128', up='up2', run=2) 

    add('bulk.deinter', '9_bulk', 1, input_st = st_int, it_folder = 'bulk', calc_method = 'uniform_scale', 
    				n_scale_images=10, scale_region = (-5, 5), cluster = 'razor128', up='up2', run=2) 


    st_al_close = st_int.copy()
    st_al_close = st_al_close.replace_atoms([30, 2], "Al")

    add('bulk.al.close', '9_bulk', 1, input_st = st_int, it_folder = 'bulk', calc_method = 'uniform_scale', 
                n_scale_images=10, scale_region = (-5, 5), cluster = 'razor128', up='up2', run=2) 

    st_al_dist = st_int.copy()
    st_al_dist = st_al_dist.replace_atoms([30, 21], "Al")
    
    add('bulk.al.dist', '9_bulk', 1, input_st = st_int, it_folder = 'bulk', calc_method = 'uniform_scale', 
                n_scale_images=10, scale_region = (-5, 5), cluster = 'razor128', up='up2', run=2) 
 
    st_al_deint = st_al_dist.copy()
    els = st_al_deint.get_elements()
    els_na = [idx for idx, el in enumerate(els) if el == "Na"]
    els_del = random.sample(els_na, int(0.9*len(els_na)))
    st_al_deint = st_al_deint.remove_atoms(els_del)

    add('bulk.al.some_na', '9_bulk', 1, input_st = st_int, it_folder = 'bulk', calc_method = 'uniform_scale', 
    				n_scale_images=10, scale_region = (-5, 5), cluster = 'razor128', up='up2', run=2) 

    st_some_na = st_int.copy()
    els = st_some_na.get_elements()
    els_na = [idx for idx, el in enumerate(els) if el == "Na"]
    els_del = random.sample(els_na, int(0.9*len(els_na)))
    st_some_na = st_some_na.remove_atoms(els_del)
    
    add('bulk.some_na', '9_bulk', 1, input_st = st_int, it_folder = 'bulk', calc_method = 'uniform_scale', 
                n_scale_images=10, scale_region = (-5, 5), cluster = 'razor128', up='up2', run=2) 

    
