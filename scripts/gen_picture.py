#### import the simple module from the paraview
from paraview.simple import *
import sys
import time
import PIL
def create_pictures_XYZ(input):
    if(not input.endswith(".vtk")):
        print("ERROR: input file must be a VTK legacy file (.vtk)")
        exit(1)

        
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()
    
    paraview.simple.Disconnect()
    paraview.simple.Connect()
    # create a new 'Legacy VTK Reader'
    data = LegacyVTKReader(FileNames=[input])
    
    # get active view
    rv = GetActiveViewOrCreate('RenderView')
    vtkDisplay = Show(data, rv)
    # trace defaults for the display properties.
    vtkDisplay.Representation = 'Surface'
    vtkDisplay.ColorArrayName = [None, '']
    vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    vtkDisplay.SelectOrientationVectors = 'None'
    vtkDisplay.ScaleFactor = 1.8
    vtkDisplay.SelectScaleArray = 'None'
    vtkDisplay.GlyphType = 'Arrow'
    vtkDisplay.GlyphTableIndexArray = 'None'
    vtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
    vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
    vtkDisplay.ScalarOpacityUnitDistance = 0.5045513280420133

    
    # Hide orientation axes
    #renderView1.OrientationAxesVisibility = 0
    
    # Properties modified on renderView1
    rv.UseGradientBackground = 1

    # Properties modified on renderView1
    rv.Background2 = [1.0, 1.0, 1.0]

    camera=GetActiveCamera()
    # reset view to fit data
    rv.ResetCamera()
    # update the view to ensure updated data information
    rv.Update()
    # save screenshot
   # time.sleep(1)
    WriteImage(input.replace(".vtk","_Z.png"), rv, ImageResolution=[996, 800])
   
    camera.Yaw(90)
    rv.ResetCamera()
    rv.Update()
    #time.sleep(1)
    WriteImage(input.replace(".vtk","_X.png"), rv, ImageResolution=[996,800])    
    
    camera.Pitch(90)
    rv.ResetCamera()
    rv.Update()
    #time.sleep(1)
    WriteImage(input.replace(".vtk","_Y.png"), rv, ImageResolution=[996,800])  

    camera.Pitch(45)
    camera.Yaw(45)
    rv.ResetCamera()
    rv.Update()
    #time.sleep(1)
    WriteImage(input.replace(".vtk","_XYZ.png"), rv, ImageResolution=[996,800])      

    Delete(data)
    del(data)
    
if __name__=="__main__":
    if(not len(sys.argv)==2):
        print("Wrong usage, it should be:")
        print("\t python gen_picture.py in.vtk ")
        print("where  in.vtk contains a mesh (vtk format).")
        exit(1)
        
    input = sys.argv[1]
    create_pictures_XYZ(input)
