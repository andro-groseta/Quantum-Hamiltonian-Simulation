from qiskit.quantum_info import SparsePauliOp

def ferm_hop_hamiltonian(J, n_qubits):
    # Input: h is the coupling, n_qubits is the number of qubits in the system
    # Output: returns the fermionic hopping hamiltonian as a SparsePauliOp object

    pauli_string = []
    coeff = []


    for i in range(n_qubits -1):
        xx_term= ['I']*n_qubits
        xx_term[i] = 'X'
        xx_term[i+1] = 'X'
        pauli_string.append(''.join(xx_term))
        coeff.append(-J/2)

    for i in range(n_qubits-1):
        yy_term=['I']*n_qubits
        yy_term[i] = 'Y'
        yy_term[i+1]='Y'
        pauli_string.append(''.join(yy_term))
        coeff.append(-J/2)

    fhh= SparsePauliOp(pauli_string, coeffs= coeff)

    return(fhh)