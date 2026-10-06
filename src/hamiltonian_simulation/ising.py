#Write the Ising Hamiltonian: H = -J * sum(Z_i * Z_i+1) - h * sum(X_i)

from qiskit.quantum_info import SparsePauliOp

def ising_hamiltonian(J, h, n_qubits):

    #Input: n_qubits is the number of qubits in the system, J and h are the coupling and external field strengths respectively
    #Output: Returns the Ising Hamiltonian as a SparsePauliOp object

    #create a list to hold the Pauli strings and their coefficients
    pauli_strings = []
    coefficients = []

    #We want a periodic boundary condition, so we will add the ZZ term for the last qubit and the first qubit
    for i in range(n_qubits):
        zz_term = ['I']*n_qubits
        zz_term[i]='Z'
        zz_term[(i+1)%n_qubits]= 'Z'
        pauli_strings.append(''.join(zz_term))
        coefficients.append(-J)

    #Add X terms for each qubit
    for i in range(n_qubits):
        x_term = ['I']*n_qubits
        x_term[i]='X'
        pauli_strings.append(''.join(x_term))
        coefficients.append(-h)


    return SparsePauliOp(pauli_strings, coeffs = coefficients)

    


    