import pennylane as qml
from catalyst import qjit

dev = qml.device("lightning.qubit", wires=2)

@qjit
@qml.qnode(dev)
def circuit(x: float):
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    qml.RX(x, wires=1)
    return qml.expval(qml.Z(1))

# Call the compiled circuit to trigger compilation
# output = circuit(0.5)

# Access and print the MLIR representation
print(circuit.mlir)
