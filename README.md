# miami
**Miami**, that stands for **M**onitoring **I**nfr**A**structure for **M**esh**I**ng, is dedicated to monitor and control the evolution of meshing algorithms developed at LIHPC.

The purpose is to provide common tools, scripts, and CI recipes to continously evaluate meshing algorithms.

<span style="color: red;">WARNING. This repository is under construction and not usable right now.</span>
## Python scripts

The directory ‘scripts’ contains python scripts, that can be used to 
write *monitoring* pipelines:
- The script [gen_tet_mesh.py](/scripts/gmsh_api.py) uses gmsh to generate a tetrahedral mesh from a step file. It can be used to convert step files available in [mambo](https://gitlab.com/franck.ledoux/mambo) into tetrahedral meshes that will be given to the faceted geometry manager of **gmds**.
## Frame 3D testing

The frame3d testing pipeline is used in the 

### Proposed scenario
The testing framework relies on [snakemake](https://snakemake.github.io/). We build a workflow, that performs the following stages:
1. We download all the geometric models stored in the [mambo](https://gitlab.com/franck.ledoux/mambo) database into the *model* directory.
2. For each geometric model, we generate a tetrahedral mesh using the [gmsh](https://gmsh.info/) python API. Tetrahedeal meshes are stored in the *tet* directory.
3. Each tetrahedral mesh is used as an input to Sofiane's Phd work. His works consists in providing an hybrid remeshing framework that will generate a hybrid mesh that try as best as possible to fit metric and orientation field given as an input. In the testing framework, the orientation field is mainly given by the frame3D algorithm of [gmds](https://github.com/LIHPC-Computational-Geometry/gmds). The metric field is an analytic function. Results are stored in the *hexdom* directory.
4. Eventually, reports are produced with quality measures.