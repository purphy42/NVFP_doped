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
    st = get_structure_from_matproj_new(mat_proj_id="mp-1238774")
    add('navpo4f', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 

    st = get_structure_from_matproj_new(mat_proj_id="mp-25440")
    add('vpo4f', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 

    st = get_structure_from_matproj_new(mat_proj_id="mp-686540")
    add('na3al2p2o8f3', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 

    st = get_structure_from_matproj_new(mat_proj_id="mp-7848")
    add('alpo4', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 

    st = get_structure_from_matproj_new(mat_proj_id="mp-19291")
    add('navpo5', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 

    st = get_structure_from_matproj_new(mat_proj_id="mp-468")
    add('alf3', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 

    st = get_structure_from_matproj_new(mat_proj_id="mp-559931")
    add('vf3', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 

    st = get_structure_from_matproj_new(mat_proj_id="mp-1094113")
    add('NaV2P2O9', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 

    st = get_structure_from_matproj_new(mat_proj_id="mp-1104878")
    add('VPO4F', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 

    st = get_structure_from_matproj_new(mat_proj_id="mp-17999")
    add('NaVF4', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 

    st = get_structure_from_matproj_new(mat_proj_id="mp-752810")
    add('NaVP2O7', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 

    st = get_structure_from_matproj_new(mat_proj_id="mp-694937")
    add('Na3V2P2O8F3', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 


    st = get_structure_from_matproj_new(mat_proj_id="mp-18835")
    add('VPO4', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 

    st = get_structure_from_matproj_new(mat_proj_id="mp-25265")
    add('VPO5', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 

    st = get_structure_from_matproj_new(mat_proj_id="mp-26728")
    add('VP2O7', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 

    st = get_structure_from_matproj_new(mat_proj_id="mp-1102077")
    add('NaAlF4', '9_bulk_mp', 1, input_st = st, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 


if 0:
    res('navpo4f', '9_bulk_mp', 1, cluster = 'razor128') 

    res('vpo4f', '9_bulk_mp', 1, cluster = 'razor128') 

    res('na3al2p2o8f3', '9_bulk_mp', 1, cluster = 'razor128') 

    res('alpo4', '9_bulk_mp', 1, cluster = 'razor128') 

    res('navpo5', '9_bulk_mp', 1, cluster = 'razor128') 

    res('alf3', '9_bulk_mp', 1, cluster = 'razor128') 

    res('vf3', '9_bulk_mp', 1, cluster = 'razor128') 

    # NEW entries
    res('NaV2P2O9', '9_bulk_mp', 1, cluster = 'razor128') 
    res('VPO4F', '9_bulk_mp', 1, cluster = 'razor128') 
    res('NaVF4', '9_bulk_mp', 1, cluster = 'razor128') 
    res('NaVP2O7', '9_bulk_mp', 1, cluster = 'razor128') 

    res('Na3V2P2O8F3', '9_bulk_mp', 1, cluster = 'razor128') 
    res('VPO4', '9_bulk_mp', 1, cluster = 'razor128') 
    res('VPO5', '9_bulk_mp', 1, cluster = 'razor128') 
    res('VP2O7', '9_bulk_mp', 1, cluster = 'razor128') 
    res('NaAlF4', '9_bulk_mp', 1, cluster = 'razor128') 

