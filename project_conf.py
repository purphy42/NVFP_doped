# -*- coding: utf-8 -*-
"""
Control of project

TODO:
cif2cell installation check or add to siman
"""
from __future__ import division, unicode_literals, absolute_import 

NEW_BATCH = True   # for testing new batch system based on set sequences 
check_job = 0
PBS_PROCS = False # if true than #PBS -l procs="+str(number_cores) is used
WALLTIME_LIMIT = True

"""Cluster constants"""
# cluster_address = 'aksenov@10.30.16.62' #
# CLUSTER_ADDRESS = cluster_address
# cluster_home    = '/home/aksenov/' # needed only for SLURM std out and std err
# CLUSTER_PYTHONPATH = '/usr/lib64/python2.7/site-packages/numpy'

# SCHEDULE_SYSTEM = 'SLURM' #see write_batch_header()
# corenum = 16; #queue = ' -l cmmd '
# CORENUM = corenum

CLUSTERS = {}
DEFAULT_CLUSTER = 'magnus'
PATH2PROJECT = '/nvpf_al_doped/' # path to project on cluster relative to home folder
# project_path_cluster = '' 
#PATH_TO_PROJECT_ON_CLUSTER = project_path_cluster
PATH_TO_PROJECT_ON_COMP = "/home/arseniy/Desktop/work/nvpf_al_doped/"


CLUSTERS['pardus'] = {
'address':'pardus',
'vasp_com':'mpirun  vasp_gam',
'homepath':'/home/arseniy.burov/nvpf_al_doped/',
'schedule':'PBS',
'walltime':'24:00:00',
'corenum':16,
'nodes':1, 
'pythonpath':'/usr/lib64/python2.7/site-packages/numpy',
'modules':'module load Compilers/Intel/psxe_2017.4; module load MPI/intel/2017.4.239;  module load QCh/VASP/5.4.4/psxe2017.4; module load ScriptLang/python/2.7; \n',
}

#'homepath':'/gss/home/arseniy.burov/',


CLUSTERS['arkuda'] = {
'address':'arkuda',
'vasp_com':'mpirun  /gss/home/a.burov/soft/vasp_gam',
'homepath':'/gss/home/a.burov/nvpf_al_doped/',
'schedule':'PBS',
'procmemgb': 10,
'walltime':'24:00:00',
# 'procmemgb':8, # 16 gb per core, pmem in pbs
'corenum':16,
'nodes':1,
'pythonpath':'',
'sshpass':True,
'path2pass':'/home/anton/.ssh/arkuda.p',  # в этом файле просто строчка с паролем, права read только для creator. Для всех остальных убрать все права
'modules':'module load  QCh/VASP/5.4.4\nmodule load ScriptLang/python/3.6u3_2018i;\n\nuptime\n',
}


CLUSTERS['magnus'] = {
'address': 'magnus',
'vasp_com':'mpirun vasp_gam',
'homepath':'/home/a.burov/nvpf_al_doped/',
'schedule':'SLURM',
'corenum': 16,
'procmemgb': 8,
'nodes': 1,
'partition':'AMG-medium',
'modules':'module load Compiler/Intel/17u8; \
module load Q-Ch/VASP/5.4.4_OPT; module load ScriptLang/python/3.10i_2020u4; \
\nulimit -s unlimited\n\
'
}

CLUSTERS['razor'] = {
'address':'razor',
'vasp_com':'mpirun vasp_gam',
'homepath':'/home/a.burov/nvpf_al_doped/',
'schedule':'SLURM',
'corenum':8,
'procmemgb': 8,
'modules':'module load devtools/compiler/nvhpc/20.11; \
module load q-ch/vasp/5.4.4_OPT; \
\nulimit -s unlimited\n\
'
}


CLUSTERS['razor24'] = {
'address':'razor24',
'vasp_com':'mpirun vasp_gam',
'homepath':'/ssd2/home/a.burov/nvpf_al_doped/',
'schedule':'SLURM',
'corenum':8,
'procmemgb': 8,
'modules':'module load devtools/compiler/nvhpc/20.11; \
module load q-ch/vasp/5.4.4_OPT; \
\nulimit -s unlimited\n\
'
}


CLUSTERS['razor32'] = {
'address':'razor32',
'vasp_com':'mpirun vasp_gam',
'homepath':'/home/a.burov/nvpf_al_doped/',
'schedule':'SLURM',
'corenum': 8,
'procmemgb': 8,
'modules':'source /etc/profile.d/modules.sh; \
module load devtools/mpi/openmpi/4.1.4/gcc/11.2; \
module load q-ch/vasp/5.4.4; \
\nulimit -s unlimited\n\
'
}

CLUSTERS['razor64'] = {
'address':'razor64',
'vasp_com':'mpirun -np 8 vasp_gam',
'homepath':'/home/a.burov/nvpf_al_doped/',
'schedule':'SLURM',
'corenum': 16,
'procmemgb': 16,
'modules': 'source /etc/profile.d/modules.sh; \
module load devtools/compiler/aocl/4.0.0; \
module load devtools/mpi/openmpi/4.1.5/gcc/11.3; \
module load q-ch/vasp/5.4.4; \
\nulimit -s unlimited\n\
'
}


CLUSTERS['r64'] = {
'address':'r64',
'vasp_com':'mpirun -np 16 vasp_gam',
'homepath':'/home/a.burov/nvpf_al_doped/',
'schedule':'SLURM',
'corenum': 16,
'procmemgb': 16,
'modules': 'source /etc/profile.d/modules.sh; \
module load devtools/compiler/aocl/4.0.0; \
module load devtools/mpi/openmpi/4.1.5/gcc/11.3; \
module load q-ch/vasp/5.4.4; \
\nulimit -s unlimited\n\
'
}


CLUSTERS['r128'] = {
'address':'r128',
'vasp_com':'srun vasp_gam',
'homepath':'/home/a.burov/nvpf_al_doped/',
'schedule':'SLURM',
'corenum':16,
'modules': 'source /etc/profile.d/modules.sh; \
module load devtools/mpi/mpich/4.2.1/gcc/11.2; \
module load devtools/math/mkl/2024.1.0.695; \
module load q-ch/vasp/5.4.4_mpich_mkl; \n \
ulimit -s unlimited\n\
'
}


CLUSTERS['razor128'] = {
'address':'razor128',
'vasp_com':'srun vasp_std',
'homepath':'/home/a.burov/nvpf_al_doped/',
'schedule':'SLURM',
'corenum':16,
'modules': 'source /etc/profile.d/modules.sh; \
module load devtools/mpi/mpich/4.2.1/gcc/11.2; \
module load devtools/math/mkl/2024.1.0.695; \
module load q-ch/vasp/5.4.4_mpich_mkl; \n \
ulimit -s unlimited\n\
'
}


"""Local constants"""
PATH2POTENTIALS = '/home/arseniy/Desktop/vasp/potpaw_paw/potpaw_PBE_MPIE'
PATH2EDITOR = "subl"
pmgkey = "dzpOVLsVP3VWa3VIOB"
mpkey = "LTSM6dStBrl69FjopxP7KdZBP35B1yh7"

path_to_paper        = '/home/anton/Research/CEStorage/aksenov_report/'
# PATH2DATABASE        = '/home/aksenov/Data/CEStorage/_aksenov'
PATH2DATABASE        = '/home/anton/Data/CEStorage/'
# gb4_geo_folder       = '/home/dim/Simulation_wrapper/gb4/out/'
#we have gb5!
PATH2JMOL  = '/home/arseniy/Desktop/Jmol/jmol.sh'
PATH2VESTA = '/home/arseniy/Desktop/VESTA-gtk3/VESTA'
PATH2NEBMAKE = '/home/arseniy/Desktop/study/comp_chemistry/final_project/vts/nebmake.pl'

geo_folder           = './'
# path_to_images       = '/home/aksenov/ydisk/cathode_report/images/'
path_to_images       = path_to_paper+'/fig/'
path_to_jmol         = '/home/arseniy/Desktop/Jmol/jmol.sh'
path_to_wrapper      = '/home/anton/Simulation_wrapper/'

# RAMDISK              = '/mnt/ramdisk/'
RAMDISK              = None
EXCLUDE_NODES  = 1


"""List of constants determined during installation"""
CIF2CELL = True 








"""List of manually added calculations:"""
MANUALLY_ADDED = [# calc name, calc folder, calc des  
    ( 'Li111'        ,"Li",        "2 Li"                                  ),
    ( 'Rb111'        ,"Rb/bcc",        "2 Rb"                                  ),
    ]




















"""
Naming conventions:

endings:
'_ml' - was used to show that this calculation uses manual equilibrium lattice determination and 
contains several versions of identical structures with different
lattice constants. Now not in use, because I always use this method. Usually 16 versions for hcp;

'_r' - calculation with structure constructed for fitted lattice constants; 
Now was replaced with '.f'; Usually one version.
'.ur' - unrelaxed
.r - relaxed atomic positions
.o - optimised cell and volume and atomic positions automatically
'.f'  - fitted
'.fr' - means that current calculation based on the structure for which lattice constants were fitted and
positions of atoms were relaxed. However see description to know for wich set they were fitted and relaxed.
Calculations with '.f' and '.fr' can have different versions which are correspondig to different sets.

.m - only matrix, all impurities were removed and matrix was freezed


letters in name, wich are usually between didgits and element's names:
b - stands for bulk, which denote ideal cells without boundaries.
g - cells with grain boundary;
v - means that impurity is in the volume of grain; far away from boundaries;
i - means that impurity is close to interface plane (grain boundary)

Versions:
20 - usually means that lattice constatns was used from other calculation and this is very good assumtion.


"""



