# qDRIFT implementation for Hamiltonian simulation

'The idea of qDRIFT is to randomly sample terms from the Hamiltonian and apply them in a random order, based on the strength'
'of the couplings. I will do this step by step here. For the Ising Hamiltonian qDRIFT treats the Hamiltonian as a list '
'of Pauli Strings and weight.'



from qiskit.quantum_info import SparsePauliOp
from qiskit import QuantumCircuit
import numpy as np




#The Input is the hamiltonian we are going to simulate
def total_coupling(H):
    #Input: H is a SparsePauliOp object
    #Output: Returns the total coupling strength of the Hamiltonian

    coupling = H.coeffs
    total_coupling = sum(abs(coupling))

    return total_coupling

def qdrift_prob (H):
    #Input: H is a SaprsePauliOp object
    #Output: Probabilities for each term in the Hamitonian)

    coupling = H.coeffs
    probabilities= []

    for i in range(len(coupling)):
        probabilities.append(abs(coupling[i]) / total_coupling(H))

    return probabilities 






'I am going to create a helper function where you put in a label of a Pauli String and it will return the correspoinding gate  '
'applied to the circuit. Then in the actual function we will implement these in order. For the helper function, the idea is to'
'find non identity terms, and rotate the X,Y into the Z basis, so we can make a chain of CNOTS and apply a Rz rotation, then '
'rotate back.'





#note: this is the Rz rotation angle, so I will not include a factor 2
def qdrift_gate(label, angle, qc):
    #Input: label is the Pauli string, angle is the Rz rotation, qc is the circuit to apply the gate to
    #Output: circuit with the gate applied

    n_qubits = len(label)
    active_qubits =[]

    for i in range(n_qubits):
        if label[i]!='I':
            active_qubits.append(n_qubits-1-i)

    #If there are no active qubits, we don't need to do anything
    if len(active_qubits) == 0:
            return qc
      

    for i in range(n_qubits):
        qubit = n_qubits-1-i
        if label[i] == 'X':
            qc.h(qubit)
        elif label[i] == 'Y':
            qc.sdg(qubit)
            qc.h(qubit)

    #I'll set a target, apply a chain of CNOTs, then apply the Rz rotation, then undo the CNOTs and rotations
    target = active_qubits[-1]

    for i in active_qubits[:-1]:
        qc.cx(i, target)
    qc.rz(angle, target)
    for i in reversed(active_qubits[:-1]):
        qc.cx(i, target)

    for i in range(n_qubits):
        qubit = n_qubits -1 -i
        if label[i]=='X':
            qc.h(qubit)
        if label[i] == 'Y':
            qc.h(qubit)
            qc.s(qubit)

    return qc



#qdrift implements U_j= exp(-i sng(hj) lambda t/r Pj), where r is the total number of qDrift steps and the full U = Ujr... Uj1
def qDrift(H, r, t, seed = None):
    #Input: H is a SparsePauliOp object, r is the number of qDrift steps, t is the total evolution time
    #Output: Returns a QC that does r number steps

    tau = total_coupling(H)*t/r
    sign = np.sign(H.coeffs.real)
    qc = QuantumCircuit(H.num_qubits)
    prob = qdrift_prob(H)

    rng = np.random.default_rng(seed)

    index = rng.choice(len(H.coeffs), size = r, p = prob)
    label = H.paulis.to_labels()

    for j in index:
        qc = qdrift_gate(label[j], 2*sign[j]*tau, qc)

    return qc



