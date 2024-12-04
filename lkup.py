import pandas as pd
import numpy as np

lkup = 'lkup_study_identifier.csv'
studyi = 'study_identifier.csv'
lkup_filter = 'lkup_study_filter.csv'
studi = 'study_ids_lookup.csv'

df = pd.read_csv(studyi, low_memory = False)

#list1 = [2,3,12,13,16,19,20,23,24,29,32,33,44,46,49,54,56,57,58,59,77,93,96,97,98,102,108,109,110,113,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,138,140]
list1 = [1,4,5,6,7,8,9,10,11,14,15,17,18,21,22,25,26,27,28,30,31,34,35,36,37,38,39,40,41,42,43,45,47,48,50,51,52,53,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,99,100,101,103,104,105,106,107,998,999,111,112,114,115,116,137,136,135,139]

df = df[df.study_identifier.isin(list1) == False]

df = df.astype(str)

df['family_id'] = np.where(
    df['fam_id'].str.len() < 5, df['fam_id'].str.zfill(5),""
)
df = df.drop(['fam_id'], axis=1)

df['site_code'] = np.where(
    df['study_identifier'].str.len() < 3, df['study_identifier'].str.zfill(3),""
)
df = df.drop(['study_identifier'], axis=1)

convert_dict = {'study_identifier1':int}
df = df.astype(convert_dict)

#df['study_identifier1'] = df['study_identifier1'].replace
df = df.replace({ 'study_identifier1':{
    2:'Melanoma, Priority A',
    3:'Hodgkins - Priority A',
    12:'CLL Misc. - Priority A',
    13:'CML - Priority A',
    16:'Dyskeratosis Cong',
    19:'DNS, only',
    20:'Miscellaneous',
    23:'DNS/XP',
    24:'Retinoblastoma/DNS/CMM',
    29:'NHL - Priority A',
    32:'HD-CMM',
    33:'HD-DNS',
    44:'CMM and/or DNS',
    46:'Waldenstroms Multiplex 1 - Priority A',
    49:'Retinoblastoma',
    54:'ALL',
    56:'Melanoma, Secondary',
    57:'Melanoma, Case/Control',
    58:'CMM/IMM',
    59:'DN, Case/Control',
    77:'Multiple Myeloma - Priority A',
    93:'Chordoma',
    96:'Chordoma SEER',
    97:'CLL - Priority A',
    98:'CLL - Priority B',
    102:'IBMFS',
    108:'Xeroderma Pigmentosum',
    109:'LFSS',
    110:'Sporadic Chordoma',
    113:'PPB',
    117:'AML - Priority A',
    118:'Hairy Cell Leukemia - Priority A',
    119:'Chordoma: Sporadic 1999',
    120:'Chordoma: Young',
    121:'AML- Priority B',
    122:'CML- Priority B',
    123:'NHL- Priority B',
    124:'Hairy Cell Leukemia- Priority B',
    125:'Hodgkins- Priority B',
    126:'Waldenstroms Multiplex 2 - Priority A',
    127:'Waldenstroms Simplex - Priority A',
    128:'Multiple Myeloma- Priority B',
    129:'Mixed Blood and LPD Cancers- Priority A',
    130:'Mixed Blood and LPD Cancers- Priority B',
    131:'CLL Misc. - Priority B',
    132:'Waldenstroms Multiplex 1- Priority B',
    133:'Waldenstroms Multiplex 2- Priority B',
    134:'Waldenstroms Simplex - Priority B',
    138:'XPSB',
    140:'Spitzoid Melanoma'
    }})

lookup_fam = ['05020', '05021', '05480', '04949']
df_filtered = df.loc[df['family_id'].isin(lookup_fam)]

df_reorder = df_filtered[['family_id','site_code','study_identifier1']]
df.rename(columns={'study_identifier1': 'site_name'}, inplace=True)

df_reorder.to_csv(studi, index = False)