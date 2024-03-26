# TFE: Optimization of Energy Systems with Carbon Capture and Storage to Reach a Carbon- Free Energy System in Belgium
GBOML and python codes

# Installation
First you need to prepare your python environment with:   

`pip install -r requirements.txt`

In particular, the basic numpy and matplotlibs libraries are used, in addition to GBOML, where the documentation   
and installation can be found here https://gboml.readthedocs.io/en/latest/


# How to run simulation and save results 

To run the simulation with the desired parameters and save the results:

`python3 main.py $config $scenario`

where you choose between 3 configs and 3 scenarios:   
`$config \in {1, 2, 3}`   
`$scenario \in {reference, optimistic, conservative}`   

The default case is config 1 with reference scenario

# How to run analysis and save plots






