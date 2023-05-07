import os
import gmsh_api
import gen_picture
current_dir = os.getcwd()

def getStepFiles(d):
    l=[]
    for sdp,Lsd, Lnf in os.walk(d):
        for f in Lnf:
            if(f.endswith(".step")):
               l.append(f)
    l.sort()
    return l


def generatePNG(d):
    for f in getStepFiles(d):
        abs_f = d+'/'+f
        vtk_f = f.replace(".step", ".vtk")
        print("===>> convert "+f+" <<===")
        gen_tet_mesh.init()
        gen_tet_mesh.process(abs_f,vtk_f,0.3)
        gen_tet_mesh.finalize()
        
        gen_picture.create_pictures_XYZ(vtk_f)
        os.remove(vtk_f)

if __name__ == "__main__":
    basic_dir = current_dir+"/../Basic"
    simple_dir = current_dir+"/../Simple"
    medium_dir = current_dir+"/../Medium"
    generatePNG(basic_dir)
    generatePNG(simple_dir)
    generatePNG(medium_dir)
