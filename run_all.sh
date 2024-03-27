#!/bin/bash
pip install -r requirements.txt
for config in 1 2 3; do
    for scenario in reference optimistic conservative; do
        echo "Lancement de la simulation pour config $config et scenario $scenario"    
        python3 main.py --config $config --scenario $scenario
        echo ""
    done
done
