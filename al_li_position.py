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



if 0:
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
    
    st_al_li_3 = st_al_li.copy()
    coords = st_al_li_3.xcart
    coord1 = np.array(coords[14])
    coord2 = np.array(coords[33])
    coords[125] = (coord1 + coord2) / 2
    st_al_li_3.xcart = coords
    st_al_li_3.update_xred()
    
    
    # add('bulk.al_li.1', '9_bulk', 1, input_st = st_al_li, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    
    # add('bulk.al_li.2', '9_bulk', 1, input_st = st_al_li_2, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    
    # add('bulk.al_li.3', '9_bulk', 1, input_st = st_al_li_3, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    
    
if 0:
    pass

    # res('bulk.al_li.1', '9_bulk', 1, cluster = 'razor128') 
    # res('bulk.al_li.2', '9_bulk', 1, cluster = 'razor128') 
    # res('bulk.al_li.3', '9_bulk', 1, cluster = 'razor128') 

    # db['bulk.al_li.1', '9_bulk', 1].run("9_bulk_rel", "full_chg", run=2, cluster = 'razor128') 
    # db['bulk.al_li.2', '9_bulk', 1].run("9_bulk_rel", "full_chg", run=2, cluster = 'razor128') 
    # db['bulk.al_li.3', '9_bulk', 1].run("9_bulk_rel", "full_chg", run=2, cluster = 'razor128') 

    # db['bulk.al_li.1.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 
    # db['bulk.al_li.2.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 
    # db['bulk.al_li.3.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 

    # db['bulk.al_li.1.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=1, cluster = 'razor128') 
    # db['bulk.al_li.2.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=1, cluster = 'razor128') 
    # db['bulk.al_li.3.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=1, cluster = 'razor128') 

    # db['bulk.al_li.1.ifc.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 
    # db['bulk.al_li.2.ifc.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 
    # db['bulk.al_li.3.ifc.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 

    # db['bulk.al_li.1.ifc.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=1, cluster = 'razor128')
    # db['bulk.al_li.2.ifc.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=1, cluster = 'razor128')  
    # db['bulk.al_li.3.ifc.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=1, cluster = 'razor128') 

    # db['bulk.al_li.1.ifc.ifc.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 
    # db['bulk.al_li.2.ifc.ifc.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 
    # db['bulk.al_li.3.ifc.ifc.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 

    # db['bulk.al_li.1.ifc.ifc', '9_bulk_rel', 1].run("9_bulk_rel_2", "full_chg", run=1, cluster = 'razor128')
    # db['bulk.al_li.2.ifc.ifc', '9_bulk_rel', 1].run("9_bulk_rel_2", "full_chg", run=1, cluster = 'razor128')  
    # db['bulk.al_li.3.ifc.ifc', '9_bulk_rel', 1].run("9_bulk_rel_2", "full_chg", run=1, cluster = 'razor128') 

    # db['bulk.al_li.1.ifc.ifc.ifc', '9_bulk_rel_2', 1].res(cluster = 'razor128') 
    # db['bulk.al_li.2.ifc.ifc.ifc', '9_bulk_rel_2', 1].res(cluster = 'razor128') 
    # db['bulk.al_li.3.ifc.ifc.ifc', '9_bulk_rel_2', 1].res(cluster = 'razor128') 

    # db['bulk.al_li.1.ifc.ifc.ifc', '9_bulk_rel_2', 1].run("9_bulk_rel", "full_chg", run=1, cluster = 'razor128')
    # db['bulk.al_li.2.ifc.ifc.ifc', '9_bulk_rel_2', 1].run("9_bulk_rel", "full_chg", run=1, cluster = 'razor128')  
    # db['bulk.al_li.3.ifc.ifc.ifc', '9_bulk_rel_2', 1].run("9_bulk_rel", "full_chg", run=1, cluster = 'razor128') 

    # db['bulk.al_li.1.ifc.ifc.ifc.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 
    # db['bulk.al_li.2.ifc.ifc.ifc.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 
    # db['bulk.al_li.3.ifc.ifc.ifc.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 

    # db['bulk.al_li.1.ifc.ifc.ifc.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=1, cluster = 'razor128')
    # db['bulk.al_li.2.ifc.ifc.ifc.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=1, cluster ='razor128')  
    # db['bulk.al_li.3.ifc.ifc.ifc.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=1, cluster = 'razor128') 

    db['bulk.al_li.1.ifc.ifc.ifc.ifc.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 
    db['bulk.al_li.2.ifc.ifc.ifc.ifc.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 
    db['bulk.al_li.3.ifc.ifc.ifc.ifc.ifc', '9_bulk_rel', 1].res(cluster = 'razor128') 


if 1:
    st_calc = db['bulk.al_li.1.ifc.ifc.ifc.ifc.ifc', '9_bulk_rel', 1].copy().end
    # add('al_li_position', '9_bulk_mp', 1, input_st = st_calc, it_folder = 'dos', up="up2", run = 0, cluster = 'razor128') 
    res('al_li_position', '9_bulk_mp', 1, cluster = 'razor128') 
    # db['al_li_position', '9_bulk_mp', 1].run("9_bulk_mp", "full_chg", run=2, add=1, cluster = 'magnus') 

    st_calc = db['bulk.al_li.2.ifc.ifc.ifc.ifc.ifc', '9_bulk_rel', 1].copy().end
    # add('al_li_position2', '9_bulk_mp', 1, input_st = st_calc, it_folder = 'dos', up="up2", run = 0, cluster = 'razor128') 
    res('al_li_position2', '9_bulk_mp', 1, cluster = 'razor128') 

    st_calc = db['bulk.al_li.3.ifc.ifc.ifc.ifc.ifc', '9_bulk_rel', 1].copy().end
    # add('al_li_position3', '9_bulk_mp', 1, input_st = st_calc, it_folder = 'dos', up="up2", run = 0, cluster = 'razor128') 
    res('al_li_position3', '9_bulk_mp', 1, cluster = 'razor128') 




if 0:
    st_inter = db['bulk.inter.ifc.ifc.ifc', '9_bulk_rel', 1]
    st_inter.end.write_poscar("/home/arseniy/Desktop/work/nvpf_al_doped/data/structures/inter.POSCAR")


    st_deinter = db['bulk.deinter.ifc.ifc', '9_bulk_rel', 1]
    st_deinter.end.write_poscar("/home/arseniy/Desktop/work/nvpf_al_doped/data/structures/deinter.POSCAR")

    st_some_na = db['bulk.some_na.ifc', '9_bulk_rel', 1]
    st_some_na.end.write_poscar("/home/arseniy/Desktop/work/nvpf_al_doped/data/structures/some_na.POSCAR")

    st_al_close = db['bulk.al.close.ifc.ifc', '9_bulk_rel', 1]
    st_inter.end.write_poscar("/home/arseniy/Desktop/work/nvpf_al_doped/data/structures/inter.POSCAR")

    st_al_dist = db['bulk.al.dist.ifc.ifc', '9_bulk_rel', 1]
    st_al_dist.end.write_poscar("/home/arseniy/Desktop/work/nvpf_al_doped/data/structures/al_dist.POSCAR")

    st_al_some_na = db['bulk.al.some_na.ifc.ifc.ifc', '9_bulk_rel', 1]
    st_al_some_na.end.write_poscar("/home/arseniy/Desktop/work/nvpf_al_doped/data/structures/al_some_na.POSCAR")

    st_al_some_na_dead = db['bulk.al.some_na_dead.ifc.ifc.ifc', '9_bulk_rel', 1]
    st_al_some_na_dead.end.write_poscar("/home/arseniy/Desktop/work/nvpf_al_doped/data/structures/al_some_na_dead.POSCAR")


if 0:
    # Al substitution in Li site
    st_int = smart_structure_read("structures/POSCAR_NaVPO4F_su_s10_1u_100_end")
    st_al_li = st_int.copy()
    st_al_li = st_al_li.replace_atoms([2, 11], "Al")
    st_al_li = st_al_li.remove_atoms([4, 5, 11, 13])
    # add('al_two_al_two_na', '9_bulk_eos', 1, input_st = st_al_li, it_folder = 'bulk', 
    #     calc_method = 'uniform_scale', ngkpt=[1,1,1], n_scale_images=10, scale_region = (-5, 5), 
    #     cluster = 'magnus', up='up2', run=2) 
    

    st_int = smart_structure_read("structures/POSCAR_NaVPO4F_su_s10_1u_100_end")
    st_al_li = st_int.copy()
    st_al_li = st_al_li.replace_atoms([2], "Al")
    st_al_li = st_al_li.remove_atoms([4, 6,])
    st_al_li = st_al_li.replace_atoms([25], "Al")
    # add('al_two_al_v_and_na', '9_bulk_eos', 1, input_st = st_al_li, it_folder = 'bulk', calc_method='uniform_scale', ngkpt=[1,1,1], n_scale_images=10, scale_region = (-5, 5),
    #     cluster = 'magnus', up='up2', run=2) 
    
    # Al substitution in Li site
    st_int = smart_structure_read("structures/POSCAR_NaVPO4F_su_s10_1u_100_end")
    st_al_li = st_int.copy()
    st_al_li = st_al_li.replace_atoms([2], "Al")
    st_al_li = st_al_li.remove_atoms([4, 6])
    # add('al_one_al_na', '9_bulk_eos', 1, input_st = st_al_li, it_folder = 'bulk', calc_method='uniform_scale', ngkpt=[1,1,1], n_scale_images=10, scale_region = (-5, 5), cluster = 'magnus', up='up2', run=2) 
    
    
if 0:
    res_loop('al_two_al_two_na.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128',)
    res_loop('al_two_al_v_and_na.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128',)
    res_loop('al_one_al_na.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128',)
    

if 0:
    st = db['al_two_al_two_na.su', '9_bulk_eos', 100].copy().init
    add('al_two_al_two_na', '9_bulk', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'magnus') 
    
    st = db['al_two_al_v_and_na.su', '9_bulk_eos', 100].copy().init
    add('al_two_al_v_and_na', '9_bulk', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'magnus') 
    
    st = db['al_one_al_na.su', '9_bulk_eos', 100].copy().init
    add('al_one_al_na', '9_bulk', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'magnus') 
    
    

if 0:
    res('al_two_al_two_na', '9_bulk', 1, cluster = 'magnus') 
    
    res('al_two_al_v_and_na', '9_bulk', 1, cluster = 'magnus') 
    
    res('al_one_al_na', '9_bulk', 1,  cluster = 'magnus') 
    
    

