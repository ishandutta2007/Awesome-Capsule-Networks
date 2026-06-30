import os

docs_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Capsule-Networks\docs"
os.makedirs(docs_dir, exist_ok=True)

details = [
    {
        "filename": "dynamic_routing_baseline.md",
        "title": "The Dynamic Routing Baseline Era",
        "description": "Introduced by Sabour et al. in 2017, this era marked the foundational breakthrough of Capsule Networks. It replaced scalar activations with vectors where orientation represents instantiation parameters and length represents activation probability. It introduced Routing-by-Agreement.",
        "diagram": """flowchart TD
    A[Lower Layer Capsule vectors] --> B[Compute Prediction Vectors u_hat]
    B --> C[Iterative Routing Loop]
    C --> D[Compute Coupling Coefficients c_ij via softmax]
    D --> E[Compute Candidate Parent s_j]
    E --> F[Apply Squash Activation to get v_j]
    F --> G{Agreement Check: u_hat . v_j}
    G -->|Update logs| C
    F --> H[Final Output Capsule Vectors]"""
    },
    {
        "filename": "em_routing_matrix.md",
        "title": "The Expectation-Maximization & Matrix Era",
        "description": "Introduced in 2018 (Hinton et al.), this era swapped vector capsules for matrix capsules. Each capsule holds an activation scalar alongside a full 4x4 Pose Matrix representing spatial transformations. It uses EM Routing based on a Gaussian mixture model.",
        "diagram": """flowchart TD
    A[Pose Matrices M_i] --> B[Multiply by learned Transformation Matrices W_ij]
    B --> C[Compute Votes V_ij]
    C --> D[EM Routing Loop]
    D --> E[M-Step: Update Mean, Variance, Activation of parent capsule]
    E --> F[E-Step: Update assignment coefficients r_ij]
    F --> D
    E --> G[Final Pose and Activation Outputs]"""
    },
    {
        "filename": "attention_vit_hybrid.md",
        "title": "The Attention-Driven & ViT Hybrid Era",
        "description": "Modern architectures (2021-Present) eliminate the slow, iterative dynamic routing loops by reframing capsule routing mathematically as a specialized form of self-attention. Fuses capsule properties into Vision Transformers (ViT) for fast, parallel execution.",
        "diagram": """flowchart TD
    A[Input Features] --> B[Capsule-to-Transformer Projection]
    B --> C[Multi-Head Self-Attention Layer]
    C --> D[Parallel Agreement Computation]
    D --> E[Fused Vector/Matrix Outputs]"""
    },
    {
        "filename": "dynamic_routing_cosine.md",
        "title": "Dynamic Routing (Cosine Agreement)",
        "description": "The routing mechanism used in the original 2017 CapsNet. It iteratively updates coupling coefficients using the dot product (cosine similarity) between predicted parent pose and actual parent output.",
        "diagram": """flowchart LR
    A[Prediction u_hat] --> B[Dot Product]
    C[Parent Output v_j] --> B
    B --> D[Log-Prior Update b_ij]
    D --> E[Softmax]
    E --> F[Coupling Coefficient c_ij]"""
    },
    {
        "filename": "em_routing_mechanism.md",
        "title": "EM Routing (Expectation-Maximization)",
        "description": "Treats capsule routing as a statistical clustering problem. Fits a Gaussian mixture model to the votes of lower-level capsules to determine assignment probabilities dynamically.",
        "diagram": """flowchart TD
    A[Lower votes V_ij] --> B[Gaussian G_j]
    B --> C[Maximize Likelihood M-step]
    C --> D[Calculate Probabilities E-step]
    D --> B"""
    },
    {
        "filename": "inverted_dot_product_attention.md",
        "title": "Inverted Dot-Product Attention Routing (Fast CapsNet)",
        "description": "Computes attention maps straight across capsule channels in a single forward pass. It replaces sequential iterative routing with concurrent matrix multiplications.",
        "diagram": """flowchart LR
    A[Child Capsules] --> B[Inverted Attention Matrix]
    B --> C[Channel-wise Softmax]
    C --> D[Single-pass Parent Outputs]"""
    },
    {
        "filename": "spatial_2d_capsnets.md",
        "title": "2D Spatial Part-Whole CapsNets",
        "description": "Configured for 2D visual tracking tasks. The capsules parameterize localized flat visual primitives (lines, corners) and capture their relative layout/hierarchical configuration.",
        "diagram": """flowchart TD
    A[2D Input Image] --> B[Convolutional Layers]
    B --> C[Primary 2D Capsules]
    C --> D[Routing Layer]
    D --> E[2D Class/Object Capsules]"""
    },
    {
        "filename": "volumetric_3d_point_cloud.md",
        "title": "3D Volumetric / Point Cloud CapsNets",
        "description": "Natively processes 3D point cloud coordinate arrays or volumetric medical scans. Captures absolute 3D spatial transforms, rotations, and scales using equivariant capsule layers.",
        "diagram": """flowchart TD
    A[3D Coordinates / Voxel Grid] --> B[3D Convolution / PointNet Features]
    B --> C[3D Quaternion/Matrix Capsules]
    C --> D[Equivariant Routing]
    D --> E[3D Pose/Class Outputs]"""
    },
    {
        "filename": "deep_convolutional_capsule_stacks.md",
        "title": "Deep Convolutional Capsule Stacks",
        "description": "Combines the representation power of deep CNNs with the spatial hierarchy tracking of CapsNets. Uses CNN layers for initial feature extraction and Capsule layers for terminal semantic layout reasoning.",
        "diagram": """flowchart LR
    A[Input] --> B[Deep CNN Stack]
    B --> C[Primary Capsules]
    C --> D[Capsule Routing]
    D --> E[Output Class]"""
    },
    {
        "filename": "hardware_incompatibility_latency.md",
        "title": "The Hardware Incompatibility & Latency Wall",
        "description": "A deployment challenge stemming from iterative routing loops requiring sequential, dynamic memory allocations that do not saturate standard parallelized GPU tensor cores.",
        "diagram": """flowchart TD
    A[Iterative Routing Math] --> B[Sequential Execution]
    B --> C[Low GPU Tensor Core Utilization]
    D[Mitigation: Fused Attention Kernels / Triton] --> E[GPU SRAM Register Compilation]
    E --> F[High Parallelized Speedup]"""
    },
    {
        "filename": "parameter_explosion.md",
        "title": "The Parameter Explosion Problem",
        "description": "Because capsule connections require transformation matrices for every child-parent pair, scaling to high-resolution datasets causes the parameter count to balloon.",
        "diagram": """flowchart TD
    A[Fully Connected Capsules] --> B[Transformation Matrix per Pair]
    B --> C[Parameter Count Balloons]
    D[Mitigation: Shared Transformation Matrices] --> E[Convolutional Capsules / SegCaps]
    E --> F[95.4% Parameter Reduction]"""
    },
    {
        "filename": "medical_image_segmentation.md",
        "title": "High-Precision Medical Image Diagnostic Segmentation",
        "description": "Capsule networks excel in medical segmentation (e.g. lung and tumor CT/MRI scans) due to their spatial reasoning, allowing accurate tracking of anatomical layouts with minimal training data.",
        "diagram": """flowchart TD
    A[Medical Scan CT/MRI] --> B[SegCaps Encoder]
    B --> C[Local Routing Layers]
    C --> D[SegCaps Decoder]
    D --> E[High-Precision Segmentation Mask]"""
    },
    {
        "filename": "aerospace_satellite_grounding.md",
        "title": "Aerospace & Satellite Volumetric Spatial Grounding",
        "description": "Utilized in satellite remote sensing to classify imagery and detect structural targets despite perspective tilts, seasonal conditions, or sun angle/shadow changes.",
        "diagram": """flowchart LR
    A[Satellite Imagery] --> B[Capsule Transformation]
    B --> C[Perspective & Tilt Invariance]
    C --> D[Robust Ground Asset Classification]"""
    },
    {
        "filename": "robotic_manipulation_pose.md",
        "title": "Autonomous Robotic Manipulation & Pose Estimation",
        "description": "Drives real-time grasp planning and 3D pose estimation for robotic manipulators. Capsule networks decode 3D orientation and depth to allow precise physical interaction.",
        "diagram": """flowchart TD
    A[Camera Feed / Point Cloud] --> B[GraspCaps Network]
    B --> C[3D Orientation & Depth Decoding]
    C --> D[6DoF Grasp Formulation]
    D --> E[Robot Arm Grasp Execution]"""
    }
]

for detail in details:
    filepath = os.path.join(docs_dir, detail["filename"])
    content = f"""# {detail["title"]}

## Detailed Information
{detail["description"]}

## Architectural Diagram
```mermaid
{detail["diagram"]}
```

---

[⬅️ Back to Main README](../README.md)
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Done generating detailed pages!")
