
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




if 0:
    pass
    # AIMD calculations
    
    add('bulk.inter', '9_bulk_md_eq', 1, input_st = st_inter.end, it_folder = 'MD', run = 2, cluster = 'magnus', ngkpt=[1,1,1], up="up2") 
    add('bulk.deinter', '9_bulk_md_eq', 1, input_st = st_deinter.end, it_folder = 'MD', run = 2, cluster = 'magnus', ngkpt=[1,1,1], up="up2") 
    add('bulk.al.some_na', '9_bulk_md_eq', 1, input_st = st_some_na.end, it_folder = 'MD', run = 2, cluster = 'magnus', ngkpt=[1,1,1], up="up2") 
    
    add('bulk.al.dist', '9_bulk_md_eq', 1, input_st = st_al_dist.end, it_folder = 'MD', run = 2, cluster = 'magnus', ngkpt=[1,1,1], up="up2")  
    add('bulk.some_na', '9_bulk_md_eq', 1, input_st = st_al_some_na.end, it_folder = 'MD', run = 2, cluster = 'magnus', ngkpt=[1,1,1], up="up2") 
    add('bulk.al.some_na_dead', '9_bulk_md_eq', 1, input_st = st_al_some_na_dead.end, it_folder = 'MD', run = 2, cluster = 'magnus', ngkpt=[1,1,1], up="up2") 
    
    # Extra calculation to check. Not very important
    add('bulk.al.close', '9_bulk_md_eq', 1, input_st = st_al_close.end, it_folder = 'MD', run = 2, cluster = 'magnus', ngkpt=[1,1,1], up="up2")  
         
    
if 0:
    st_av = db['bulk.some_na.averaged.ifc', '9_bulk', 1].copy().end
    add('bulk.some_na.averaged', '9_bulk_md_eq', 1, input_st = st_av, it_folder = 'MD', run = 2, cluster = 'magnus', ngkpt=[1,1,1], up="up2")  
