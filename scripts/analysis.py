import pandas

def define_table():

if __name__ == "__main__":
    results
    #We read all the step files
    step_files = read_step("mambo", "Basic")
    for step_file in step_files:
        # We create the corresponding vtk file
        vtk_tet_mesh_file = step_file.replace(".step", ".vtk")
        # and fill it with a tetrahedral mesh
        gen_tet_mesh(step_file, vtk_tet_mesh_file, 0.2)
        # then we invocate the frame3d executable to generate a frame field
        process = subprocess.Popen("./frame3d", shell=False)
        out, err = process.communicate()
        errcode = process.returncode
        print(errcode)
        process.kill()
        process.terminate()
