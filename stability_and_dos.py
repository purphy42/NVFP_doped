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
from siman.analysis import calc_oxidation_states
from collections import defaultdict




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

st_inter = db['bulk.inter.ifc.ifc.ifc', '9_bulk_rel', 1]

st_deinter = db['bulk.deinter.ifc.ifc', '9_bulk_rel', 1]

st_al_close = db['bulk.al.close.ifc.ifc', '9_bulk_rel', 1]

st_al_dist = db['bulk.al.dist.ifc.ifc', '9_bulk_rel', 1]

st_some_na = db['bulk.some_na.ifc', '9_bulk_rel', 1]

st_al_some_na = db['bulk.al.some_na.ifc.ifc.ifc', '9_bulk_rel', 1]

st_al_some_na_dead = db['bulk.al.some_na_dead.ifc.ifc.ifc', '9_bulk_rel', 1]

# close = st_al_close.e0_at
# dist = st_al_dist.e0_at
# diff = dist - close
# print(close*1000, dist*1000, diff*1000)


# st_al_dist = db['al.dist', '9bulk_dos', 1].copy()


if 0:
    # st_al_dist = db['inter', '9bulk_dos', 1].copy()
    # st_al_dist = db['deinter', '9bulk_dos', 1].copy()
    # st_al_dist = db['some_na', '9bulk_dos', 1].copy()

    # st_al_dist = db['al.dist', '9bulk_dos', 1].copy()
    # st_al_dist = db['al_some_na', '9bulk_dos', 1].copy()
    st_al_dist = db['al_some_na_dead', '9bulk_dos', 1].copy()
    
    name = "al_some_na_dead"
    
    els = st_al_dist.init.get_elements()
    # els_al = [idx for idx, el in enumerate(els) if el == "Al"]
    els_v = [idx for idx, el in enumerate(els) if el == "V"]
    els = [idx for idx, el in enumerate(els)]
    
    # magmom = st_al_dist.init.magmom
    # magmom = [round(mom, 3) for mom in magmom]
    # magmom = np.array(magmom)
    
    ylim = (-1.0, 1.0)
    
    # print(magmom)
        
    # if (len(els_al)) > 0:
    #     print("Magmom on Al")
    #     print(els_al)
    #     print(magmom[els_al])
    # if (len(els_v)) > 0:
    #     print("Magmom on V")
    #     print(els_v)
    #     print(magmom[els_v])
    
    
    # if len(els_al) > 0:
        # st_al_dist.dos(iatoms = els_al, x_nbins = None, ylim = ylim, xlim = (-12, 4),
        #     fontsize = fontsize,  corner_letter  = 0, image_name = f'dos/{name}_o',
        #     orbitals = ['p6'], fig_format = 'png', show_dos_at_Fermi="p",
        # )

    # if len(els_v) > 0:
    #     st_al_dist.dos(iatoms = "ad", x_nbins = None, ylim = ylim, xlim = (-12, 4),
    #         fontsize = fontsize, corner_letter  = 0, image_name = f'dos/{name}_v',
    #         orbitals = ["s", 'p6', 'd'], fig_format = 'pdf', show_dos_at_Fermi="p",
    #         color_dict = {"s": "r", "p": "g"}
    #         )

    # if len(els_v) > 0:
    st_al_dist.dos(iatoms = els_v, x_nbins = None, ylim = ylim, xlim = (-12, 4),
        fontsize = fontsize, corner_letter  = 0, image_name = f'dos/{name}_o',
        orbitals = ['p6'], fig_format = 'png', show_dos_at_Fermi="p",
        # color_dict = {"s": "r", "p": "g"}
        )



if 0:
    # BADER
    add('al_some_na_dead', '9bulk_bader', 1, input_st = st_al_some_na_dead.end, it_folder = 'stability', up="up2", run = 0, cluster = 'razor128') 

    add('al_some_na', '9bulk_bader', 1, input_st = st_al_some_na.end, it_folder = 'stability', up="up2", run = 0, cluster = 'razor128') 

    add('some_na', '9bulk_bader', 1, input_st = st_some_na.end, it_folder = 'stability', up="up2", run = 0, cluster = 'razor128') 

    add('al.dist', '9bulk_bader', 1, input_st = st_al_dist.end, it_folder = 'stability', up="up2", run = 0, cluster = 'razor128') 

    add('deinter', '9bulk_bader', 1, input_st = st_deinter.end, it_folder = 'stability', up="up2", run = 0, cluster = 'razor128') 

    add('inter', '9bulk_bader', 1, input_st = st_inter.end, it_folder = 'stability', up="up2", run = 0, cluster = 'razor128') 

    from siman.analysis import calc_oxidation_states
    #ox1 = calc_oxidation_states(db['llzo.ngx_160', '9g_bader_400', 1], silent = 0)


if 0:
    # BADER
    res('al_some_na_dead', '9bulk_bader', 1, cluster = 'razor128') 
    res('al_some_na', '9bulk_bader', 1, cluster = 'razor128') 
    res('al.dist', '9bulk_bader', 1, cluster = 'razor128') 
    res('some_na', '9bulk_bader', 1, cluster = 'razor128') 
    res('deinter', '9bulk_bader', 1, cluster = 'razor128') 
    res('inter', '9bulk_bader', 1, cluster = 'razor128') 



def calc_average_oxi_state(calc):

    # Create dictionary to accumulate sums and counts
    sum_dict = defaultdict(float)
    count_dict = defaultdict(int)

    st = calc.copy().end
    els = st.get_elements()

    calc.get_bader_ACF()
    ox_states = calc_oxidation_states(calc, silent = 1)

    for el, ox in zip(els, ox_states):
        sum_dict[el] += ox
        count_dict[el] += 1

    # Calculate averages
    average_oxidation_states = {el: sum_dict[el]/count_dict[el] for el in sum_dict}

    print(average_oxidation_states)


# calc_average_oxi_state(db['al_some_na_dead', '9bulk_bader', 1])
# calc_average_oxi_state(db['al_some_na', '9bulk_bader', 1])
# calc_average_oxi_state(db['al.dist', '9bulk_bader', 1])
# calc_average_oxi_state(db['some_na', '9bulk_bader', 1])
# calc_average_oxi_state(db['deinter', '9bulk_bader', 1])
# calc_average_oxi_state(db['inter', '9bulk_bader', 1])









