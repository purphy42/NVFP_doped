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
    

# res_loop('bulk.inter.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128', up="up2")

# print( db['bulk.inter.su', '9_bulk_eos', 100].end.rprimd )
# db['bulk.inter.su', '9_bulk_eos', 100].res()



if 0:
    pass

    res_loop('bulk.inter.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128', up="up2")

    res_loop('bulk.deinter.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128', up="up2")

    res_loop('bulk.al.close.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128', up="up2")

    res_loop('bulk.al.dist.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128', up="up2")

    res_loop('bulk.al.some_na.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128', up="up2")

    res_loop('bulk.some_na.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128', up="up2")

    res_loop('bulk.al.some_na_dead.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128', up="up2")



if 0:
    st_bulk_inter = db['bulk.inter.su', '9_bulk_eos', 100].copy().end
    st_bulk_deinter = db['bulk.deinter.su', '9_bulk_eos', 100].copy().end
    st_bulk_al_close = db['bulk.al.close.su', '9_bulk_eos', 100].copy().end
    st_bulk_al_dist = db['bulk.al.dist.su', '9_bulk_eos', 100].copy().end
    
    # add('bulk.inter', '9_bulk', 1, input_st = st_bulk_inter, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    # add('bulk.deinter', '9_bulk', 1, input_st = st_bulk_deinter, it_folder = 'MD', up="up2", run = 2, cluster = 'razor128') 
    # add('bulk.al.close', '9_bulk', 1, input_st = st_bulk_al_close, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    # add('bulk.al.dist', '9_bulk', 1, input_st = st_bulk_al_dist, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
  
    st_bulk_soma_na = db['bulk.some_na.su', '9_bulk_eos', 100].copy().end
    st_bulk_some_na_dead = db['bulk.al.some_na_dead.su', '9_bulk_eos', 100].copy().end
    st_bulk_al_some_na = db['bulk.al.some_na.su', '9_bulk_eos', 100].copy().end

    # add('bulk.al.some_na_dead', '9_bulk', 1, input_st = st_bulk_some_na_dead, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    # add('bulk.some_na', '9_bulk', 1, input_st = st_bulk_soma_na, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    # add('bulk.al.some_na', '9_bulk', 1, input_st = st_bulk_al_some_na, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    


if 0:
    db['bulk.inter.su', '9_bulk_eos', 100].copy().res()
    db['bulk.deinter.su', '9_bulk_eos', 100].copy().res()
    db['bulk.al.close.su', '9_bulk_eos', 100].copy().res()
    db['bulk.al.dist.su', '9_bulk_eos', 100].copy().res()
    db['bulk.al.some_na.su', '9_bulk_eos', 100].copy().res()
    db['bulk.some_na.su', '9_bulk_eos', 100].copy().res()
    db['bulk.al.some_na_dead.su', '9_bulk_eos', 100].copy().res()
 


# Pre-relaxtion

if 1:
    pass
    
    # Inter
    # res('bulk.inter', '9_bulk', 1, up="up2", cluster = 'razor128')
    # db['bulk.inter', '9_bulk', 1].run("9_bulk_rel", "full_chg", run=2, cluster="razor128")
    # db['bulk.inter.ifc', '9_bulk_rel', 1].res(cluster="razor128")         
    # db['bulk.inter.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=2, cluster="razor128")
    # db['bulk.inter.ifc.ifc', '9_bulk_rel', 1].res(cluster="razor128")         
    # db['bulk.inter.ifc.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=2, cluster="razor128")
    # db['bulk.inter.ifc.ifc.ifc', '9_bulk_rel', 1].res(cluster="razor128")         
    #  FINISHED
    
    # Deinter
    # res('bulk.deinter', '9_bulk', 1, up="up2", cluster = 'razor128')
    # db['bulk.deinter', '9_bulk', 1].run("9_bulk_rel", "full_chg", run=1, cluster="razor128") 
    # db['bulk.deinter.ifc', '9_bulk_rel', 1].res(show='en', cluster="razor128") 
    # db['bulk.deinter.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=1, cluster="razor128") 
    # db['bulk.deinter.ifc.ifc', '9_bulk_rel', 1].res(cluster="razor128") 
    # FINISHED
  
    # Al close
    # res('bulk.al.close', '9_bulk', 1, up="up2", cluster = 'razor128') 
    # db['bulk.al.close', '9_bulk', 1].run("9_bulk_rel", "full_chg", run=2, cluster="razor128")
    # db['bulk.al.close.ifc', '9_bulk_rel', 1].res(cluster="razor128") 
    # db['bulk.al.close.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=2, cluster="razor128")
    # db['bulk.al.close.ifc.ifc', '9_bulk_rel', 1].res(cluster="razor128") 
    # FINISHED

    # Al DIST
    # res('bulk.al.dist', '9_bulk', 1, up="up2", cluster = 'razor128') 
    # db['bulk.al.dist', '9_bulk', 1].run("9_bulk_rel", "full_chg", run=2, cluster="razor128")
    # db['bulk.al.dist.ifc', '9_bulk_rel', 1].res(cluster="razor128") 
    # db['bulk.al.dist.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=2, cluster="razor128")
    # db['bulk.al.dist.ifc.ifc', '9_bulk_rel', 1].res(cluster="razor128") 
    # FINISHED

    # Some Na
    # res('bulk.some_na', '9_bulk', 1, up="up2", cluster = 'razor128') 
    # db['bulk.some_na', '9_bulk', 1].run("9_bulk_rel", "full_chg", run=2, cluster="razor128")
    # db['bulk.some_na.ifc', '9_bulk_rel', 1].res(cluster="razor128")
    # FINISHED
    
    # SOME Na with Al
    # res('bulk.al.some_na', '9_bulk', 1, up="up2", cluster = 'razor128') 
    # db['bulk.al.some_na', '9_bulk', 1].run("9_bulk_rel", "full_chg", run=2, add=1, cluster="razor128") 
    # db['bulk.al.some_na.ifc', '9_bulk_rel', 1].res(cluster="razor128") 
    # db['bulk.al.some_na.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=2, add=1, cluster="razor128") 
    # db['bulk.al.some_na.ifc.ifc', '9_bulk_rel', 1].res(cluster="razor128") 
    # db['bulk.al.some_na.ifc.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=2, add=1, cluster="razor128") 
    # db['bulk.al.some_na.ifc.ifc.ifc', '9_bulk_rel', 1].res(show="en", cluster="razor128") 
    # FINISHED
    
    # Al with some dead Na  
    # res('bulk.al.some_na_dead', '9_bulk', 1, up="up2", cluster = 'razor128') 
    # db['bulk.al.some_na_dead', '9_bulk', 1].run("9_bulk_rel", "full_chg", run=1, cluster="razor128") 
    # res('bulk.al.some_na_dead.ifc', '9_bulk_rel', 1, up="up2", cluster = 'razor128') 
    # db['bulk.al.some_na_dead.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=1, cluster="razor128") 
    # res('bulk.al.some_na_dead.ifc.ifc', '9_bulk_rel', 1, up="up2", cluster = 'razor128') 
    # db['bulk.al.some_na_dead.ifc.ifc', '9_bulk_rel', 1].run("9_bulk_rel", "full_chg", run=1, cluster="razor128") 
    # res('bulk.al.some_na_dead.ifc.ifc.ifc', '9_bulk_rel', 1, up="up2", cluster = 'razor128') 
    # FINISHED
    


# st_deinter.jmol()

# st_inter.end.jmol()


if 0:
    st = st_some_na.end
    
    vol = 1
    for i in range(3):
        if i == 1:
            print(f"{st.rprimd[i][i]/2:.3f}", end="\t")
            vol *= st.rprimd[i][i]/2
        else:
            print(f"{st.rprimd[i][i]:.3f}", end="\t")
            vol *= st.rprimd[i][i]
            
    print(f"{vol:.3f}")

# st_inter = db['bulk.inter.ifc.ifc.ifc', '9_bulk_rel', 1]

# st_deinter = db['bulk.deinter.ifc.ifc', '9_bulk_rel', 1]

# st_al_close = db['bulk.al.close.ifc.ifc', '9_bulk_rel', 1]

# st_al_dist = db['bulk.al.dist.ifc.ifc', '9_bulk_rel', 1]

# st_some_na = db['bulk.some_na.ifc', '9_bulk_rel', 1]

# st_al_some_na = db['bulk.al.some_na.ifc.ifc.ifc', '9_bulk_rel', 1]

# st_al_some_na_dead = db['bulk.al.some_na_dead.ifc.ifc.ifc', '9_bulk_rel', 1]



if 0:
    st_inter = db['bulk.inter.ifc.ifc.ifc', '9_bulk_rel', 1].copy().end
    # add('bulk.inter', '9_bulk_eos_isif3', 1, input_st = st_inter, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    res('bulk.inter', '9_bulk_eos_isif3', 1, cluster = 'razor128') 

    st_deinter = db['bulk.deinter.ifc.ifc', '9_bulk_rel', 1].copy().end
    # add('bulk.deinter', '9_bulk_eos_isif3', 1, input_st = st_deinter, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    res('bulk.deinter', '9_bulk_eos_isif3', 1, cluster = 'razor128') 

    st_al_close = db['bulk.al.close.ifc.ifc', '9_bulk_rel', 1].copy().end
    # add('bulk.al.close', '9_bulk_eos_isif3', 1, input_st = st_al_close, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    res('bulk.al.close', '9_bulk_eos_isif3', 1, cluster = 'razor128') 

    st_al_dist = db['bulk.al.dist.ifc.ifc', '9_bulk_rel', 1].copy().end
    # add('bulk.al.dist', '9_bulk_eos_isif3', 1, input_st = st_al_dist, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    res('bulk.al.dist', '9_bulk_eos_isif3', 1, cluster = 'razor128') 

    st_some_na = db['bulk.some_na.ifc', '9_bulk_rel', 1].copy().end
    # add('bulk.some_na', '9_bulk_eos_isif3', 1, input_st = st_some_na, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    res('bulk.some_na', '9_bulk_eos_isif3', 1, cluster = 'razor128') 

    st_al_some_na = db['bulk.al.some_na.ifc.ifc.ifc', '9_bulk_rel', 1].copy().end
    # add('bulk.al.some_na', '9_bulk_eos_isif3', 1, input_st = st_al_some_na, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    res('bulk.al.some_na', '9_bulk_eos_isif3', 1, cluster = 'razor128') 

    st_al_some_na_dead = db['bulk.al.some_na_dead.ifc.ifc.ifc', '9_bulk_rel', 1].copy().end
    # add('bulk.al.some_na_dead', '9_bulk_eos_isif3', 1, input_st = st_al_some_na_dead, it_folder = 'bulk', up="up2", run = 2, cluster = 'razor128') 
    res('bulk.al.some_na_dead', '9_bulk_eos_isif3', 1, cluster = 'razor128') 




if 0:
    # BULK STRUCTURES
    st_int = smart_structure_read("structures/POSCAR_NaVPO4F_su_s10_1u_100_end")
    st_deint = smart_structure_read("structures/POSCAR_VPO4F_id_su_Na_s10_Na_1u_100_end")
    add('bulk.inter', '9_bulk_eos_isif3_ecut', 1, input_st = st_int, it_folder = 'bulk', cluster = 'magnus', up='up2', run=2) 
    add('bulk.deinter', '9_bulk_eos_isif3_ecut', 1, input_st = st_deint, it_folder = 'bulk', cluster = 'magnus', up='up2', run=2) 

    st_al_close = st_int.copy()
    st_al_close = st_al_close.replace_atoms([27, 28], "Al")
    add('bulk.al.close', '9_bulk_eos_isif3_ecut', 1, input_st = st_al_close, it_folder = 'bulk', cluster = 'magnus', up='up2', run=2) 

    st_al_dist = st_int.copy()
    st_al_dist = st_al_dist.replace_atoms([27, 30], "Al")
    add('bulk.al.dist', '9_bulk_eos_isif3_ecut', 1, input_st = st_al_dist, it_folder = 'bulk', cluster = 'magnus', up='up2', run=2)    
 
    st_al_deint = st_al_dist.copy()
    els = st_al_deint.get_elements()
    els_na = [idx for idx, el in enumerate(els) if el == "Na"]
    els_del = random.sample(els_na, int(0.9*len(els_na)))
    st_al_deint = st_al_deint.remove_atoms(els_del)

    add('bulk.al.some_na', '9_bulk_eos_isif3_ecut', 1, input_st = st_al_deint, it_folder = 'bulk', cluster = 'magnus', up='up2', run=2)    

    st_some_na = st_int.copy()
    els = st_some_na.get_elements()
    els_na = [idx for idx, el in enumerate(els) if el == "Na"]
    els_del = random.sample(els_na, int(0.9*len(els_na)))
    st_some_na = st_some_na.remove_atoms(els_del)
    add('bulk.some_na', '9_bulk_eos_isif3_ecut', 1, input_st = st_some_na, it_folder = 'bulk', cluster = 'magnus', up='up2', run=2)    
    
    st_al_deint = st_al_dist.copy()
    els = st_al_deint.get_elements()
    els_na = [idx for idx, el in enumerate(els) if el == "Na"]
    els_del = random.sample(els_na, int(0.8*len(els_na)))
    st_al_deint = st_al_deint.remove_atoms(els_del)

    add('bulk.al.some_na_dead', '9_bulk_eos_isif3_ecut', 1, input_st = st_al_deint, it_folder = 'bulk', cluster = 'magnus', up='up2', run=2)    
    

# Other positions 
if 0:
    # Sampled Li atoms to remove
    # [1, 14, 5, 3, 2, 8, 0, 11, 13, 7, 9, 15, 12, 4]
    # [2, 7, 9, 0, 4, 12, 15, 11, 3, 5, 6, 13, 10, 14]
    # [14, 3, 0, 5, 9, 2, 7, 4, 1, 11, 13, 10, 8, 15]
    # [10, 12, 14, 11, 6, 15, 3, 0, 1, 5, 9, 2, 13, 7]
    # [9, 1, 4, 7, 6, 15, 2, 14, 5, 12, 11, 0, 10, 3]
    
    for idx in range(5):
        st = db['bulk.inter.ifc.ifc.ifc', '9_bulk_rel', 1].copy().end
        els = st.get_elements()
        els_na = [idx for idx, el in enumerate(els) if el == "Na"]
        els_del = random.sample(els_na, int(0.9*len(els_na)))
        st = st.remove_atoms(els_del)
        
        print(els_del)
        
        # add(f'bulk.some_na.sample_{idx}', '9_bulk_eos', 1, input_st = st, it_folder = 'bulk', calc_method = 'uniform_scale', ngkpt=[1,1,1], n_scale_images=8, scale_region = (-5, 5), cluster = 'razor128', run=2)
    
if 0:
    for idx in range(5):
        res_loop(f'bulk.some_na.sample_{idx}.su', '9_bulk_eos', list(range(1,11)) + [100], show = 'fit', analys_type = 'fit_a', cluster = 'razor128', up="up2")
        