from gboml import *
import json
import matplotlib.pyplot as plt
import numpy as np
import gboml.compiler.classes as gcc
import argparse
import os


if not os.path.exists("images"):
        os.makedirs("images")


parser = argparse.ArgumentParser()



parser.add_argument('--scenario', help='Scenario', 
                        type=str, default="reference", choices=['reference','optimistic','conservative'])


args = parser.parse_args()

scenario = args.scenario



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


filename = "results/config1_"+ str(scenario) + ".json"
dico = {}
with open(filename, "r") as fp:
    dico = json.load(fp)
   
d = MakeMeReadable(dico)



years = 5
x = ['Battery Storage', 'Wind Turbines', 'HVDC', 'Hydrogen storage', 'Electrolysis', 'FT Process', 'Direct Air Capture', 'Solar PV', 'Refinery', 'Petrol Storage', 'Water Desalination', 'Petrol Carriers']
y = np.array([np.sum([d.solution.elements.BATTERY_STORAGE.objectives.unnamed[0],d.solution.elements.BATTERY_STORAGE.objectives.unnamed[1]]), np.sum([d.solution.elements.WIND_PLANTS.objectives.unnamed[0], d.solution.elements.WIND_PLANTS.objectives.unnamed[1]]), np.sum([d.solution.elements.HVDC.objectives.unnamed[0],d.solution.elements.HVDC.objectives.unnamed[1]]), d.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[0], d.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[0], d.solution.elements.FT_PROCESS.objectives.unnamed[0], np.sum([d.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[0], d.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[1]]), d.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[0],  d.solution.elements.REFINERY.objectives.unnamed[0], np.add(d.solution.elements.PETROL_STORAGE_HUB.objectives.unnamed[0],d.solution.elements.PETROL_STORAGE_DESTINATION.objectives.unnamed[0]), np.sum([d.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0],d.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0]]), d.solution.elements.PETROL_CARRIERS.objectives.unnamed[0]])/(647.6268*years)

sorted_indices = np.argsort(y)
sorted_x = [x[i] for i in sorted_indices]
sorted_y = y[sorted_indices]
sorted_y_rounded = np.round(sorted_y, 2)

colors = ['#F9E79F', '#F9E79F', '#F9E79F', '#ADE2F0', '#ADE2F0', '#D68B11', '#ABE78C', '#F9E79F', '#D68B11', '#D68B11', '#588AD3', '#D68B11']

plt.figure(figsize=(10,7))
bars = plt.barh(sorted_x, sorted_y_rounded.flatten(), height=0.6, color=[colors[i] for i in sorted_indices])
plt.xlabel('€/MWh')
plt.title(f'Synthetic FT-Products Cost Breakdown for config 1 (€/MWh) - Total Cost: {np.sum(sorted_y_rounded):.2f} €/kg')

for i, bar in enumerate(bars):
    plt.text(bar.get_width(), i, str(bar.get_width()))

plt.savefig("images/cost_breakdown_config1_"+ str(scenario) + ".png", dpi=150, bbox_inches='tight')

filename = "results/config2_"+ str(scenario) + ".json"
dico = {}
with open(filename, "r") as fp:
    dico = json.load(fp)
   
e = MakeMeReadable(dico)


years = 5
x = ['Battery Storage', 'Wind Turbines', 'HVDC', 'Hydrogen storage', 'Electrolysis', 'FT Process', 'Direct Air Capture', 'Solar PV', 'Refinery', 'Petrol Storage', 'Water Desalination', 'Petrol Carriers']
y = np.array([np.sum([e.solution.elements.BATTERY_STORAGE.objectives.unnamed[0],e.solution.elements.BATTERY_STORAGE.objectives.unnamed[1]]), np.sum([e.solution.elements.WIND_PLANTS.objectives.unnamed[0], e.solution.elements.WIND_PLANTS.objectives.unnamed[1]]), np.sum([e.solution.elements.HVDC.objectives.unnamed[0],e.solution.elements.HVDC.objectives.unnamed[1]]), e.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[0], e.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[0], e.solution.elements.FT_PROCESS.objectives.unnamed[0], np.sum([e.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[0], e.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[1]]), e.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[0],  e.solution.elements.REFINERY.objectives.unnamed[0], np.add(e.solution.elements.PETROL_STORAGE_HUB.objectives.unnamed[0],e.solution.elements.PETROL_STORAGE_DESTINATION.objectives.unnamed[0]), np.sum([e.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0],e.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0]]), e.solution.elements.PETROL_CARRIERS.objectives.unnamed[0]])/(647.6268*years)

sorted_indices = np.argsort(y)
sorted_x = [x[i] for i in sorted_indices]
sorted_y = y[sorted_indices]
sorted_y_rounded = np.round(sorted_y, 2)

colors = ['#F9E79F', '#F9E79F', '#F9E79F', '#ADE2F0', '#ADE2F0', '#D68B11', '#ABE78C', '#F9E79F', '#D68B11', '#D68B11', '#588AD3', '#D68B11']

plt.figure(figsize=(10,7))
bars = plt.barh(sorted_x, sorted_y_rounded.flatten(), height=0.6, color=[colors[i] for i in sorted_indices])
plt.xlabel('€/MWh')
plt.title(f'Synthetic FT-Products Cost Breakdown for config 2 (€/MWh) - Total Cost: {np.sum(sorted_y_rounded):.2f} €/kg')

for i, bar in enumerate(bars):
    plt.text(bar.get_width(), i, str(bar.get_width()))

plt.savefig("images/cost_breakdown_config2_"+ str(scenario) + ".png", dpi=150, bbox_inches='tight')

filename = "results/config3_"+ str(scenario) + ".json"
dico = {}
with open(filename, "r") as fp:
    dico = json.load(fp)
   
f = MakeMeReadable(dico)



years = 5
x = ['Battery Storage', 'Wind Turbines', 'HVDC', 'Hydrogen storage', 'Electrolysis', 'FT Process', 'Direct Air Capture', 'Solar PV', 'Refinery', 'Petrol Storage', 'Water Desalination', 'Petrol Carriers']
y = np.array([np.sum([f.solution.elements.BATTERY_STORAGE.objectives.unnamed[0],f.solution.elements.BATTERY_STORAGE.objectives.unnamed[1]]), np.sum([f.solution.elements.WIND_PLANTS.objectives.unnamed[0], f.solution.elements.WIND_PLANTS.objectives.unnamed[1]]), np.sum([f.solution.elements.HVDC.objectives.unnamed[0],f.solution.elements.HVDC.objectives.unnamed[1]]), f.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[0], f.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[0], f.solution.elements.FT_PROCESS.objectives.unnamed[0], np.sum([f.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[0], f.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[1]]), f.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[0],  f.solution.elements.REFINERY.objectives.unnamed[0], np.add(f.solution.elements.PETROL_STORAGE_HUB.objectives.unnamed[0],f.solution.elements.PETROL_STORAGE_DESTINATION.objectives.unnamed[0]), np.sum([f.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0],f.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0]]), f.solution.elements.PETROL_CARRIERS.objectives.unnamed[0]])/(647.6268*years)

sorted_indices = np.argsort(y)
sorted_x = [x[i] for i in sorted_indices]
sorted_y = y[sorted_indices]
sorted_y_rounded = np.round(sorted_y, 2)

colors = ['#F9E79F', '#F9E79F', '#F9E79F', '#ADE2F0', '#ADE2F0', '#D68B11', '#ABE78C', '#F9E79F', '#D68B11', '#D68B11', '#588AD3', '#D68B11']

plt.figure(figsize=(10,7))
bars = plt.barh(sorted_x, sorted_y_rounded.flatten(), height=0.6, color=[colors[i] for i in sorted_indices])
plt.xlabel('€/MWh')
plt.title(f'Synthetic FT-Products Cost Breakdown for config 3(€/MWh) - Total Cost: {np.sum(sorted_y_rounded):.2f} €/kg')

for i, bar in enumerate(bars):
    plt.text(bar.get_width(), i, str(bar.get_width()))

plt.savefig("images/cost_breakdown_config3_"+ str(scenario) + ".png", dpi=150, bbox_inches='tight')



scenarios = ['Config 1', 'Config 2', 'Config 3']
x = ['[GWh] Batteries', '[GW] Solar PV', '[GW] Wind turbines', '[TWh] Hydrogen', '[GW_el] Electrolysis', '[GW_th] FT Process', '[Mt/y] DAC', '[kt/h] Desalination' ]
y_scenario_1 = np.array([d.solution.elements.BATTERY_STORAGE.variables.capacity_stock.values, d.solution.elements.SOLAR_PV_PLANTS.variables.capacity.values, d.solution.elements.WIND_PLANTS.variables.capacity.values,np.divide(d.solution.elements.HYDROGEN_STORAGE.variables.capacity_stock.values,1/0.04), d.solution.elements.ELECTROLYSIS_PLANTS.variables.capacity.values , np.divide(d.solution.elements.FT_PROCESS.variables.capacity.values, 1/16), np.divide(d.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.variables.capacity.values, 1/8.76), d.solution.elements.DESALINATION_PLANTS.variables.capacity.values])
y_scenario_2 = np.array([e.solution.elements.BATTERY_STORAGE.variables.capacity_stock.values, e.solution.elements.SOLAR_PV_PLANTS.variables.capacity.values, e.solution.elements.WIND_PLANTS.variables.capacity.values,np.divide(e.solution.elements.HYDROGEN_STORAGE.variables.capacity_stock.values,1/0.04), e.solution.elements.ELECTROLYSIS_PLANTS.variables.capacity.values , np.divide(e.solution.elements.FT_PROCESS.variables.capacity.values, 1/16), np.divide(e.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.variables.capacity.values, 1/8.76), e.solution.elements.DESALINATION_PLANTS.variables.capacity.values])
y_scenario_3 = np.array([f.solution.elements.BATTERY_STORAGE.variables.capacity_stock.values, f.solution.elements.SOLAR_PV_PLANTS.variables.capacity.values, f.solution.elements.WIND_PLANTS.variables.capacity.values,np.divide(f.solution.elements.HYDROGEN_STORAGE.variables.capacity_stock.values,1/0.04), f.solution.elements.ELECTROLYSIS_PLANTS.variables.capacity.values , np.divide(f.solution.elements.FT_PROCESS.variables.capacity.values, 1/16), np.divide(f.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.variables.capacity.values, 1/8.76), f.solution.elements.DESALINATION_PLANTS.variables.capacity.values])


y_scenario_1_rounded = np.round(y_scenario_1, 2)
y_scenario_2_rounded = np.round(y_scenario_2, 2)
y_scenario_3_rounded = np.round(y_scenario_3, 2)

plt.figure(figsize=(10,7))
bar_width = 0.25
index = np.arange(len(x))

bars1 = plt.barh(index + bar_width, y_scenario_1_rounded.flatten(), bar_width, label='Config 1', color = '#2F4E77')
bars2 = plt.barh(index, y_scenario_2_rounded.flatten(), bar_width, label='Config 2', color = '#4C7BB3')
bars3 = plt.barh(index - bar_width, y_scenario_3_rounded.flatten(), bar_width, label='Config 3', color = '#7FB3D5')

plt.yticks(index, x)
plt.xlabel('Capacities of each config for {} scenario'.format(scenario))
plt.legend()
plt.savefig("images/capa_comparison_" + str(scenario) +".png", dpi=150, bbox_inches='tight')
plt.show()
