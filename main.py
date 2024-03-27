from gboml import *
import json
import matplotlib.pyplot as plt
import numpy as np
import gboml.compiler.classes as gcc
import argparse
import os


parser = argparse.ArgumentParser()

parser.add_argument('-conf', '--config', help='Config',
                        type=int, default=1, choices=[1,2,3])

parser.add_argument('-sc', '--scenario', help='Scenario', 
                        type=str, default="reference", choices=['reference','optimistic','conservative'])

args = parser.parse_args()
config = args.config 
scenario = args.scenario


years = 5
gboml_model = GbomlGraph(8760*years)
nodes, edges, global_params = gboml_model.import_all_nodes_and_edges("FT_Products.gboml")


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
print("Solved")


if not os.path.exists("results"):
        os.makedirs("results")


solution, objective, status, solver_info, constraints_information, variables_information = solution
dico = gboml_model.turn_solution_to_dictionary(solver_info, status, solution, objective, constraints_information, variables_information)

with open("results/config" + str(config) + "_"+ str(scenario) + ".json", "w") as json_file:
    json_obj = json.dumps(dico)
    json_file.write(json_obj)

print("Json done")