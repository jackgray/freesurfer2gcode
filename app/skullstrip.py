from os import abspath, path, mkdir
from nipype import Node, Workflow
from nipype.interfaces.freesurfer import ReconAll, MRIConvert

def skullStrip(in_file):
    # defines subjects_dir path 
    subjects_dir = abspath('anat')
    if not path.isdir(subjects_dir):
        mkdir(subjects_dir)
        
    # autorecon1 interface with manually defined cmdline method 
    recon1 = Node(ReconAll(), name='autorecon1')
    recon1.inputs.subject_id = subject_id
    recon1.inputs.directive = 'autorecon1'
    recon1.inputs.subjects_dir = subjects_dir
    recon1.inputs.T1_files = abspath(in_file)
    # if the run is interrupted, this line allows the run to be resumed without manually deleting the log files
    recon1.inputs.args = '-no-isrunning'

    recon_convert = Node(MRIConvert(), name='mgztonii')
    recon_convert.inputs.out_type = 'nii'

    # creates nested workflow
    skullstrip = Workflow(name=subject_id + '_skullstrip_' + args.s)   
    skullstrip.connect(recon1, 'brainmask', recon_convert, 'in_file')

