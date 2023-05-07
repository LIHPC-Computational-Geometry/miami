from mambo_api import read as read_step
from gmsh_api import gen_tet_mesh
import subprocess

if __name__ == "__main__":
    #We read all the step files
    step_files = read_step("mambo", "Basic")
    print(step_files)
    for step_file in step_files:
        # We create the corresponding vtk file
        vtk_tet_mesh_file = step_file.replace(".step", ".vtk")
        out_file = step_file.replace(".step", "_out.vtk")
        # and fill it with a tetrahedral mesh
        gen_tet_mesh(step_file, vtk_tet_mesh_file, 0.2)
        # then we invocate the frame3d executable to generate a frame field
        process = subprocess.Popen(["./build_gmds/bin/frame3dExe", vtk_tet_mesh_file, out_file], shell=False)
        out, err = process.communicate()
        errcode = process.returncode
        print(errcode)
        process.kill()
        process.terminate()
