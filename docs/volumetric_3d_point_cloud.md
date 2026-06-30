# 3D Volumetric / Point Cloud CapsNets

## Detailed Information
Natively processes 3D point cloud coordinate arrays or volumetric medical scans. Captures absolute 3D spatial transforms, rotations, and scales using equivariant capsule layers.

## Architectural Diagram
```mermaid
flowchart TD
    A[3D Coordinates / Voxel Grid] --> B[3D Convolution / PointNet Features]
    B --> C[3D Quaternion/Matrix Capsules]
    C --> D[Equivariant Routing]
    D --> E[3D Pose/Class Outputs]
```

---

[⬅️ Back to Main README](../README.md)
