import bpy
import math
import os

# 1. Clean scene
bpy.ops.wm.read_factory_settings(use_empty=True)

def create_pbr_material(name, base_color, metallic=0.0, roughness=0.2, emission_color=None, emission_strength=0.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = base_color
        bsdf.inputs["Metallic"].default_value = metallic
        bsdf.inputs["Roughness"].default_value = roughness
        if emission_color and "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = emission_color
            bsdf.inputs["Emission Strength"].default_value = emission_strength
    return mat

# Materials
mat_jade = create_pbr_material(
    "SomaticJade",
    base_color=(0.20, 0.68, 0.48, 1.0),
    metallic=0.22,
    roughness=0.12,
    emission_color=(0.06, 0.72, 0.50, 1.0),
    emission_strength=0.35
)

mat_gold = create_pbr_material(
    "ChampagneGold",
    base_color=(0.92, 0.68, 0.30, 1.0),
    metallic=0.96,
    roughness=0.15,
    emission_color=(0.92, 0.68, 0.30, 1.0),
    emission_strength=0.12
)

mat_silver_sage = create_pbr_material(
    "PlatinumSage",
    base_color=(0.82, 0.90, 0.84, 1.0),
    metallic=0.92,
    roughness=0.14,
    emission_color=(0.40, 0.85, 0.65, 1.0),
    emission_strength=0.15
)

mat_pearl = create_pbr_material(
    "LuminousPearl",
    base_color=(0.45, 0.98, 0.75, 1.0),
    metallic=0.1,
    roughness=0.08,
    emission_color=(0.25, 0.95, 0.68, 1.0),
    emission_strength=0.85
)

# 2. Sculpt Organic Jade Core
bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=4, radius=0.52, location=(0, 0, 0))
core = bpy.context.active_object
core.name = "JadeCore"

# Apply organic harmonic wave displacement to vertices
for v in core.data.vertices:
    x, y, z = v.co.x, v.co.y, v.co.z
    wave = 1.0 + 0.065 * math.sin(x * 5.0) * math.cos(y * 5.0) * math.sin(z * 5.0)
    v.co.x *= wave
    v.co.y *= wave
    v.co.z *= wave

bpy.ops.object.shade_smooth()
core.data.materials.append(mat_jade)

# 3. Outer Gyroscopic Ring (Champagne Gold)
bpy.ops.mesh.primitive_torus_add(
    major_radius=0.92,
    minor_radius=0.036,
    major_segments=96,
    minor_segments=28,
    location=(0, 0, 0),
    rotation=(0.55, 0.35, 0.0)
)
ring_outer = bpy.context.active_object
ring_outer.name = "RingOuter"
bpy.ops.object.shade_smooth()
ring_outer.data.materials.append(mat_gold)

# 4. Inner Gyroscopic Ring (Platinum Sage)
bpy.ops.mesh.primitive_torus_add(
    major_radius=0.74,
    minor_radius=0.026,
    major_segments=96,
    minor_segments=24,
    location=(0, 0, 0),
    rotation=(-0.50, 0.65, 0.30)
)
ring_inner = bpy.context.active_object
ring_inner.name = "RingInner"
bpy.ops.object.shade_smooth()
ring_inner.data.materials.append(mat_silver_sage)

# 5. Orbital Energy Satellites (3 nodes)
for i in range(3):
    angle = i * (2.0 * math.pi / 3.0)
    rx = 0.92 * math.cos(angle)
    ry = 0.92 * math.sin(angle)
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=24,
        ring_count=16,
        radius=0.075,
        location=(rx, ry, 0.0)
    )
    node = bpy.context.active_object
    node.name = f"SatelliteNode_{i+1}"
    bpy.ops.object.shade_smooth()
    node.data.materials.append(mat_pearl)
    node.parent = ring_outer

# 6. Export to GLB
out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "3d")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "elena_orb.glb")

bpy.ops.export_scene.gltf(
    filepath=out_path,
    export_format='GLB',
    export_apply=False
)

print(f"SUCCESS_GLB_EXPORT: {out_path} ({os.path.getsize(out_path)} bytes)")
