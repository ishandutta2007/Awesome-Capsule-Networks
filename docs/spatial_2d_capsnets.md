# 2D Spatial Part-Whole CapsNets

## Detailed Information
Configured for 2D visual tracking tasks. The capsules parameterize localized flat visual primitives (lines, corners) and capture their relative layout/hierarchical configuration.

## Architectural Diagram
```mermaid
flowchart TD
    A[2D Input Image] --> B[Convolutional Layers]
    B --> C[Primary 2D Capsules]
    C --> D[Routing Layer]
    D --> E[2D Class/Object Capsules]
```

---

[⬅️ Back to Main README](../README.md)
