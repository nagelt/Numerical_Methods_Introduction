# %%
import numpy as np
import math
import pandas as pd

# You could use following function to add geological layers to the plot
from functions import add_MT_DB_geoboundaries_yaxis

# %% [markdown]
# In following cell you will find boundary condtions needed for the analytical solution.

# %%
gamma_w = 1e3 * 9.81  # kN/m³
Tbot = 32.08  # °C
ptop = 0.562e6
pbot = 2.463e6  # Pa
hbot = 530.0
dT_dz = -0.08  # K/m, Mont Terri
dp = (pbot - ptop) - gamma_w * (301 / math.sqrt(2))

# %%
# Values from Goncalves 2023. All arrays from Staffelegg to Passwang, after flipping
k = np.array([9.80e-18, 7.80e-20, 9.06e-21, 3.74e-21, 4.76e-20, 3.74e-21,
       1.00e-19, 1.00e-10])  # m²
eT = np.array([14.67889908, 16.30988787,  5.60652396, 27.52293578, 11.00917431, 13.76146789, 0., 0.]) # Pa/K
dz = np.array([64, 47, 4, 12, 36, 32, 69, 37]) # m thickness of layers
dh = -dp / gamma_w  # m
Tz = Tbot + (dz.cumsum()) * dT_dz
kT = eT * k / 0.001016
kf = k / 0.001016 * gamma_w  # has to be in m/s
eT /= gamma_w  # conversion to m/K


# %% [markdown]
# In following cells, implement analytical solution discussed during today's lecture.

# %%

# %%

# %%

# %%

# %% [markdown]
# In following cells, compare analytical solution with observation data.

# %%
# Read reference data
temperature_reference = pd.read_csv("Observation_data/temperature.csv")
t_ref_t = temperature_reference["Temp"].to_numpy()
t_ref_z = temperature_reference["Depth"].to_numpy()

pressure_reference = pd.read_csv("Observation_data/pressure.csv")
p_ref_p = pressure_reference["X"].to_numpy()
p_ref_z = pressure_reference["Y_corr"].to_numpy()

# %%

# %%

# %%

# %%


# %% [markdown]
# You could also try to compare variants with constant values for kT and kf with those including temperature dependent viscosity.

# %%
mu = lambda T: 1.856e-14 * np.exp(4209/T + 0.04527 * T - 3.376e-5 *T*T)
kT = eT * k / mu(Tz + 273.15)
kf = k / mu(Tz + 273.15) * gamma_w

