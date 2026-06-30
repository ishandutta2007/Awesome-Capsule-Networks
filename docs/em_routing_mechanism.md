# EM Routing (Expectation-Maximization)

## Detailed Information
Treats capsule routing as a statistical clustering problem. Fits a Gaussian mixture model to the votes of lower-level capsules to determine assignment probabilities dynamically.

## Architectural Diagram
```mermaid
flowchart TD
    A[Lower votes V_ij] --> B[Gaussian G_j]
    B --> C[Maximize Likelihood M-step]
    C --> D[Calculate Probabilities E-step]
    D --> B
```

---

[⬅️ Back to Main README](../README.md)
