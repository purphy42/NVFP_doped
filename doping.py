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



# st_int.nn(i=27, n=10, only=[23])

# close: 3.57 AA
# dist: 5.68 AA

# ion relaxation 0.3, DOS 0.2.  AIMD: 0.5


if 0:
    # BULK STRUCTURES
    st_int = smart_structure_read("structures/POSCAR_NaVPO4F_su_s10_1u_100_end")

    st_deint = smart_structure_read("structures/POSCAR_VPO4F_id_su_Na_s10_Na_1u_100_end")

    add('bulk.inter', '9_bulk_eos', 1, input_st = st_int, it_folder = 'bulk', calc_method = 'uniform_scale', 
    				ngkpt=[1,1,1], n_scale_images=10, scale_region = (-5, 5), cluster = 'razor128', up='up2', run=2) 

    add('bulk.deinter', '9_bulk_eos', 1, input_st = st_deint, it_folder = 'bulk', calc_method = 'uniform_scale', 
    				ngkpt=[1,1,1], n_scale_images=10, scale_region = (-5, 5), cluster = 'razor128', up='up2', run=2) 


    st_al_close = st_int.copy()
    st_al_close = st_al_close.replace_atoms([27, 28], "Al")

    add('bulk.al.close', '9_bulk_eos', 1, input_st = st_al_close, it_folder = 'bulk', calc_method = 'uniform_scale', 
                ngkpt=[1,1,1], n_scale_images=10, scale_region = (-5, 5), cluster = 'razor128', up='up2', run=2) 

    st_al_dist = st_int.copy()
    st_al_dist = st_al_dist.replace_atoms([27, 30], "Al")
    
    add('bulk.al.dist', '9_bulk_eos', 1, input_st = st_al_dist, it_folder = 'bulk', calc_method = 'uniform_scale', 
                ngkpt=[1,1,1], n_scale_images=10, scale_region = (-5, 5), cluster = 'razor128', up='up2', run=2) 
 
    st_al_deint = st_al_dist.copy()
    els = st_al_deint.get_elements()
    els_na = [idx for idx, el in enumerate(els) if el == "Na"]
    els_del = random.sample(els_na, int(0.9*len(els_na)))
    st_al_deint = st_al_deint.remove_atoms(els_del)

    add('bulk.al.some_na', '9_bulk_eos', 1, input_st = st_al_deint, it_folder = 'bulk', calc_method = 'uniform_scale', ngkpt=[1,1,1], n_scale_images=10, scale_region = (-5, 5), cluster = 'razor128', up='up2', run=2) 

    st_some_na = st_int.copy()
    els = st_some_na.get_elements()
    els_na = [idx for idx, el in enumerate(els) if el == "Na"]
    els_del = random.sample(els_na, int(0.9*len(els_na)))
    st_some_na = st_some_na.remove_atoms(els_del)
    
    add('bulk.some_na', '9_bulk_eos', 1, input_st = st_some_na, it_folder = 'bulk', calc_method = 'uniform_scale', 
            ngkpt=[1,1,1], n_scale_images=10, scale_region = (-5, 5), cluster = 'razor128', up='up2', run=2) 

    
    st_al_deint = st_al_dist.copy()
    els = st_al_deint.get_elements()
    els_na = [idx for idx, el in enumerate(els) if el == "Na"]
    els_del = random.sample(els_na, int(0.8*len(els_na)))
    st_al_deint = st_al_deint.remove_atoms(els_del)

    # st_al_deint.printme()

    add('bulk.al.some_na_dead', '9_bulk_eos', 1, input_st = st_al_deint, it_folder = 'bulk', ngkpt=[1,1,1], 
        calc_method = 'uniform_scale', n_scale_images=10, scale_region = (-5, 5), cluster = 'razor128', up='up2', run=2) 
    

if 0:
    res_loop('bulk.inter.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128', up="up2")

    res_loop('bulk.deinter.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128', up="up2")

    res_loop('bulk.al.close.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128', up="up2")

    res_loop('bulk.al.dist.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128', up="up2")

    # res_loop('bulk.al.some_na.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128')

    # res_loop('bulk.some_na.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128')

    # res_loop('bulk.al.some_na_dead.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128')



if 0:
    st_bulk_inter = db['bulk.inter.su', '9_bulk_eos', 100].copy().end
    # st_bulk_deinter = db['bulk.deinter.su', '9_bulk_eos', 100].copy().end
    st_bulk_al_close = db['bulk.al.close.su', '9_bulk_eos', 100].copy().end
    st_bulk_al_dist = db['bulk.al.dist.su', '9_bulk_eos', 100].copy().end
    

    # st_bulk_deinter.jmol()
    
    # st_bulk_al_some_na = db['bulk.al.some_na.su', '9_bulk_eos', 100].copy().end
    # st_bulk_soma_na = db['bulk.some_na.su', '9_bulk_eos', 100].copy().end
    # st_bulk_some_na_dead = db['bulk.al.some_na_dead.su', '9_bulk_eos', 100].copy().end
  
    add('bulk.inter', '9_bulk', 1, input_st = st_bulk_inter, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    # add('bulk.deinter', '9_bulk', 1, input_st = st_bulk_deinter, it_folder = 'MD', up="up2", run = 2, cluster = 'razor128') 
    add('bulk.al.close', '9_bulk', 1, input_st = st_bulk_al_close, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    add('bulk.al.dist', '9_bulk', 1, input_st = st_bulk_al_dist, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    



if 0:
    # MD calculations
    st_bulk_inter = db['bulk.inter.su', '9_bulk_eos', 100].copy().end
    st_bulk_deinter = db['bulk.deinter.su', '9_bulk_eos', 100].copy().end
    st_bulk_al_close = db['bulk.al.close.su', '9_bulk_eos', 100].copy().end
    st_bulk_al_dist = db['bulk.al.dist.su', '9_bulk_eos', 100].copy().end
    
    
    # add('bulk.inter', '9_bulk_md_eq', 1, input_st = st_bulk_inter, it_folder = 'MD', up="up2", run = 2, cluster = 'razor128', up="up2") 
    # add('bulk.deinter', '9_bulk_md_eq', 1, input_st = st_bulk_deinter, it_folder = 'MD', up="up2", run = 2, cluster = 'razor128', up="up2") 
    # add('bulk.al.close', '9_bulk_md_eq', 1, input_st = st_bulk_al_close, it_folder = 'MD', up="up2", run = 2, cluster = 'razor128', up="up2") 
    # add('bulk.al.dist', '9_bulk_md_eq', 1, input_st = st_bulk_al_dist, it_folder = 'MD', up="up2", run = 2, cluster = 'razor128', up="up2") 
    
    # st_bulk_al_some_na = db['bulk.al.some_na.su', '9_bulk_eos', 100].copy().end
    # st_bulk_soma_na = db['bulk.some_na.su', '9_bulk_eos', 100].copy().end
    # st_bulk_some_na_dead = db['bulk.al.some_na_dead.su', '9_bulk_eos', 100].copy().end
    
    # add('bulk.al.some_na', '9_bulk_md_eq', 1, input_st = st_bulk_al_some_na, it_folder = 'MD', up="up2", run = 2, cluster = 'razor128') 
    # add('bulk.some_na', '9_bulk_md_eq', 1, input_st = st_bulk_soma_na, it_folder = 'MD', up="up2", run = 2, cluster = 'razor128') 
    # add('bulk.al.some_na_dead', '9_bulk_md_eq', 1, input_st = st_bulk_some_na_dead, it_folder = 'MD', up="up2", run = 2, cluster = 'razor128') 
    


if 0:
    db['bulk.inter.su', '9_bulk_eos', 100].copy().res()
    db['bulk.deinter.su', '9_bulk_eos', 100].copy().res()
    db['bulk.al.close.su', '9_bulk_eos', 100].copy().res()
    db['bulk.al.dist.su', '9_bulk_eos', 100].copy().res()
    db['bulk.al.some_na.su', '9_bulk_eos', 100].copy().res()
    db['bulk.some_na.su', '9_bulk_eos', 100].copy().res()
    db['bulk.al.some_na_dead.su', '9_bulk_eos', 100].copy().res()
 


if 1:
    # Al substitution in Li site
    st_int = smart_structure_read("structures/POSCAR_NaVPO4F_su_s10_1u_100_end")
    st_al_li = st_int.copy()
    st_al_li = st_al_li.replace_atoms([2], "Al")
    st_al_li = st_al_li.remove_atoms([4, 6])
    
    st_al_li_2 = st_al_li.copy()
    coords = st_al_li_2.xcart
    coord1 = np.array(coords[65])
    coord2 = np.array(coords[67])
    coords[125] = (coord1 + coord2) / 2
    st_al_li_2.xcart = coords
    st_al_li_2.update_xred()
    
    st_al_li_3 = st_al_li.copy()
    coords = st_al_li_3.xcart
    coord1 = np.array(coords[14])
    coord2 = np.array(coords[33])
    coords[125] = (coord1 + coord2) / 2
    st_al_li_3.xcart = coords
    st_al_li_3.update_xred()
    
    add('bulk.al_li.1', '9_bulk', 1, input_st = st_al_li, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    
    add('bulk.al_li.2', '9_bulk', 1, input_st = st_al_li_2, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    
    add('bulk.al_li.3', '9_bulk', 1, input_st = st_al_li_3, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    
