
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")


# # 0. General note

# * This notebook produces figures and calculations presented in [Ye et al. 2017, JGR](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2016JB013811).
# 
# * This notebook demonstrates how to correct pressure scales for the existing phase boundary data.

# # 1. Global setup

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy as unp
import pytheos as eos


# # 2. Pressure calculations for PPv

# * Data from Tateno2009
# 
# T (K) | Au-Tsuchiya | Pt-Holmes | MgO-Speziale
# ------|-------------|-----------|--------------
# 3500  | 120.4       | 137.7     | 135.6
# 2000  | 110.5       | 126.8     | 115.8
# 
# * Dorogokupets2007
# 
# T (K) | Au          | Pt        | MgO   
# ------|-------------|-----------|--------------
# 3500  | 119.7       | 135.2     | 129.6
# 2000  | 108.9       | 123.2     | 113.2
# 
# <b>
# * In conclusion, PPV boundary discrepancy is not likely due to pressure scale problem.
# </b>

# In[3]:


t_ppv = np.asarray([3500., 2000.])


# In[4]:


Au_T = eos.gold.Tsuchiya2003()
Au_D = eos.gold.Dorogokupets2007()

v = np.asarray([51.58,51.7])
p_Au_T_ppv = Au_T.cal_p(v, t_ppv)
p_Au_D_ppv = Au_D.cal_p(v, t_ppv)
print(p_Au_T_ppv, p_Au_D_ppv)
print('slopes: ', (p_Au_T_ppv[0]-p_Au_T_ppv[1])/(t_ppv[0]-t_ppv[1]),      (p_Au_D_ppv[0]-p_Au_D_ppv[1])/(t_ppv[0]-t_ppv[1]) )


# In[5]:


Pt_H = eos.platinum.Holmes1989()
Pt_D = eos.platinum.Dorogokupets2007()

v = np.asarray([48.06, 48.09])
p_Pt_H_ppv = Pt_H.cal_p(v, t_ppv)
p_Pt_D_ppv = Pt_D.cal_p(v, t_ppv)
print(p_Pt_H_ppv, p_Pt_D_ppv)
print('slopes: ', (p_Pt_H_ppv[0]-p_Pt_H_ppv[1])/(t_ppv[0]-t_ppv[1]),      (p_Pt_D_ppv[0]-p_Pt_D_ppv[1])/(t_ppv[0]-t_ppv[1]) )


# In[6]:


MgO_S = eos.periclase.Speziale2001()
MgO_D = eos.periclase.Dorogokupets2007()

v = np.asarray([52.87, 53.6])
p_MgO_S_ppv = MgO_S.cal_p(v, t_ppv)
p_MgO_D_ppv = MgO_D.cal_p(v, t_ppv)
print(p_MgO_S_ppv, p_MgO_D_ppv)
print('slopes: ', (p_MgO_S_ppv[0]-p_MgO_S_ppv[1])/(t_ppv[0]-t_ppv[1]),       (p_MgO_D_ppv[0]-p_MgO_D_ppv[1])/(t_ppv[0]-t_ppv[1]) )


# # 3. Post-spinel

# Fei2004
# 
# Scales|  PT        |  PT 
# ------|------------|------------
# MgO-S | 23.6, 1573 | 22.8, 2173
# MgO-D | 23.1, 1573 | 22.0, 2173
# 
# Ye2014
# 
# Scales | PT         | PT
# -------|------------|------------
# Pt-F   | 25.2, 1550 | 23.2, 2380
# Pt-D   | 24.6, 1550 | 22.5, 2380 
# Au-F   | 28.3, 1650 | 27.1, 2150
# Au-D   | 27.0, 1650 | 25.6, 2150

# In[7]:


MgO_S = eos.periclase.Speziale2001()
MgO_D = eos.periclase.Dorogokupets2007()

v = np.asarray([68.75, 70.3])
t_MgO = np.asarray([1573.,2173.])
p_MgO_S = MgO_S.cal_p(v, t_MgO)
p_MgO_D = MgO_D.cal_p(v, t_MgO)
print(p_MgO_S, p_MgO_D)
print('slopes: ', (p_MgO_S[0]-p_MgO_S[1])/(t_MgO[0]-t_MgO[1]), (p_MgO_D[0]-p_MgO_D[1])/(t_MgO[0]-t_MgO[1]) )


# In[8]:


Pt_F = eos.platinum.Fei2007bm3()
Pt_D = eos.platinum.Dorogokupets2007()

v = np.asarray([57.43, 58.85])
t_Pt = np.asarray([1550., 2380.])
p_Pt_F = Pt_F.cal_p(v, t_Pt)
p_Pt_D = Pt_D.cal_p(v, t_Pt)
print(p_Pt_F, p_Pt_D)
print('slopes: ', (p_Pt_F[0]-p_Pt_F[1])/(t_Pt[0]-t_Pt[1]), (p_Pt_D[0]-p_Pt_D[1])/(t_Pt[0]-t_Pt[1]) )


# In[9]:


Au_F = eos.gold.Fei2007bm3()
Au_D = eos.gold.Dorogokupets2007()

v = np.asarray([62.33,63.53])
t_Au = np.asarray([1650., 2150.])
p_Au_F = Au_F.cal_p(v, t_Au)
p_Au_D = Au_D.cal_p(v, t_Au)
print(p_Au_F, p_Au_D)
print('slopes: ', (p_Au_F[0]-p_Au_F[1])/(t_Au[0]-t_Au[1]), (p_Au_D[0]-p_Au_D[1])/(t_Au[0]-t_Au[1]) )


# In[10]:


f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,3.5))
#ax.plot(unp.nominal_values(p_Au_T), t, c='b', ls='--', label='Au-Tsuchiya')
lw = 4
l_alpha = 0.3

ax1.plot(unp.nominal_values(p_Au_D), t_Au, c='b', ls='-', alpha=l_alpha, label='Au-D07', lw=lw)
ax1.annotate('Au-D07', xy=(25.7, 2100), xycoords='data',
            xytext=(26.9, 2100), textcoords='data',
            arrowprops=dict(facecolor='k', alpha=0.5, shrink=1, width = 0.1, headwidth=5),
            horizontalalignment='right', verticalalignment='center')

ax1.plot(unp.nominal_values(p_Au_D-2.5), t_Au, c='b', ls='-', label='Au-mD07', lw=lw)
ax1.annotate('Au-D07,\n corrected', xy=(24.35, 1700), xycoords='data',
            xytext=(24.8, 1700), textcoords='data',
            arrowprops=dict(facecolor='k', alpha=0.5, shrink=1, width = 0.1, headwidth=5),
            horizontalalignment='left', verticalalignment='center')

#ax.plot(unp.nominal_values(p_Pt_H), t, c='r', ls='--', label='Pt-Holmes')
ax1.plot(unp.nominal_values(p_Pt_D), t_Pt, c='r', ls='-', label='Pt-D07', lw=lw)
ax1.annotate('Pt-D07', xy=(22.7, 2300), xycoords='data',
            xytext=(23.1, 2300), textcoords='data',
            arrowprops=dict(facecolor='k', alpha=0.5, shrink=1, width = 0.1, headwidth=5),
            horizontalalignment='left', verticalalignment='center')

ax1.plot(unp.nominal_values(p_MgO_S), t_MgO, c='k', ls='-', alpha=l_alpha, label='MgO-S01', lw=lw)
ax1.annotate('MgO-S01', xy=(22.9, 2150), xycoords='data',
            xytext=(22.5, 2250), textcoords='data',
            arrowprops=dict(facecolor='k', alpha=0.5, shrink=1, width = 0.1, headwidth=5),
            horizontalalignment='right', verticalalignment='top')

ax1.plot(unp.nominal_values(p_MgO_D), t_MgO, c='k', ls='-', label='MgO-D07', lw=lw)
ax1.annotate('MgO-D07', xy=(22.7, 1800), xycoords='data',
            xytext=(22.3, 1800), textcoords='data',
            arrowprops=dict(facecolor='k', alpha=0.5, shrink=1, width = 0.1, headwidth=5),
            horizontalalignment='right', verticalalignment='center')

ax1.fill([23.5,24,24,23.5], [1700,1700,2000,2000], 'k', alpha=0.2)

ax1.set_xlabel("Pressure (GPa)"); ax1.set_ylabel("Temperature (K)")
#l = ax1.legend(loc=3, fontsize=10, handlelength=2.5); l.get_frame().set_linewidth(0.5)

ax2.plot(unp.nominal_values(p_Au_T_ppv), t_ppv, c='b', ls='-', alpha=l_alpha, label='Au-T04', lw=lw)
ax2.annotate('Au-T04', xy=(120, 3400), xycoords='data',
            xytext=(122, 3400), textcoords='data',
            arrowprops=dict(facecolor='k', alpha=0.5, shrink=1, width = 0.1, headwidth=5),
            horizontalalignment='left', verticalalignment='center')

ax2.plot(unp.nominal_values(p_Au_D_ppv), t_ppv, c='b', ls='-', label='Au-D07', lw=lw)
ax2.annotate('Au-D07', xy=(119, 3400), xycoords='data',
            xytext=(117, 3400), textcoords='data',
            arrowprops=dict(facecolor='k', alpha=0.5, shrink=1, width = 0.1, headwidth=5),
            horizontalalignment='right', verticalalignment='center')

ax2.plot(unp.nominal_values(p_Pt_H_ppv), t_ppv, c='r', ls='-', alpha=l_alpha, label='Pt-H89', lw=lw)
ax2.annotate('Pt-H89', xy=(129, 2300), xycoords='data',
            xytext=(132, 2300), textcoords='data',
            arrowprops=dict(facecolor='k', alpha=0.5, shrink=1, width = 0.1, headwidth=5),
            horizontalalignment='left', verticalalignment='center')

ax2.plot(unp.nominal_values(p_Pt_D_ppv), t_ppv, c='r', ls='-', label='Pt-D07', lw=lw)
ax2.annotate('Pt-D07', xy=(124, 2150), xycoords='data',
            xytext=(123.7, 2300), textcoords='data',
            arrowprops=dict(facecolor='k', alpha=0.5, shrink=1, width = 0.1, headwidth=5),
            horizontalalignment='center', verticalalignment='bottom')

ax2.plot(unp.nominal_values(p_MgO_S_ppv), t_ppv, c='k', ls='-', alpha=l_alpha, label='MgO-S01', lw=lw)
ax2.annotate('MgO-S01', xy=(132, 3250), xycoords='data',
            xytext=(132.2, 3550), textcoords='data',
            arrowprops=dict(facecolor='k', alpha=0.5, shrink=1, width = 0.1, headwidth=5),
            horizontalalignment='left', verticalalignment='bottom')

ax2.plot(unp.nominal_values(p_MgO_D_ppv), t_ppv, c='k', ls='-', label='MgO-D07', lw=lw)
ax2.annotate('MgO-D07', xy=(128, 3400), xycoords='data',
            xytext=(128, 3550), textcoords='data',
            arrowprops=dict(facecolor='k', alpha=0.5, shrink=1, width = 0.1, headwidth=5),
            horizontalalignment='center', verticalalignment='bottom')

ax2.set_xlabel("Pressure (GPa)"); ax2.set_ylabel("Temperature (K)")
ax2.set_ylim(1900, 3700.)
#l = ax2.legend(loc=0, fontsize=10, handlelength=2.5); l.get_frame().set_linewidth(0.5)

ax1.text(0.05, 0.03, 'a', horizontalalignment='center',            verticalalignment='bottom', transform = ax1.transAxes,              fontsize = 32)
ax2.text(0.05, 0.03, 'b', horizontalalignment='center',            verticalalignment='bottom', transform = ax2.transAxes,              fontsize = 32)

ax1.set_yticks(ax1.get_yticks()[::2])
#ax2.set_yticks(ax2.get_yticks()[::2])
plt.tight_layout(pad=0.6)

plt.savefig('f-boundaries.pdf', bbox_inches='tight',                         pad_inches=0.1)

