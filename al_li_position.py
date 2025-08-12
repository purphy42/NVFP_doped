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
    
    add('bulk.al_li.1', '9_bulk', 1, input_st = st_al_li, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    
    add('bulk.al_li.2', '9_bulk', 1, input_st = st_al_li_2, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    
    add('bulk.al_li.3', '9_bulk', 1, input_st = st_al_li_3, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    
    
if 1:
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


