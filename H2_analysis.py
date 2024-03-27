from gboml import *
import json
import matplotlib.pyplot as plt
import numpy as np
import gboml.compiler.classes as gcc
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('--config', help='Config',
                        type=int, default=1, choices=[1,2,3])

parser.add_argument('--scenario', help='Scenario', 
                        type=str, default="reference", choices=['reference','optimistic','conservative'])

args = parser.parse_args()
config = args.config 
scenario = args.scenario

if not os.path.exists("images"):
        os.makedirs("images")

if not os.path.exists("H2_results"):
        os.makedirs("H2_results")


years = 5
Efficiency = np.arange(50, 85, 1) #define the range of efficiencies to analyse


for i in range(len(Efficiency)):
   
    conversion_factor_hydrogen_electrolysis = float(100*33/Efficiency[i])
    gboml_model = GbomlGraph(8760*years)
    nodes, edges, global_params = gboml_model.import_all_nodes_and_edges("H2_analysis.gboml")


    if scenario == "optimistic":
        facteur = 0.8
    elif scenario == "reference":
        facteur = 1
    elif scenario == "conservative":
        facteur = 1.2
    else:
        print("Choose an appropriate scenario")



    if config == 1:
        conversion_factor_hydrogen = 0.547
        conversion_factor_carbon_dioxide = 4.16
        conversion_factor_water = 3.3

    elif config == 2:
        conversion_factor_hydrogen = 0.53
        conversion_factor_carbon_dioxide = 3.04
        conversion_factor_water = 3.46

    elif config == 3:
        conversion_factor_hydrogen = 5.19
        conversion_factor_carbon_dioxide = 3.417
        conversion_factor_water = 3.21

    else:
        print("Choose an appropriate config")
        
    global_params = list(filter(lambda x: x.name != "conversion_factor_hydrogen_electrolysis", global_params))
    global_params.append(gcc.Parameter("conversion_factor_hydrogen_electrolysis", 
                                gcc.Expression("literal", conversion_factor_hydrogen_electrolysis)))

    global_params = list(filter(lambda x: x.name != "facteur", global_params))
    global_params.append(gcc.Parameter("facteur", 
                                gcc.Expression("literal", facteur)))    

    global_params = list(filter(lambda x: x.name != "conversion_factor_hydrogen", global_params))
    global_params.append(gcc.Parameter("conversion_factor_hydrogen", 
                                gcc.Expression("literal", conversion_factor_hydrogen)))

    global_params = list(filter(lambda x: x.name != "conversion_factor_carbon_dioxide", global_params))
    global_params.append(gcc.Parameter("conversion_factor_carbon_dioxide", 
                                gcc.Expression("literal", conversion_factor_carbon_dioxide)))

    global_params = list(filter(lambda x: x.name != "conversion_factor_water", global_params))
    global_params.append(gcc.Parameter("conversion_factor_water", 
                                gcc.Expression("literal", conversion_factor_water)))


    gboml_model.add_nodes_in_model(*nodes)
    gboml_model.add_hyperedges_in_model(*edges)
    gboml_model.add_global_parameters(global_params)
    gboml_model.build_model()
    solution = gboml_model.solve_gurobi()
    
    solution, objective, status, solver_info, constraints_information, variables_information = solution
    dico = gboml_model.turn_solution_to_dictionary(solver_info, status, solution, objective, constraints_information, variables_information)

    with open("results_H2/config" + str(config) + "_"+ str(scenario) + "_"+ str(Efficiency[i]) + ".json", "w") as json_file:
        json_obj = json.dumps(dico)
        # Writing to sample.json
        json_file.write(json_obj)
    

class MakeMeReadable:
    def __init__(self, d):
        self.d = d
   
    def __dir__(self):
        return self.d.keys()
   
    def __getattr__(self, v):
        try:
            out = self.d[v]
            if isinstance(out, dict):
                return MakeMeReadable(out)
            return out
        except:
            return getattr(self.d, v)
       
    def __str__(self):
        return str(self.d)
   
    def __repr__(self):
        return repr(self.d)

    
cost = np.zeros(len(Efficiency))

for i in range(len(Efficiency)):
    filename = "results_H2/config" + str(config) + "_"+ str(scenario) + "_"+ str(Efficiency[i]) + ".json"
    dico = {}
    with open(filename, "r") as fp:
        dico = json.load(fp)
        
    d = MakeMeReadable(dico)
    y = np.array([np.sum([d.solution.elements.BATTERY_STORAGE.objectives.unnamed[0],d.solution.elements.BATTERY_STORAGE.objectives.unnamed[1]]), np.sum([d.solution.elements.WIND_PLANTS.objectives.unnamed[0], d.solution.elements.WIND_PLANTS.objectives.unnamed[1]]), np.sum([d.solution.elements.HVDC.objectives.unnamed[0],d.solution.elements.HVDC.objectives.unnamed[1]]), d.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[0], d.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[0], d.solution.elements.FT_PROCESS.objectives.unnamed[0], np.sum([d.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[0], d.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[1]]), d.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[0],  d.solution.elements.REFINERY.objectives.unnamed[0], np.add(d.solution.elements.PETROL_STORAGE_HUB.objectives.unnamed[0],d.solution.elements.PETROL_STORAGE_DESTINATION.objectives.unnamed[0]), np.sum([d.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0],d.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0]]), d.solution.elements.PETROL_CARRIERS.objectives.unnamed[0]])/(647.6268*years)
    cost[i] = sum(y)
    

plt.plot(Efficiency, cost)
plt.fill_between(Efficiency, min(cost), max(cost), where=(Efficiency < 70), color='lightblue', alpha=0.5, label = 'PEM')
plt.fill_between(Efficiency, min(cost), max(cost), where=(Efficiency >= 70), color='lightcoral', alpha=0.5, label = 'SOEC')

plt.xlabel("Electrolysis Efficiency [%]")
plt.ylabel("FT-Products Cost [€/kg]")
plt.legend(loc = (0.765,0.8))
plt.show()