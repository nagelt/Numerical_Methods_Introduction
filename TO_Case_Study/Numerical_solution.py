# %%
import ogstools as ot
import matplotlib.pyplot as plt

# %% [markdown]
# Your first task will be to add correct boundary condtions into  prj file in folder "Numerical solution": MT_DB.prj.

# %% [markdown]
# Now that project file is ready, numerical simulation can be run:

# %%
# Load project file
MT_DB = ot.Project(input_file="Numerical_solution/MT_DB.prj",
                   output_file="Numerical_solution/MT_DB.prj")

# %%
# Run simulation
MT_DB.run_model(args=f"-m Numerical_solution/Mesh/ -o output/")

# %%
# Load results
MT_DB_results = ot.MeshSeries("output/run_0.pvd")

# %% [markdown]
# In this part, you can compare analytical solution, numerical model and observation data. 

# %%
# You can obtain a vertical profile over simulation domain
MT_DB_TO_sample = MT_DB_results[-1].sample_over_line([5, 0, 0], [5, -301, 0])

# %% [markdown]
# Some plotting functions in OGSTools can make use of presets for variables.
# The preset for pressure can be accessed like this: ot.variables.pressure
# For more help and information you can visit: https://ogstools.opengeosys.org/
