#!/bin/bash
pip install -r requirements.txt
for config in 1 2 3; do
    for scenario in reference optimistic conservative; do
        echo "Simulation launch for config $config and $scenario scenario"    
        python3 main.py --config $config --scenario $scenario
        echo ""
    done
done
