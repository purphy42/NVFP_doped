
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
    
         
    # add('bulk.deinter', '9_bulk', 1, input_st = st_bulk_deinter, it_folder = 'MD', up="up2", run = 2, cluster = 'razor128') 
    # add('bulk.al.close', '9_bulk', 1, input_st = st_bulk_al_close, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    # add('bulk.al.dist', '9_bulk', 1, input_st = st_bulk_al_dist, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    # add('bulk.al.some_na', '9_bulk', 1, input_st = st_bulk_al_some_dead, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
  
