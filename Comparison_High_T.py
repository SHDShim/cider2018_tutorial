
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")


# # 0. General note

# * This notebook produces figures and calculations presented in [Ye et al. 2017, JGR](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2016JB013811).
# 
# * This notebook compared widely used Pt, Au, and MgO pressure scales at high temperatures relevant for the lower mantle.

# # 1. Global setup

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from uncertainties import unumpy as unp
import pytheos as eos


# # 2. Data Input

# Notations for datasets.
# 
# * PM = Pt-MgO
# * AM = Au-MgO

# ## 2.1. Reading Pt-MgO (PM) and Au-MgO (AM) at High T

# In[7]:


data_PM = pd.read_csv('./data/Pt_MgO_HiT.csv')
data_AM = pd.read_csv('./data/Au_MgO_HiT.csv')


# In[8]:


data_PMN_300.tail()


# In[9]:


data_AMN_300.tail()


# In[10]:


v_Pt_PM    = data_PM['V(Pt)'] 
s_v_Pt_PM  = data_PM['sV(Pt)']
v_MgO_PM   = data_PM['V(MgO)'] 
s_v_MgO_PM = data_PM['sV(MgO)']
T_PM    = data_PM['T'] 
s_T_PM  = data_PM['sT']

v_Au_AM    = data_AM['V(Au)'] 
s_v_Au_AM  = data_AM['sV(Au)']
v_MgO_AM   = data_AM['V(MgO)'] 
s_v_MgO_AM = data_AM['sV(MgO)']
T_AM    = data_AM['T'] 
s_T_AM  = data_AM['sT']


# ## 2.2. Define Pt, Au, and MgO scales

# In[11]:


std_MgO =[ eos.periclase.Speziale2001(), eos.periclase.Dorogokupets2007(),              eos.periclase.Tange2009(), eos.periclase.Dorogokupets2015()]
std_Au =[ eos.gold.Fei2007bm3(), eos.gold.Dorogokupets2007(),              eos.gold.Yokoo2009(), eos.gold.Dorogokupets2015()]
std_Pt =[ eos.platinum.Fei2007bm3(), eos.platinum.Dorogokupets2007(),              eos.platinum.Yokoo2009(), eos.platinum.Dorogokupets2015()]


# # 3. Comparing scales

# In[12]:


p_MgO_PM = []; p_MgO_AM = []; p_Pt_PM = []; p_Au_AM = [] 
for i in range(4):
    p_MgO_PM_t = std_MgO[i].cal_p(unp.uarray(v_MgO_PM,s_v_MgO_PM), unp.uarray(T_PM, s_T_PM))
    p_MgO_AM_t = std_MgO[i].cal_p(unp.uarray(v_MgO_AM,s_v_MgO_AM), unp.uarray(T_AM, s_T_AM))
    p_Pt_PM_t = std_Pt[i].cal_p(unp.uarray(v_Pt_PM,s_v_Pt_PM), unp.uarray(T_PM, s_T_PM))
    p_Au_AM_t = std_Au[i].cal_p(unp.uarray(v_Au_AM,s_v_Au_AM), unp.uarray(T_AM, s_T_AM))
    p_MgO_PM.append(p_MgO_PM_t)
    p_MgO_AM.append(p_MgO_AM_t)
    p_Pt_PM.append(p_Pt_PM_t)
    p_Au_AM.append(p_Au_AM_t)


# In[13]:


f, axarr = plt.subplots(2, 2,                     figsize=(8,6))
ax = [axarr[0,0], axarr[0,1], axarr[1,0], axarr[1,1]]
ms = 8; mew = 0.7
label = ['a', 'b', 'c', 'd']

for i in range(4):
    ax[i].axhline(y=0, c='k', ls=':')
    ax[i].errorbar(unp.nominal_values(p_MgO_AM[i]),             unp.nominal_values(p_Au_AM[i]) - unp.nominal_values(p_MgO_AM[i]),             yerr = unp.std_devs(p_Au_AM[i]),             fmt='bo', mec='w', mew=mew, label = 'Au',             ms=ms, capsize=0, lw=0.4)
    ax[i].errorbar(unp.nominal_values(p_MgO_PM[i]),             unp.nominal_values(p_Pt_PM[i]) - unp.nominal_values(p_MgO_PM[i]),             yerr = unp.std_devs(p_Pt_PM[i]),             fmt='ro', mec='w', mew=mew, label="Pt",             ms=ms, capsize=0, lw=0.4)
    ax[i].set_xlabel('P(MgO) (GPa)'); ax[i].set_ylabel('$\mathdefault{{\Delta} P}$ (GPa)')
    l = ax[i].legend(loc=3, numpoints = 1, fontsize = 10)
    l.get_frame().set_linewidth(0.5)
    plt.tight_layout(pad=0.4)
    ax[i].set_ylim(-8.,4.); ax[i].set_xlim(0.,160.)
    ax[i].set_xticks(ax[i].get_xticks()[::2])
    ax[i].text(0.08, 0.83,label[i], horizontalalignment='center',            verticalalignment='bottom', transform = ax[i].transAxes,              fontsize = 24)

plt.savefig('f-Compare-HighT.pdf', bbox_inches='tight',                         pad_inches=0.1)


# * A 3 GPa difference at 24 GPa is clearly visible between Au and Pt throughout the comparisons.
# * MgO scale is severe need for improvements in any cases.
