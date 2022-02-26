#!/bin/env python

from nipype.interfaces.freesurfer import recon_all, MRIConvert

# Skull strip
recon_all = Node(ReconAll(), name='recon_all')
recon_all.inputs.subject_id = subject_id
recon_all.inputs.T1_files = abspath(args.input)

reconConvert = Node(MRIConvert(), name='mgztonii')
reconConvert.inputs.out_type = 'nii'

# Nest workflow
skullStrip = Workflow(name=subjec_id + '_skullstrip')
skullStrip.connect(recon_all\, 'brainmask', reconConvert, 'in_file')

# Cortical mesh generation
mesh_combine = Node(mesh_image_interface, name='mesh_combine')
mesh_generate = Workflow(name=subject_id + '_mesh')

mesh_generate.connect(recon_all)