# Inverted Dot-Product Attention Routing (Fast CapsNet)

## Detailed Information
Computes attention maps straight across capsule channels in a single forward pass. It replaces sequential iterative routing with concurrent matrix multiplications.

## Architectural Diagram
```mermaid
flowchart LR
    A[Child Capsules] --> B[Inverted Attention Matrix]
    B --> C[Channel-wise Softmax]
    C --> D[Single-pass Parent Outputs]
```

---

[⬅️ Back to Main README](../README.md)
