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

parser.add_argument('-sc', '--scenario', help='Scenario', 
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

filename = "results/config2_"+ str(scenario) + ".json"
dico = {}
with open(filename, "r") as fp:
    dico = json.load(fp)
   
e = MakeMeReadable(dico)

filename = "results/config3_"+ str(scenario) + ".json"
dico = {}
with open(filename, "r") as fp:
    dico = json.load(fp)
   
f = MakeMeReadable(dico)

years = 5
wind1 = (np.sum([e.solution.elements.WIND_PLANTS.objectives.unnamed[0], e.solution.elements.WIND_PLANTS.objectives.unnamed[1]]))/(647.6268*years)
hydrogen1 = (e.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[0] + e.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[1] + e.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[0] + e.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[1])/(647.6268*years)
battery1 = ( np.sum([e.solution.elements.BATTERY_STORAGE.objectives.unnamed[0],e.solution.elements.BATTERY_STORAGE.objectives.unnamed[1]]))/(647.6268*years)
solar1 = (e.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[0] + e.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[1])/(647.6268*years)
FT1 = (e.solution.elements.FT_PROCESS.objectives.unnamed[0] + e.solution.elements.FT_PROCESS.objectives.unnamed[1] + e.solution.elements.PETROL_CARRIERS.objectives.unnamed[0] + e.solution.elements.PETROL_CARRIERS.objectives.unnamed[1])/(647.6268*years)
CO21 = (e.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[0] + e.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[1] + e.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[0] + e.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[1]  )/(647.6268*years)
Others1 = (e.solution.elements.HVDC.objectives.unnamed[0] + e.solution.elements.HVDC.objectives.unnamed[1]  + e.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0] + e.solution.elements.DESALINATION_PLANTS.objectives.unnamed[1] + e.solution.elements.WATER_STORAGE.objectives.unnamed[0] + e.solution.elements.WATER_STORAGE.objectives.unnamed[1])/(647.6268*years)

wind2 = (np.sum([d.solution.elements.WIND_PLANTS.objectives.unnamed[0], d.solution.elements.WIND_PLANTS.objectives.unnamed[1]]))/(647.6268*years)
hydrogen2 = (d.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[0] + d.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[1] + d.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[0] + d.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[1])/(647.6268*years)
battery2 = ( np.sum([d.solution.elements.BATTERY_STORAGE.objectives.unnamed[0],d.solution.elements.BATTERY_STORAGE.objectives.unnamed[1]]))/(647.6268*years)
solar2 = (d.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[0] + d.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[1])/(647.6268*years)
FT2 = (d.solution.elements.FT_PROCESS.objectives.unnamed[0] + d.solution.elements.FT_PROCESS.objectives.unnamed[1] + d.solution.elements.PETROL_CARRIERS.objectives.unnamed[0] + d.solution.elements.PETROL_CARRIERS.objectives.unnamed[1])/(647.6268*years)
CO22 = (d.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[0] + d.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[1] + d.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[0] + d.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[1] )/(647.6268*years)
Others2 = (d.solution.elements.HVDC.objectives.unnamed[0] + d.solution.elements.HVDC.objectives.unnamed[1]  + d.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0] + d.solution.elements.WATER_STORAGE.objectives.unnamed[0])/(647.6268*years)

wind3 = (np.sum([f.solution.elements.WIND_PLANTS.objectives.unnamed[0], f.solution.elements.WIND_PLANTS.objectives.unnamed[1]]))/(647.6268*years)
hydrogen3 = (f.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[0] + f.solution.elements.ELECTROLYSIS_PLANTS.objectives.unnamed[1] + f.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[0] + f.solution.elements.HYDROGEN_STORAGE.objectives.unnamed[1])/(647.6268*years)
battery3 = ( np.sum([f.solution.elements.BATTERY_STORAGE.objectives.unnamed[0],f.solution.elements.BATTERY_STORAGE.objectives.unnamed[1]]))/(647.6268*years)
solar3 = (f.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[0] + f.solution.elements.SOLAR_PV_PLANTS.objectives.unnamed[1])/(647.6268*years)
FT3 = (f.solution.elements.FT_PROCESS.objectives.unnamed[0] + f.solution.elements.FT_PROCESS.objectives.unnamed[1] + f.solution.elements.PETROL_CARRIERS.objectives.unnamed[0] + f.solution.elements.PETROL_CARRIERS.objectives.unnamed[1])/(647.6268*years)
CO23 = (f.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[0] + f.solution.elements.DIRECT_AIR_CAPTURE_PLANTS.objectives.unnamed[1] + f.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[0] + f.solution.elements.CARBON_DIOXIDE_STORAGE.objectives.unnamed[1]  )/(647.6268*years)
Others3 = (f.solution.elements.HVDC.objectives.unnamed[0] + f.solution.elements.HVDC.objectives.unnamed[1]  + f.solution.elements.DESALINATION_PLANTS.objectives.unnamed[0] + f.solution.elements.DESALINATION_PLANTS.objectives.unnamed[1] + f.solution.elements.WATER_STORAGE.objectives.unnamed[0] + f.solution.elements.WATER_STORAGE.objectives.unnamed[1])/(647.6268*years)

colors = ['#BFC9CA', '#D35400', '#F5B041', '#F4D03F', '#ABEBC6', '#5DADE2', '#2ECC71']
categories = ['Config 3', 'Config 2', 'Config 1']
cost_types = ['Others', 'FT-Process', 'Battery', 'Solar PV', 'Wind', 'Hydrogen', 'CO2']
values = np.array([[Others3, Others1, Others2 ],
                [FT3, FT1, FT2],
                    [battery3, battery1, battery2],
                [solar3, solar1, solar2],
                [wind3, wind1, wind2],
                [hydrogen3, hydrogen1, hydrogen2],
                [CO23, CO21, CO22],])


fig, ax = plt.subplots()
bottoms = np.zeros(len(categories))
for i, cost_type in enumerate(cost_types):
    bars = ax.barh(categories, values[i], left=bottoms, label=cost_type, color=colors[i])
    bottoms += values[i]

last_bottoms = bottoms
for j, bar in enumerate(bars):
    value = last_bottoms[j]
    ax.text(bar.get_x() + bar.get_width() + 0.01, bar.get_y() + bar.get_height() / 2, str(round(value, 2)), ha='left',
            va='center')


ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
ax.set_xlim(right=max(bottoms) * 1.2)  
plt.savefig("images/cost_comparison_" + str(scenario) +".png", dpi=150, bbox_inches='tight')




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


scenarios = ['Optimistic', 'Reference', 'Conservative']
x = ["Config 3", "Config 2", "Config 1"]
y_scenario_1 = np.array([1.73, 1.69, 1.92])
y_scenario_2 = np.array([2.18, 2.13, 2.41])
y_scenario_3 = np.array([2.63, 2.57, 2.9])  

y_scenario_1_rounded = np.round(y_scenario_1, 2)
y_scenario_2_rounded = np.round(y_scenario_2, 2)
y_scenario_3_rounded = np.round(y_scenario_3, 2)

plt.figure(figsize=(10,7))
bar_width = 0.25
index = np.arange(len(x))

bars1 = plt.barh(index + bar_width, y_scenario_1_rounded.flatten(), bar_width, label='Optimistic', color = '#FFD700')
bars2 = plt.barh(index, y_scenario_2_rounded.flatten(), bar_width, label='Reference', color = '#FFA500')
bars3 = plt.barh(index - bar_width, y_scenario_3_rounded.flatten(), bar_width, label='Conservative', color = '#FF8C00')

plt.yticks(index, x)


for i, bar in enumerate(bars1):
    plt.text(bar.get_width() + 0.1/5, bar.get_y() + bar.get_height()/2, y_scenario_1_rounded[i], ha='left', va='center', color='black', fontsize=10)

for i, bar in enumerate(bars2):
    plt.text(bar.get_width() + 0.1/5, bar.get_y() + bar.get_height()/2, y_scenario_2_rounded[i], ha='left', va='center', color='black', fontsize=10)

for i, bar in enumerate(bars3):
    plt.text(bar.get_width() + 0.1/5, bar.get_y() + bar.get_height()/2, y_scenario_3_rounded[i], ha='left', va='center', color='black', fontsize=10)

plt.legend()

plt.savefig("images/all_cost_comparison_FT.png", dpi=150, bbox_inches='tight')
