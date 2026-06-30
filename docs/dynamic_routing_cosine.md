# Dynamic Routing (Cosine Agreement)

## Detailed Information
The routing mechanism used in the original 2017 CapsNet. It iteratively updates coupling coefficients using the dot product (cosine similarity) between predicted parent pose and actual parent output.

## Architectural Diagram
```mermaid
flowchart LR
    A[Prediction u_hat] --> B[Dot Product]
    C[Parent Output v_j] --> B
    B --> D[Log-Prior Update b_ij]
    D --> E[Softmax]
    E --> F[Coupling Coefficient c_ij]
```

---

[⬅️ Back to Main README](../README.md)
