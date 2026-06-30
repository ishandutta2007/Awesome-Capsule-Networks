# The Expectation-Maximization & Matrix Era

## Detailed Information
Introduced in 2018 (Hinton et al.), this era swapped vector capsules for matrix capsules. Each capsule holds an activation scalar alongside a full 4x4 Pose Matrix representing spatial transformations. It uses EM Routing based on a Gaussian mixture model.

## Architectural Diagram
```mermaid
flowchart TD
    A[Pose Matrices M_i] --> B[Multiply by learned Transformation Matrices W_ij]
    B --> C[Compute Votes V_ij]
    C --> D[EM Routing Loop]
    D --> E[M-Step: Update Mean, Variance, Activation of parent capsule]
    E --> F[E-Step: Update assignment coefficients r_ij]
    F --> D
    E --> G[Final Pose and Activation Outputs]
```

---

[⬅️ Back to Main README](../README.md)
