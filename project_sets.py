
import copy
# from header import * 
from siman import header
from siman.set_functions import InputSet, inherit_iset, make_sets_for_conv, init_default_sets
"""
remove update_set() completly
"""


#1 - only volume; v  isif = 5
#2 - full relax;    vsa
#8 - no relaxation; 0
#9 - only atoms;    a


#set_potential uses relative paths







"""List of user VASP sets obtained on inheritance principle """
"""Syntax:  ("set_new", "set_old", {"param1":value1, "param2":value2, ...})
        - set_new - name of new set
        - set_old - name of base set used for creating new set
        - {} -      dictionary of parameters to be updated in set_new

"""
  # Ueff::list(string=numeric):=["V"=3.1,"Cr"=3.5,"Mn"=3.9,"Fe"=4.0,"Co"=3.4,"Ni"=6.0,"Cu"=4.0,"Mo"=3.5,"Ag"=1.5]
dftu_packet = {'ISTART'   :1,   'ICHARG':1,  'LDAUTYPE':2, 'LASPH':'.TRUE.', 
                'LDAUPRINT':2, 'LMAXMIX' :4, 'LDAU' :'.TRUE.',
                'LDAUL':{'Ti':2,   'Co':2  , 'Fe':2  , 'Ni':2  , 'Mn':2  , 'V':2   , 'Cr':2 },
                'LDAUU':{'Ti':0,   'Co':3.4, 'Fe':4.0, 'Ni':6.2, 'Mn':3.9, 'V':3.1 , 'Cr':3.5, 'Fe/S':1.9 },
                'LDAUJ':{'Ti':0.0, 'Co':0.0, 'Fe':0.0, 'Ni':0.0, 'Mn':0.0, 'V':0.0 , 'Cr':0.0, 'Fe/S':0   } } # universal set, Jain2011 azh values, Ni from genome
dftu_packet1 = {'ISTART'   :1,   'ICHARG':1,  'LDAUTYPE':2, 'LASPH':'.TRUE.', 
                'LDAUPRINT':2, 'LMAXMIX' :4, 'LDAU' :'.TRUE.',
                'LDAUL':{'Ti':2,   'Co':2  , 'Fe':2  , 'Ni':2  , 'Mn':2  , 'V':2   , 'Cr':2, 'W':2 },
                'LDAUU':{'Ti':0,   'Co':3.4, 'Fe':4.0, 'Ni':6.2, 'Mn':3.9, 'V':3.1 , 'Cr':3.5, 'Fe/S':1.9, 'W':4 },
                'LDAUJ':{'Ti':0.0, 'Co':0.0, 'Fe':0.0, 'Ni':0.0, 'Mn':0.0, 'V':0.0 , 'Cr':0.0, 'Fe/S':0, 'W':1   } }
dftu_packet_h = {'ISTART'   :1,   'ICHARG':1,  'LDAUTYPE':2, 'LASPH':'.TRUE.', 
                'LDAUPRINT':2, 'LMAXMIX' :4, 'LDAU' :'.TRUE.', 
                'LDAUL':{'Ti':2,   'Co':2  , 'Fe':2  , 'Ni':2  , 'Mn':2  , 'V':2   , 'Cr':2,               'W':2 },
                'LDAUU':{'Ti':0,   'Co':3.4, 'Fe':4.0, 'Ni':6.2, 'Mn':5,   'V':3.1 , 'Cr':3.5, 'Fe/S':1.9, 'W':4 },
                'LDAUJ':{'Ti':0.0, 'Co':0.0, 'Fe':0.0, 'Ni':0.0, 'Mn':0.0, 'V':0.0 , 'Cr':0.0, 'Fe/S':0,   'W':1   } }

dftu_packet_h2 = {'ISTART'   :1,   'ICHARG':1,  'LDAUTYPE':2, 'LASPH':'.TRUE.', 
                'LDAUPRINT':2, 'LMAXMIX' :4, 'LDAU' :'.TRUE.',
                'LDAUL':{'Ti':2,   'Co':2  , 'Fe':2  , 'Ni':2  , 'Mn':2  , 'V':2   , 'Cr':2,               'W':2 , 'Ru': 2  , 'Mo': 2},
                'LDAUU':{'Ti':0,   'Co':5,   'Fe':4.0, 'Ni':6.2, 'Mn':5,   'V':3.1 , 'Cr':3.5, 'Fe/S':1.9, 'W':4 , 'Ru': 4  , 'Mo': 3},
                'LDAUJ':{'Ti':0.0, 'Co':0.0, 'Fe':0.0, 'Ni':0.0, 'Mn':0.0, 'V':0.0 , 'Cr':0.0, 'Fe/S':0,   'W':1 , 'Ru': 0.0, 'Mo': 0} }

dftu_packet_h3 = {'ISTART'   :1,   'ICHARG':1,  'LDAUTYPE':2, 'LASPH':'.TRUE.', 
                'LDAUPRINT':2, 'LMAXMIX' :4, 'LDAU' :'.TRUE.',
                'LDAUL':{'Ti':2,   'Co':2  , 'Fe':2  , 'Ni':2  , 'Mn':2  , 'V':2   , 'Cr':2,               'W':2 , 'Ru': 2  , 'Mo': 2, 'Zn':2},
                'LDAUU':{'Ti':0,   'Co':5,   'Fe':4.0, 'Ni':6.2, 'Mn':5,   'V':3.1 , 'Cr':3.5, 'Fe/S':1.9, 'W':4 , 'Ru': 4  , 'Mo': 3, 'Zn':5},
                'LDAUJ':{'Ti':0.0, 'Co':0.0, 'Fe':0.0, 'Ni':0.0, 'Mn':0.0, 'V':0.0 , 'Cr':0.0, 'Fe/S':0,   'W':1 , 'Ru': 0.0, 'Mo': 0, 'Zn':0} }

dftu_packet_rsf = {'ISTART'   :1,   'ICHARG':1,  'LDAUTYPE':2, 'LASPH':'.TRUE.', 'LDAUPRINT':2, 'LMAXMIX' :4, 'LDAU' :'.TRUE.', 'LDAUL':{'Ti':2,   'Co':2  , 'Fe':2  , 'Ni':2  , 'Mn':2  , 'V':2   , 'Cr':2,               'W':2 , 'Ru': 2  , 'Mo': 2, 'Zn':2}, 'LDAUU':{'Ti':0,   'Co':3.32,   'Fe':4.0, 'Ni':6.2, 'Mn':3.9,   'V':3.25 , 'Cr':3.7, 'Fe':5.3, 'W':6.2, 'Ru': 4  , 'Mo': 4.38, 'Zn':5}, 'LDAUJ':{'Ti':0.0, 'Co':0.0, 'Fe':0.0, 'Ni':0.0, 'Mn':0.0, 'V':0.0 , 'Cr':0.0, 'Fe':0,   'W':1 , 'Ru': 0.0, 'Mo': 0, 'Zn':0} }


dftu_packet_off = {'LDAU' :None, 'LASPH':None, 'LDAUPRINT':None, 'LDAUTYPE':None,  'LDAUL':None, 'LDAUU':None, 'LDAUJ':None, }

YBaCoO_dftu =  {'LDAUU':{'Co':5}, 'LDAUJ':{'Co':0.8} }

mag_packet = {
    'GGA_COMPAT': '.FALSE.',
    'ISPIN':2,
    'LORBIT':11, #more info
    'magnetic_moments':{'Ti':0.6, 'V':5, 'Fe':5, 'Co':5, 'Mn':5, 'Ni':5, 'Cr':5 }

}

mag_packet_n = {

    'magnetic_moments':{'Ti':0.6, 'V':5, 'Fe':5, 'Co':0, 'Mn':5, 'Ni':5, 'Cr':5, 'Mo':0 }
}

mag_packet_lfp = {

    'magnetic_moments':{'Fe':5, 'Co':4, 'Mn':5, 'Ni':3 }
}


#hybrid packet
hse6_pack = {'ISTART':1, 'LHFCALC':'.TRUE.', 'HFSCREEN':0.2, 'add_nbands':1.1, 'ALGO':'All', 'TIME':0.4}
hse6_pack_low = hse6_pack.copy()
hse6_pack_low.update({'PRECFOCK':'Fast', 'NKRED':2})


mix_mag_packet =  {'AMIX':0.2, 'BMIX':0.00001, 'AMIX_MAG':0.8, 'BMIX_MAG':0.00001} #linear mixing fine
mix_mag_packet_fine =  {'AMIX':0.1, 'BMIX':0.00001, 'AMIX_MAG':0.4, 'BMIX_MAG':0.00001} #even finer linear mixing

ion_relax_packet = {'NSW':25, 'EDIFFG':-0.025, 'EDIFF':0.0001, 'ISIF':2}
static_run_packet = {'NSW':0, 'EDIFF'     : 6e-06, 'NELM':50}
my_low_pack = {'KSPACING':0.3, 'ENCUT':400, 'ENAUG':400*1.75, 'POTIM':0.2, 'NELM':20, 'EDIFFG':-0.05 }
acc_pack  = {'PREC':'Accurate', 'ADDGRID':'.TRUE.', 'EDIFF':6e-6, 'EDIFFG':-0.010, 'NELM':50, 'NSW':50, 'ISTART':1, 'ICHARG':0 }
acc_pack_relax  = {'PREC':'Accurate', 'ADDGRID':'.TRUE.', 'EDIFF':1e-8, 'EDIFFG':-0.010, 'NSW':50, 'NELM':50, 'ISTART':1, 'ICHARG':0 }
acc_pack2_stat   = {'PREC':'Accurate', 'ADDGRID':'.TRUE.', 'EDIFF':1e-8, 'LREAL':False, 'NSW':0, 'NELM':50, 'ISTART':1, 'ICHARG':0 }
acc_pack2_relax  = {'PREC':'Accurate', 'ADDGRID':'.TRUE.', 'EDIFF':1e-8, 'LREAL':False, 'EDIFFG':-0.025, 'NELM':50, 'NSW':50, 'ISTART':1, 'ICHARG':0 }
acc_pack4_relax  = {'PREC':'Accurate', 'ADDGRID':'.TRUE.', 'EDIFF':1e-4, 'LREAL':False, 'EDIFFG':-0.025, 'NELM':50, 'NSW':50, 'ISTART':1, 'ICHARG':0 }


dos_pack = {'NSW':0, 'LORBIT':12, 'ISMEAR':-5, 'SIGMA':None, 'LAECHG':'.TRUE.', 'EMIN':-10, 'EMAX':14, 'NEDOS':2000, 'KSPACING':0.15, 'savefile':'dox'}
bader_pack = {'PREC':'Accurate', 'ADDGRID':'.TRUE.', 'EDIFF':1e-08, 'LAECHG':'.TRUE.', 'NELM':100, 'NSW':0, 'ICHARG':1, 'savefile' : 'acox'}
surface_pack = {'AMIN':0.01, 'AMIX':0.2, 'BMIX':0.001, 'NELMIN':8, 'IDIPOL':3, 'LDIPOL':'.TRUE.', 'LVTOT':'.TRUE.'} # from pymatgen
surface_pack2 = {'AMIN':None, 'AMIX':None, 'BMIX':None, 'NELMIN':8, 'IDIPOL':3, 'LDIPOL':'.TRUE.', 'LVTOT':'.TRUE.', 'NELM':50, 'ICHARG':1} # 
# slab_incar["DIPOL"] = structure.center_of_mass # please consider


partial_chg_pack = {'savefile':'p', 'LWAVE':False, 'ICHARG':0, 'LPARD':'TRUE', 'EINT':'-0.75 0', 'NBMOD':-3}


dos_pack2 = dos_pack.copy()
dos_pack3 = dos_pack.copy()
dos_pack3.update({'PREC':'Accurate', 'ADDGRID':'.TRUE.', 'EDIFF':6e-6, 'NELM':50, })
# dos_pack2.update({83:'Bi_pv', 34:'Se'})
mag_relax = mag_packet.copy()
mag_relax.update(ion_relax_packet)
# print mag_relax
sv_pot_pack = {'set_potential':{3:"Li_sv2",    8:"O", 9:"F", 11:'Na_sv', 37:'Rb_sv', 15:"P", 16:'S', 19:'K_sv', 22:"Ti_sv_new", 23:"V_sv_new", 25:"Mn_sv",    26:"Fe_sv",     27:"Co_sv" , 28:"Ni_pv", 33:'As_d'  }} #except O_sv, which requires 1000 eV ecut at least
sv_pot_pack_sn = {'set_potential':{3:"Li_sv2",    8:"O", 9:"F", 11:'Na_sv', 37:'Rb_sv', 15:"P", 16:'S', 19:'K_sv', 22:"Ti_sv_new", 23:"V_sv_new", 25:"Mn_sv",    26:"Fe_sv",     27:"Co_sv" , 28:"Ni_pv", 33:'As_d' , 50:"Sn_d" }} #except O_sv, which requires 1000 eV ecut at least
pot_pack = {'set_potential':{1:'H', 3:"Li",  5:'B', 6:'C',  8:"O", 9:"F", 11:'Na', 12:'Mg', 15:"P", 16:'S', 19:'K_pv',     20:'Ca',         22:"Ti",        23:"V", 24:'Cr',   25:"Mn",       26:"Fe",        27:"Co_new", 28:"Ni_new", 33:'As', 37:'Rb_pv', 39:'Y_sv', 45:'Rh', 56:'Ba_sv',   83:'Bi_pv', 34:'Se',    }  }
pot_pack_rsf = {'set_potential':{1: "H", 2: "He", 3:"Li_sv", 4: "Be_sv", 5: "B", 6: "C", 7: "N",  8:"O", 9:"F", 10: "Ne",  11:'Na_pv',
    12: "Mg_pv", 13: "Al", 14: "Si", 15: "P", 16: "S", 17: "Cl", 18: "Ar", 19: "K_sv", 20: "Ca_sv", 21: "Sc_sv", 22: "Ti_d", 23:"V_pv",
    24: "Cr_pv", 25: "Mn_pv", 26: "Fe_pv", 27: "Co", 28: "Ni_pv", 29: "Cu_pv", 30: "Zn", 31: "Ga_d", 32: "Ge_d", 33: 'As', 34: "Se",
    35: "Br", 36: "Kr", 37: "Rb_sv", 38: "Sr_sv", 39: "Y_sv", 40: "Zr_sv", 41: "Nb_pv", 42: "Mo_pv", 43: "Tc_pv", 44: "Ru_pv", 45: "Rh_pv", 46: "Pd", 47: "Ag", 48: "Cd", 49: "In_d", 50: "Sn_d", 51: "Sb", 52: "Te", 53: "I", 54: "Xe", 55: "Cs_sv", 56: "Ba_sv", 57: "La",
    58: "Ce", 59: "Pr_3", 60: "Nd_3", 61: "Pm_3", 62: "Sm_3", 63: "Eu", 64: "Gd", 65: "Tb_3", 66: "Dy_3", 67: "Ho_3", 68: "Er_3",
    69: "Tm_3", 70: "Yb_3", 71: "Lu_3", 72: "Hf_pv", 73: "Ta_pv", 74: "W_pv", 75: "Re_pv", 76: "Os_pv", 77: "Ir",  78: "Pt", 79: "Au",
    80: "Hg", 81: "Tl", 82: "Pb_d", 83: "Bi", 84: "Po", 85: "At_d", 86: "Rn", }} #except O_sv, which requires 1000 eV ecut at least

over = ''

YBC8mag2 = '0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6'
YBC8mag4 = '0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 -5 -5 5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6'

band_pack_monibc = {'ICHARG':11, 'LORBIT':11, 
             'k_band_structure':[101, ('G', 0, 0, 0), ('R', 0.5, 0.5, 0.5), 
                                 ('R\'', -0.5, -0.5, -0.5), ('T', 0, 0.5, 0.5), ('T\'', 0, -0.5, -0.5),
                                 ('U', 0.5, 0, 0.5), ('U\'', -0.5, 0, -0.5), ('V', 0.5, 0.5, 0),
                                 ('V\'', -0.5, -0.5, 0), ('X', 0.5, 0, 0), ('X\'', -0.5, 0, 0),
                                 ('Y', 0, 0.5, 0), ('Y\'', 0, -0.5, 0), ('Z', 0, 0, 0.5), ('Z\'', 0,0,-0.5)] }

user_vasp_sets = [


('8', 'static', {}),
('8','8',pot_pack,),
('9',    '8', ion_relax_packet),
('8U',    '8', dftu_packet ),

('9u', '8u',    ion_relax_packet),  #ion relax 



('1' ,'9', my_low_pack ),
('1m' ,'1', mag_packet ),
('0m' ,'1m',    static_run_packet, ),  #
('0mAB', '0m', bader_pack),
('0mABI0', '0mAB', {'ISMEAR':0, 'SIGMA':0.1}),
('0mbox', '0m',    {'magnetic_moments':{'O':1.}, 'ISTART':0,'KSPACING':10., 'KGAMMA':'.FALSE.','add_nbands':2, 'ISMEAR':0, 'LREAL':'.FALSE.', 'SIGMA':0.01},),  #
('0mboxn',    '0mbox', {'NELM':100, 'add_nbands':4}),


('1ur' ,'9u',   {'u_ramping_nstep':3, 'KSPACING':0.3, 'ENCUT':400, 'ENAUG':400*1.75, 'POTIM':0.2, 'NELM':20, 'EDIFFG':-0.05 } ),  # low quality
('1ur10' ,'1ur',    {'u_ramping_nstep':10 } ),  #
('1urk15' ,'1ur',    {'KSPACING':0.15 } ),  #
('1urp03' ,'1ur',    {'POTIM':0.03 } ),  #
('1urn1' ,'1ur',    {'NELM':10 } ),  #
('1urnp' ,'1ur',    {'NPAR':4 } ),  #
('1urNM' ,'1ur',    {'NELMIN':8 } ),  #
('1u' ,'1ur',    {'u_ramping_nstep':None }, ),  #
('1ui' ,'1u', {} ),  #for inherit_xred option, make control from here


('1u_co' , '1u',  {**mag_packet_n, 'NPAR': 4}, ''),
('1ul_new' ,'1u',     {'IDIPOL':3, 'LPLANE': '.FALSE.'}, ),
('1uc' ,'1u',     {'IBRION':2, 'LPLANE': '.FALSE.'}, ),
('1ulc' ,'1ul_new',     {'IBRION':2}, ),
('1ULC' ,'1ulc',     {'IBRION':2, 'PREC':'Accurate', 'NSW': 45, 'NPAR': 4}),
('1ULC_co' ,'1ulc',     {'IBRION':2, 'PREC':'Accurate', 'NSW': 45, 'NPAR': 4, 'MAGMOM' : None }),
('1ULC_co_n' ,'1ULC_co',     { 'NSW': 30 }),
('1ULC_co1' , '1ULC_co', {**mag_packet_n, 'LDIPOL': '.TRUE.'}, over), 


('1uh_co' , '1u_co',  dftu_packet_h, ''),
('1uh2_co' , '1u_co',  dftu_packet_h2, ''),
('1h_co' , '1u_co',  {**dftu_packet_off, 'NPAR' : None, 'NSIM' :None}, ''),



#For LVP
('9_bulk_mp', 'bulk', {'NSW':99, 'EDIFFG': -0.05, 'EDIFF': 1e-5, 'ISIF':2, 'ENCUT':520, 'ENAUG': 780, 'add_nbands': 1.1, "GGA_COMPAT": ".FALSE.", 'KSPACING': 0.3, 'ISMEAR': 0, 'SIGMA': 0.2, 'NELM': 100, 'NPAR': None, 'LREAL': 'Auto', 'ISTART': 1,  'ISPIN': 2, "LORBIT": 11, "LAECHG": ".TRUE.", 'POTIM': 0.1, 'LASPH': '.TRUE.',  'MAXMIX': None, 'GGA_COMPAT': None, 'PREC': 'Accurate', 'LPLANE': None, 'ALGO': 'Normal',  "NELMIN": 4, "LWAVE": ".FALSE.", "IWAVPR": 11, "IBRION": 1, "LMIXTAU": ".TRUE.", 'savefile' : 'acoxt', 'LDAUL':{'V': 2, 'Li': 0, 'P': 0, 'O': 0, 'F': 0}, 'LDAUU':{'V': 3.25}, 'LDAUJ': {'V': 0.0}, **pot_pack_rsf },  'over'),


('9_bulk', '9', {'NSW':50,'EDIFFG':-0.05, 'EDIFF':1e-5, 'ISIF':2, 'ENCUT':520, 'ENAUG': 780, 'add_nbands':1.1, 
    'KSPACING': 0.3, "LDAU": ".TRUE.", 'LDAUTYPE': 2, 'LDAUPRINT': 2, 'LDAUL':{'V': 2, 'Li': 0, 'P': 0, 'O': 0, 'F': 0}, 'LDAUU':{'V': 3.1}, 'ISMEAR': 0, 'SIGMA':0.1,'NELM':100, 'NPAR': None, 'LREAL': 'Auto', 'ISTART': 1,  'ISPIN': 2, 'LMAXMIX': 4, 'POTIM': 0.15, 'LASPH': '.TRUE.', 'LORBIT': 11, 'GGA_COMPAT': ".FALSE.", 'PREC': 'Accurate', 'LPLANE': ".TRUE.", 'LSCALU': '.FALSE.', 'ALGO': 'Normal',  "NELMIN": 8, "NELMDL": -8, 'LDAUJ': {'V': 0.0}, "LWAVE": ".FALSE.", "IWAVPR": 11, "IBRION": 1 }, 'over'),

('9_bulk_eos', '9_bulk', {"ISIF": 4, "NELM": 100, "NSW": 35 }, 'over'),


('9_bulk_met', '9_bulk', {'ISMEAR': 2, 'KSPACING': 0.3, 'add_nbands':3.0, "SIGMA": 0.01}, "over"),

('9_bulk_rel', '9_bulk', {'NSW':100, 'POTIM': 0.1, 'EDIFF': 1e-5, "NELMDL": -8, "NELMIN": 4}, "over"),  
('9_bulk_rel_fast', '9_bulk', {'NSW':150, 'POTIM': 0.1, 'EDIFF': 1e-5, "KSPACING": 2.0}, "over"),  

('9_bulk_md_eq', '9_bulk', {'IBRION':0, 'ISIF': 2, 'SIGMA': 0.026, 'POTIM': 2, 'PREC': 'Single', 
    'NSW': 2000, 'TEBEG': 600, 'TEEND': 600, 'SMASS':0, 'MDALGO': 2, 'LWAVE': '.FALSE.', 
    'LCHARG': ".FALSE.", 'ALGO': 'Very Fast', 'NELMDL': None, 'NELMIN': None,
    'ENCUT': 300, 'ENAUG': 500, "KSPACING": 1.0, "ADDGRID": ".TRUE.", "EDIFF": 1e-4,
     "PSTRESS": 0, "IWAVPR": 12, "MAXMIX": 40, "NBLOCK": 50, 'savefile' : 'acoxt'}, "over"),




# ANALYSIS OF CHARGES
('9bulk_dos', '9_bulk', {'LORBIT':12, 'ISMEAR':-5, 'SIGMA':None, 'LAECHG':'.TRUE.', 'EMIN':-20, 
    'EMAX':20, 'NEDOS':2000, 'KSPACING':0.2, 'savefile':'dox', 'LCHARG': 'TRUE', 'NSW':0, 'IBRION': -1,
    "NPAR": 2, "NFREE": 20, "POTIM": 0.04, 'PREC':'Accurate', 'ADDGRID':'.TRUE.', 'EDIFF':1e-6, 'NELM':300, 
     "NELMIN": 8, "NELMDL": -8, "NSW": 0, 'LCHARG': 'TRUE' }, "over"),

# Occupation matrix calculations
('0u_prio' ,  '9neb_nfree_base_kp',  {'NSW':0, "LDAU": ".TRUE.", 'LDAUTYPE': 2, 'LDAUPRINT': 2,
     'LDAUL':{'V': 2, 'Li': -1, 'P': -1, 'O': -1, 'F': -1},'LDAUU':{'V': 0.0}, 'LSCALU': '.FALSE.',
    'LDAUJ': {'V': 0.0}, "SIGMA": 0.2, 'AMIN': 0.01, 'AMIX': 0.2, 'BMIX': 1.0 }, ''), # single point set

('0u' ,  '0u_prio',     {'NSW':0, "NELM": 300}, ''), # single point set
('1u_omc' ,  '0u_prio',     {'OCCEXT':1}, ''), # OMC set
('1u_omcs' ,'1u_omc',    {'set_sequence':['0u']}, ), # set producing two calculations in sequence: OMC -> single point 








('1h_co_g' , '1h_co',  {'ISMEAR':0}, ''),
('4h_co_g' , '1h_co_g',  {'ISIF':4}, '0'),
('1h_co_g2' , '1h_co_g',  {'NELM':50}, ''),
('1h_co_g2_n' , '1h_co_g2',  {'IBRION':2, 'NPAR':4, }, ''),
('1uh_co_g2' , '1h_co_g2',  dftu_packet_h2, ''),
('4uh_co_g2' , '1uh_co_g2',  {'ISIF':4}, ),
('4uh_co_g2occ' , '1uh_co_g2',  {'OCCEXT':1}, ''),

('1uh_co_g2a1' , '1uh_co_g2',  {'PREC':'Accurate'}, ''),
('1uh_co_g2a' , '1uh_co_g2',  {'PREC':'Accurate', 'EDIFFG':-0.005, 'NSW':100}, ''),
('8uh_co_g2a' , '1uh_co_g2a',  {'NSW':0}, ''),

('1uh_co_g2a_elastic' , '1uh_co_g2a',  {'IBRION':6, 'ISIF':3, 'NPAR':1, 'POTIM':0.1, 'NPAR':None}, ''),
('1uh_co_g2a_phon' , '1uh_co_g2a',  {'IBRION':8, 'ISIF':3, 'NPAR':1, 'POTIM':0.1, 'NPAR':None}, ''),



('1uh_co_g3' , '1h_co_g2',  dftu_packet_h3, ''),
('1uh_co_g3_acc' , '1uh_co_g3', {'PREC':'Accurate', 'EDIFFG':-0.005, 'NSW':100} , ''),
('1uh_co_g3_nacc' , '1uh_co_g3', {'PREC':'Accurate', 'EDIFFG':-0.05, 'NSW':100} , ''),
('4uh_co_g3_nacc' , '1uh_co_g3_nacc', {'ISIF':4} , ''),



#occ
('1uh_co_g2_occ' ,  '1uh_co_g2',     {'NSW':0}, ''),
('1uh_co_g2_occ_occ' ,  '1uh_co_g2',     {'OCCEXT':1}, ''),
('1uh_co_g2_occ_occs' ,'1uh_co_g2_occ_occ',    {'set_sequence':['1uh_co_g2_occ']}, ), 

('1uh_co_g2a_occ' ,  '1uh_co_g2a',     {'NSW':0}, ''),
('1uh_co_g2a_occ_occ' ,  '1uh_co_g2a',     {'OCCEXT':1}, ''),
('1uh_co_g2a_occ_occs' ,'1uh_co_g2a_occ_occ',    {'set_sequence':['1uh_co_g2a_occ']}, ), 

('8uh_co_g2a_occ' ,  '8uh_co_g2a',     {'NSW':0}, ''),
('8uh_co_g2a_occ_occ' ,  '8uh_co_g2a',     {'OCCEXT':1}, ''),
('8uh_co_g2a_occ_occs' ,'8uh_co_g2a_occ_occ',    {'set_sequence':['8uh_co_g2a_occ']}, ),

('1uh_co_g2a1_occ' ,  '1uh_co_g2a1',     {'NSW':0}, ''),
('1uh_co_g2a1_occ_occ' ,  '1uh_co_g2a1',     {'OCCEXT':1}, ''),
('1uh_co_g2a1_occ_occs' ,'1uh_co_g2a1_occ_occ',    {'set_sequence':['1uh_co_g2a1_occ']}, ), 

('1uh_co_g3_occ' ,  '1uh_co_g3_acc',     {'NSW':20}, ''),
('1uh_co_g3_occ_occ' ,  '1uh_co_g3_acc',     {'OCCEXT':1}, ''),
('1uh_co_g3_occ_occs' ,'1uh_co_g3_occ_occ',    {'set_sequence':['1uh_co_g3_occ']}, ), 

('1uh_co_g3n_occ' ,  '1uh_co_g3_nacc',     {'NSW':20}, ''),
('1uh_co_g3n_occ_occ' ,  '1uh_co_g3_nacc',     {'OCCEXT':1}, ''),
('1uh_co_g3n_occ_occs' ,'1uh_co_g3n_occ_occ',    {'set_sequence':['1uh_co_g3n_occ']}, ), 
('1uh_co_g3n_dos_omc' ,  '1uh_co_g3n_occ_occ',    dos_pack, ''),



('1uh_co_g2a_elastic_omc' , '1uh_co_g2a_elastic',  {'OCCEXT':1}, ''),
('1uh_co_g2a_phon_omc' , '1uh_co_g2a_phon',  {'OCCEXT':1}, ''),
('1uh_co_g2a_dos_omc' ,  '1uh_co_g2a1_occ_occ',    dos_pack, ''),








('1suh2_co' , '1uh2_co',  {**surface_pack2, 'ISMEAR':0}, over),
('1s_co' , '1suh2_co',  {**dftu_packet_off, 'ISMEAR':0}, over),



('1uh2_cog' , '1uh2_co',  {'ISMEAR':0, 'SIGMA':0.05, 'POTIM':0.5}, over),

('1uh2_co_dos_hse' , '1uh2_co_dos',  {**hse6_pack_low}, over),
('1uh2_co_hse' , '1uh2_co',  {**hse6_pack_low}, over),



# Mo
('1h_mo' , '1h_co',  {**mag_packet_n, 'ISMEAR':0, 'SIGMA': None}, ''),
('1h_mo_dos' , '1h_mo',  {**dos_pack3}, ''),
('1uh_mo' , '1h_mo',  {**dftu_packet_h2}, ''),
('1uh_mo_bader' , '1uh_mo',  {**bader_pack}, ''),
('4uh_mo' , '1uh_mo',  {'ISIF':4}, ''),
('1uh_mo_dos' , '1uh_mo',  {**dos_pack3}, ''),
('1uh_mo_dos_occ' , '1uh_mo_dos', {'OCCEXT':1}, over), 


('1uh_mo4' , '1uh_mo',  {'LDAUU':{'Mo': 4.4}}, ''),

('1uh_mo6' , '1uh_mo',  {'LDAUU':{'Mo': 6}}, ''),
('4uh_mo6' , '1uh_mo6',  {'ISIF':4}, ''),
('1uh_mo6_dos' , '1uh_mo6',  {**dos_pack3}, ''),

('1uh_mo7' , '1uh_mo',  {'LDAUU':{'Mo': 7}}, ''),
('1uh_mo7_dos' , '1uh_mo7',  {**dos_pack3}, ''),
('1uh_mo_occ' , '1uh_mo', {'OCCEXT':1}, over), 
('1uh_mo7_occ' , '1uh_mo7', {'OCCEXT':1}, over), 




###############################################################################
# Ti electron
('1uh2_ti' , '1uh2_co',  {'LDAUU':{'Ti':11},'LDAUJ':{'Ti':1}, 'set_potential':{22:"Ti_sv_new2"}, 'ISMEAR':0, 'SIGMA':0.1}, ''),
('1uh2_ti_l' , '1uh2_ti',  {'set_potential':{22:"Ti"}}, ''),

('1uh2_ti_bader' , '1uh2_ti',  bader_pack, ''),
('1uh2_ti_l_bader' , '1uh2_ti_l',  bader_pack, ''),
('1uh2_ti_dos' , '1uh2_ti',  dos_pack, ''),
('1uh2_ti_l_dos' , '1uh2_ti_l',  dos_pack, ''),

# O u-corr
('1uh2_o' , '1uh2_co',  {'LDAUU':{'Mn':5,'O':7, 'Ni':6.2, 'Ru':5},'LDAUJ':{'Mn':0,'O':0, 'Ni':0, 'Ru':0}, 'LDAUL':{'Mn':2,'O':1, 'Ni':2, 'Ru':2}, 'ISMEAR':0, 'SIGMA':0.1}, over),
('1uh2_o10' , '1uh2_co',  {'LDAUU':{'Mn':5,'O':10, 'Ni':6.2, 'Ru':5},'LDAUJ':{'Mn':0,'O':0, 'Ni':0, 'Ru':0}, 'LDAUL':{'Mn':2,'O':1, 'Ni':2, 'Ru':2}, 'ISMEAR':0, 'SIGMA':0.1}, over),
('1uh2_o_ur3' , '1uh2_o',  {'u_ramping_nstep':3}, ''),
('1uh2_o10_ur3' , '1uh2_o10',  {'u_ramping_nstep':3}, ''),
('1uh2_o_sp' , '1uh2_o',  {'NSW':0}, ''),
('1uh2_o_dos' , '1uh2_o',  {**dos_pack,'NELM':50}, over),
('1uh2_o_bader' , '1uh2_o',  bader_pack, ''),
#####################################################################################################

#occ
('1uh2_o_occ' ,  '1uh2_o',     {'NSW':0}, ''),
('1uh2_o_occ_occ' ,  '1uh2_o',     {'OCCEXT':1}, ''),
('1uh2_o_occ_occs' ,'1uh2_o_occ_occ',    {'set_sequence':['1uh2_o_occ']}, ), 

#occ
('1uh2_cog_occ' ,  '1uh2_co_gaus2',     {'NSW':0}, ''),
('1uh2_cog_occ_occ' ,  '1uh2_co_gaus2',     {'OCCEXT':1}, ''),
('1uh2_cog_occ_occs' ,'1uh2_cog_occ_occ',    {'set_sequence':['1uh2_cog_occ']}, ), 

('1uh2_co_occ' ,  '1uh2_co',     {'OCCEXT':1}, ''),
('0uh2_co' ,  '1uh2_co',     {'NSW':0}, ''),
('1uh2_co_occs' ,'1uh2_co_occ',    {'set_sequence':['0uh2_co']}, ), 
##########################################


#dos
('1uh2_co_dos' , '1uh2_co',  dos_pack, ''),
('1uh2_co_dos_g' , '1uh2_co_dos',  {'ISMEAR':0, 'SIGMA':0.05}, over),
('1uh2_co_dos_part1' , '1uh2_co_dos',  {'ISYM': -1, 'savefile': 'ocvlwd'}, ''),
('1uh2_co_dos_part2' , '1uh2_co_dos_part1',  {'LPARD': '.TRUE.' }, over),

('1uh2_co_dos_part' , '1uh2_co_dos_part1',  {'set_sequence': ['1uh2_co_dos_part2'] }, ''),






('9Gub' , '1u_co',   {'LDAU': False, 'ISMEAR': 0, 'SIGMA': 0.1, 'LDIPOL': False}, over), 



]



# header.varset['9ac'].printme()
#Create u-set; be cautious
def create_u_sets(based_on):
    """
    Special function for cathode projects.
    Allows to create quickly sets with different U values based on some set.
    """
    
    #Shishkin
    U_dic = {'LiFePO4':{'Fe':2.1}, 'NaFePO4':{'Fe':2.2}, 'LiMnPO4':{'Mn':2.2,}, 
             'LiCoPO4':{'Co':2.8}, 'LiTiS2':{'Ti':3.3}, 'LiNiO2':{'Ni':4.6}, 'LiCoO2':{'Co':3.6},
             'TiS2':{'Ti':3.5},  'FePO4':{'Fe':3.7}, 'CoO2':{'Co':3.9}, 'NiO2':{'Ni':4.0}, 'MnPO4':{'Mn':4.0}, 'CoPO4':{'Co':4.2}, 
    }


    U_dic2 = {#LiTiO2 #Morgan2011, LiMn2O4 Zhou2004, other azh
    # 3.4:( 'NaLiCoPO4F'),
    # (4:'Fe',3.1:'V'):('Na2FeVF7')
    }

    U_dic_12 = {#Shishkin #LiTiO2 #Morgan2011, LiMn2O4 Zhou2004, other azh
            'LiFePO4':{'Fe':2.1}, 'NaFePO4':{'Fe':2.2}, 'LiMnPO4':{'Mn':2.2,}, 
            'LiCoPO4':{'Co':2.8}, 'LiTiS2':{'Ti':3.3}, 'LiNiO2':{'Ni':4.6}, 'LiCoO2':{'Co':3.6},
            'TiS2':{'Ti':3.5},  'FePO4':{'Fe':3.7}, 'CoO2':{'Co':3.9}, 'NiO2':{'Ni':4.0}, 'MnPO4':{'Mn':4.0}, 'CoPO4':{'Co':4.2}, 
            'LiTiO2':{'Ti':4.2}, 'LiMn2O4':{'Mn':4.9}, 
            'LiVPO4F':{'V':3.1}, 'KVPO4F':{'V':3.1}, 'LiVP2O7':{'V':3.1},
            'NaMnAsO4':{'Mn':3.9},
            # 'Na2FePO4F':{'Fe':4},  'KFeSO4F':{'Fe':4},
    }



    dic =  U_dic_12
    df = pd.DataFrame(dic)
    # print list(df.columns)
    ramping_sets = []
    simple__sets = []
    for mat in df:
        u_dict = df[mat].dropna().to_dict()

        if len(u_dict.values()) > 1:
            print_and_log('Error! Please implement name conventions for multi-element LDAUU')
            raise RuntimeError
        U = u_dict.values()[0]


        ramp_set = based_on+'r'+str(U).replace('.', '-')
        simp_set = based_on+str(U).replace('.', '-')
        
        if ramp_set not in ramping_sets:
            ramping_sets.append( (ramp_set,  based_on, {'u_ramping_region':(0, U+0.00013, 0.1)})    )
            simple__sets.append( (simp_set,  based_on, {'LDAUU':u_dict })  )

    df.loc['set'] = [s[0] for s in ramping_sets] # add row with set for each material

        
    #helper

    for mat in df:
        # print mat
        if 'Li' in mat or 'Na' in mat or 'K' in mat: 
            folder = mat
            DS = mat[2:]
            if 'K' in mat:
                DS = mat[1:]
            if 'Na2' in mat:
                DS = mat[3:]
        else:
            continue

        IS_set = df[mat]['set']
        if DS in df:
            DS_set = df[DS]['set']
        else:
            DS_set = IS_set

        # print [mat, IS_set, DS, DS_set, folder],','
        # for ise in '8u', '8ue4', '8ue5', '8uL':
        # print str([mat, 'set', DS, 'set', folder]).replace("'set'", 'ise'),','




    return ramping_sets+simple__sets   
# create_u_sets('just_helper')         
#user_vasp_sets+=create_u_sets('8U')
# user_vasp_sets+=create_u_sets('8Um')
# user_vasp_sets+=create_u_sets('8Utm')






















# for phonons you should use:
# PREC = Accurate avoid wrap around errors
# LREAL = .FALSE. reciprocal space projection technique
# EDIFF = 1E-6 high accuracy required

    #May be useful
#For very accurate energy calculations:
#s.set_vaspp['ISMEAR'] = [-5, " Tetrahedron with Blochl corrections"]
#However this approach needs at least 3 kpoints and produce errors in stress tensor and forces

        #




