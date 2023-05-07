import gmsh
import sys

model = gmsh.model
factory = model.occ


def init():
    gmsh.initialize()


def finalize():
    gmsh.finalize()


def check_param(step_file, mesh_file, mesh_size):
    # ==========================================================================================
    # Check step file suffix
    # ===========================================================================================
    if not step_file.endswith(".step") and not step_file.endswith(".stp"):
        print("ERROR: the input geometry file must be at the step format (.stp or .step)")
        exit(1)
        # ===========================================================================================
    # Check vtk file suffix
    # ===========================================================================================
    if not mesh_file.endswith(".vtk"):
        print("ERROR: the output mesh file must be a vtk legacy file (.vtk)")
        exit(1)
    # ===========================================================================================
    # Check mesh size value
    # ===========================================================================================
    if (mesh_size <= 0) or (mesh_size > 1):
        print("ERROR: the mesh size must be in ]0,1]")
        exit(1)


def gen_tet_mesh(step_file, mesh_file, mesh_size):
    check_param(step_file, mesh_file, mesh_size)
    gmsh.initialize(sys.argv)
    # ======================================================================================
    # Conversion process
    # ======================================================================================
    model.add("step_to_tet")
    factory.importShapes(step_file)
    gmsh.option.setNumber("Mesh.CharacteristicLengthFactor", mesh_size);
    factory.synchronize()
    model.mesh.generate(3)
    gmsh.write(mesh_file)
    gmsh.finalize()

