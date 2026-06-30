# The Parameter Explosion Problem

## Detailed Information
Because capsule connections require transformation matrices for every child-parent pair, scaling to high-resolution datasets causes the parameter count to balloon.

## Architectural Diagram
```mermaid
flowchart TD
    A[Fully Connected Capsules] --> B[Transformation Matrix per Pair]
    B --> C[Parameter Count Balloons]
    D[Mitigation: Shared Transformation Matrices] --> E[Convolutional Capsules / SegCaps]
    E --> F[95.4% Parameter Reduction]
```

---

[⬅️ Back to Main README](../README.md)
