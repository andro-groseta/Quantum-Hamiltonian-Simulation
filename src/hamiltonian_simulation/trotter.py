from qiskit import QuantumCircuit

#Start with first oder Trotterization, e^(-iHt) = e^(-iH1t)e^(-iH2t)...e^(-iHnt)

def first_trotter_step(J, h, n_qubits, dt):
    #Input: n_qubits is the number of qubits in the system, J and h are the coupling and external field strengths respectively, t is the time step
    #Output: Returns a QuantumCircuit that implements the first order Trotterization of the Ising Hamiltonian

    #create a quantum circuit with n_qubits
    qc = QuantumCircuit(n_qubits)

    # Qiskit defines RZZ(theta) = exp(-i theta ZZ / 2).
    # For H_ZZ = -J ZZ, exp(-i H_ZZ dt) = exp(+i J dt ZZ),so theta = -2 J dt. 
    # note: periodic boundary conditions are implemented by using (i+1)%n_qubits to wrap around to the first qubit when i is the last qubit
    for i in range(n_qubits):
        qc.rzz(-2*J*dt, i, (i+1)%n_qubits)

    #Apply the X terms
    for i in range(n_qubits):
        qc.rx(-2*h*dt, i)

    return qc





def first_trotterization(J, h, n_qubits, t, n_steps): 
    #Input: n_qubits is the number of qubits in the system, J and h are the coupling and external field strengths respectively, t is the total time, n_steps is the number of Trotter steps
    #Output: Returns a QuantumCircuit that implements the first order Trotterization of the Ising Hamiltonian for time t

    #create a quantum circuit with n_qubits
    qc = QuantumCircuit(n_qubits)

    #calculate the time step
    dt = t/n_steps

    #apply the first order Trotterization for n_steps
    for _ in range(n_steps):
        step = first_trotter_step(J, h, n_qubits, dt)
        qc.compose(step, inplace= True)

    return qc









def second_trotter_step(J, h, n_qubits, dt):

    #Input and Output are the same as the first_trotter_step function

    #The second order Trotterization is given by e^(-iHt) = e^(-iH1t/2)e^(-iH2t)e^(-iH1t/2)
    #We need to do the same thing as before, but need to do "half" steps for Z, then a full step for X, then another "half" step for Z
    #So the angle in the Z is going to be half of what it was in the first trotter step

    qc = QuantumCircuit(n_qubits)

    for i in range(n_qubits):
        qc.rzz(-J*dt, i, (i+1)%n_qubits)

    for i in range(n_qubits):
        qc.rx(-2*h*dt, i)

    for i in range(n_qubits):
        qc.rzz(-J*dt, i, (i+1)%n_qubits)

    return qc




def second_trotterization(J, h, n_qubits, t, n_steps):

    qc = QuantumCircuit(n_qubits)

    dt = t/n_steps
    for _ in range(n_steps):
        step = second_trotter_step(J, h, n_qubits, dt)
        qc.compose(step, inplace = True)

    return qc
