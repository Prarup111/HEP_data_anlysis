import numpy as np
import pandas as pd
df1 = pd.read_excel('to_edit.xlsx')
def reclass (Name):
        # Redundancy न्यूनीकरण requirements here
        if (Name == 'Alnus nepalensis'):
            Al_nep_diam = np.random.choice(np.random.uniform(high = 57.5759, low = 4.011810, size = (121,)))
            return Al_nep_diam
        elif (Name == 'Betula alnoids'):
            bet_al_d = np.random.choice(np.random.uniform(high = 27.709529, low = 4.012239, size = (9,)))
            return bet_al_d
        elif (Name == 'Castanopsis indica'):
            cast_in_d = np.random.choice(np.random.uniform(high = 27.96029395, low = 4.01223949, size = (20,)))
            return cast_in_d
        elif (Name == 'Eurya acuminate'): 
            eu_d = np.random.choice(np.random.uniform(high = 19.55966752, low = 4.01223949, size = (16)))
            return eu_d
        elif (Name == 'Ficus nerifolia'): 
            fi_neri_d = np.random.choice(np.random.uniform(high = 21.06425732, low = 4.263004459, size = (3,)))
            return fi_neri_d
        elif (Name == 'Lagerstroemia parvifolia'):
            lager_d = np.random.choice(np.random.uniform(high = 12.28748344, low = 4.01223949, size = (6,)))
            return lager_d
        elif (Name == 'Lyonia ovalifolia'):
            ly_ova_d = np.random.choice(np.random.uniform(high = 13.03977834, low = 3.9763801, size = (4,)))
            return ly_ova_d
        elif (Name == 'Macaranga indica'):
            mac_ind_d = np.random.choice(np.random.uniform(high = 24.07343694, low = 4.13779751, size = (5,)))
            return mac_ind_d
        elif (Name == 'Machilus odoratissima'):
            ma_odor_d = np.random.choice(np.random.uniform(high = 17.80431274, low = 4.137621975, size = (2,)))
            return ma_odor_d
        elif (Name == 'Macropanax undulatus'):
            pan_und_d = np.random.choice(np.random.uniform(high = 28.08567643, low = 4.63779778, size = (2,)))
            return pan_und_d
        elif (Name == 'Pinus wallichiana'):
            pi_w_d = np.random.choice(np.random.uniform(high = 10.65751115, low = 4.764534395, size = (4,)))
            return pi_w_d
        elif (Name == 'Quercus lineata'):
            que_line_d = np.random.choice(np.random.uniform(high = 26.07955669, low = 4.639151911, size = (4,)))
            return que_line_d
        elif (Name == 'Quercus semecarpifolia'):
            que_carp_d = np.random.choice(np.random.uniform(high = 20.31196242, low = 4.388386943, size = (2,)))
            return que_carp_d
        elif (Name == 'Rhododendron arboreum'):
            rhod_d = np.random.choice(np.random.uniform(high = 22.8196121, low = 4.137621975, size = (1,)))
            return rhod_d
        elif (Name == 'Sapium insigne'):
            sap_in_d = np.random.choice(np.random.uniform(high = 15.04589809, low = 5.642211783, size = (1,)))
            return sap_in_d
        elif (Name == 'Symplocus lucida'):
            symp_luc_d = np.random.choice(np.random.uniform(high = 28.71258885, low = 4.2519708, size = (14,)))
            return symp_luc_d
        elif (Name == 'Toona ciliata'):
            toon_d = np.random.choice(np.random.uniform(high = 26.33032166, low = 4.01181319, size = (8,)))
            return toon_d
        else:
            return 1
df1['Diam'] = df1['Name'].apply(reclass)
df1.to_excel('to_edit.xlsx', index = False)
