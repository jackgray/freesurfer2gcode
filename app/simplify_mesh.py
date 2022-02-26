from os import path, rename
import pymeshlab as meshlab

def simplifyMesh(in_file_hemi, in_file_cc, out_file, pipe_dir, pipe_file):
    
    ms = meshlab.MeshSet()
    
    if len(in_file_hemi) == 2: 
        # loads each item in the in_file_hemi
        ms.load_new_mesh(in_file_hemi[0])
        ms.load_new_mesh(in_file_hemi[1])
    
    else: 
    
        ms.load_new_mesh(in_file_hemi)
        
    # loads corpus collosum into the mesh 
    ms.load_new_mesh(in_file_cc)

    # flatten visible layers with default settings - this also combines common vertices 
    ms.apply_filter('flatten_visible_layers')

    # simplifies the mesh using a quadric based edge collapse strategy with 150000 vertices 
    ms.apply_filter('simplification_quadric_edge_collapse_decimation', targetfacenum=150000)

    # applies a laplacian smooth - Average each vertex position with weighted positions of neighbour vertices.
    ms.apply_filter('laplacian_smooth')

    # exports final combined mesh 
    ms.save_current_mesh(out_file)
    