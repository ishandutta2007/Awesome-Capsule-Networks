# Autonomous Robotic Manipulation & Pose Estimation

## Detailed Information
Drives real-time grasp planning and 3D pose estimation for robotic manipulators. Capsule networks decode 3D orientation and depth to allow precise physical interaction.

## Architectural Diagram
```mermaid
flowchart TD
    A[Camera Feed / Point Cloud] --> B[GraspCaps Network]
    B --> C[3D Orientation & Depth Decoding]
    C --> D[6DoF Grasp Formulation]
    D --> E[Robot Arm Grasp Execution]
```

---

[⬅️ Back to Main README](../README.md)
