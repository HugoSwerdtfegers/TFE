# TFE: Optimization of Energy Systems with Carbon Capture and Storage to Reach a Carbon- Free Energy System in Belgium

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

To obtain cost breakdown graphs as well as capacity comparison 

`python3 analysis.py $scenario`

where you choose between 3 scenarios

`$scenario \in {reference, optimistic, conservative}`  

The graphs will necessarily be produced for each configuration, so the 3 simulation files must have been generated beforehand.

The default case is the reference scenario

# How to run electrolyser analysis 

To run the simulations and obtain a graph showing the impact of the efficiency of the electrolyser  

`python3 H2_analysis.py $config $scenario`   

where you choose between 3 configs and 3 scenarios:   

`$config \in {1, 2, 3}`   
`$scenario \in {reference, optimistic, conservative}`  

(WARNING! : Simulation can take several hours)

The default case is config 1 with reference scenario





