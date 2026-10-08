from qiskit import QuantumCircuit

def ferm_first_trotter_step(J, n_qubits, dt):
    #Input: J is the coupling, n_qubits qubits number, dt time interval
    #Output: the first trotter step

    qc = QuantumCircuit(n_qubits)

    #XX gate with angle -J*dt
    for i in range(n_qubits -1):
        qc.rxx(-J*dt,i,i+1)

    #YY gate with angel -J*dt
    for i in range(n_qubits -1):
        qc.ryy(-J*dt,i,i+1)

    return(qc)


def ferm_first_trotterization(J, n_qubits, t, n_steps):
    #Input:
    #Ouput: First order Trotterization circuit for n steps

    qc= QuantumCircuit(n_qubits)
    dt=t/n_steps

    for _ in range(n_steps):
        step = ferm_first_trotter_step(J, n_qubits, dt)
        qc.compose(step, inplace=True)

    return(qc)




def ferm_second_trotter_step(J, n_qubits,dt):

    qc = QuantumCircuit(n_qubits)

    #half XX gate
    for i in range(n_qubits-1):
        qc.rxx(-J/2*dt,i,i+1)
    for i in range(n_qubits -1):
        qc.ryy(-J*dt, i, i+1)
    for i in range(n_qubits -1):
        qc.rxx(-J/2*dt,i, i+1)

    return (qc)

def ferm_second_trotterization(J, n_qubits, t, n_steps):

    qc = QuantumCircuit(n_qubits)
    dt = t/n_steps

    for _ in range(n_steps):
        step = ferm_second_trotter_step(J, n_qubits, dt)
        qc.compose(step, inplace= True)

    return(qc)