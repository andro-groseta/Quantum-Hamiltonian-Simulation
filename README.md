# Quantum Hamiltonian Simulation

This project covers Hamiltonian simulations for the time evolution of quantum many-body-hamiltonians.

Currently it covers:
- First-order Trotterization
- Second-order Trotterization
- qDRIFT

The first analized Hamiltonian is the transverse-field Ising-Hamiltonian $H = -J\sum_i Z_iZ_{i+1} -h\sum_i X_i$ with periodic boundary conditions. The second is the fermionic hopping Hamiltonian $H = J\sum_i^{N-2}(X_iX_{i+1} + Y_iY_{i+1})$ with open boundary conditions.

## Project Structure

```text
quantum-hamiltonian-simulation/
├── notebooks/
│   ├── 01_ising_time_evolution.ipynb
|   └── 02_fermionic_hopping.ipynb
├── src/
│   └── hamiltonian_simulation/
│       ├── __init__.py
|       ├── ferm_trotter.py
|       ├── ferm.py
│       ├── ising.py
│       ├── trotter.py
│       └── qdrift.py
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```
The src/hamiltonian_simulation package contains the reusable code, while the notebooks are reserved for analysis.

## Methods

1. Trotterization

In Trotterization, the time-evolution operator is estimated via product formulae. This project goes to 2nd order.

2. qDRIFT

qDRIFT is a stochastic approximation technique, in which the Hamiltonian is split into the composing Pauli-strings, where the probabilistic weight is assigned using the hamiltonian coefficients.

## Benchmark

The methods of comparison used in this notebook are
- State Infidelity
- Native two-qubit gates
- Circuit depth

## Installation and usage

Clone the repository and install in editable mode. The functions can then be imported.

e.g from hamiltonian_simulation.ising import ising_hamiltonian

## Future Work

Planned extensions:
- 

