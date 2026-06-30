# The Dynamic Routing Baseline Era

## Detailed Information
Introduced by Sabour et al. in 2017, this era marked the foundational breakthrough of Capsule Networks. It replaced scalar activations with vectors where orientation represents instantiation parameters and length represents activation probability. It introduced Routing-by-Agreement.

## Architectural Diagram
```mermaid
flowchart TD
    A[Lower Layer Capsule vectors] --> B[Compute Prediction Vectors u_hat]
    B --> C[Iterative Routing Loop]
    C --> D[Compute Coupling Coefficients c_ij via softmax]
    D --> E[Compute Candidate Parent s_j]
    E --> F[Apply Squash Activation to get v_j]
    F --> G{Agreement Check: u_hat . v_j}
    G -->|Update logs| C
    F --> H[Final Output Capsule Vectors]
```

---

[⬅️ Back to Main README](../README.md)
