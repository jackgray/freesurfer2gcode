#!/bin/env python

from nipype.interfaces.freesurfer import recon_all, MRIConvert

# Custom imports
from skullstrip import skullStrip
from simplify_mesh import simplifyMesh

# Skull strip
skullStrip(in_file)

# Nest workflow
skullStrip = Workflow(name=subjec_id + '_skullstrip')
skullStrip.connect(recon1\, 'brainmask', reconConvert, 'in_file')

# create custom nipype interface for mesh simplification
mesh_image_interface = Function(
    input_names = ['in_file_hemi', 'in_file_cc', 'out_file', 'pipe_dir', 'pipe_file'],
    output_names = ['out_file'],
    function = simplifyMesh
)
mesh_image_interface.inputs.out_file = file_name + '.stl'
# Cortical mesh generation
mesh_combine = Node(mesh_image_interface, name='mesh_combine')
mesh_generate = Workflow(name=subject_id + '_mesh')

mesh_generate.connect(recon1)