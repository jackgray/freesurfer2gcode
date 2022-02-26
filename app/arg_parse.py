from argparse import ArgumentParser

parser = ArgumentParser(description='Enter the path to a T1 MRI image to attempt to convert it to a printable gcode file.')
parser.add_argument('-f', 
                    type=str,
                    help='Enter path to structural nifti file (should be T1 for best results)',
                    required=True)
args = parser.parse_args()
