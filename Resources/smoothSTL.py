import bpy
import glob
import os
import time
import sys
import argparse

subsurf = 'Subsurf' if (2, 80, 0) >= bpy.app.version else 'Subdivision'


class ArgumentParserForBlender(argparse.ArgumentParser):
    """
    This class is identical to its superclass, except for the parse_args
    method (see docstring). It resolves the ambiguity generated when calling
    Blender from the CLI with a python script, and both Blender and the script
    have arguments. E.g., the following call will make Blender crash because
    it will try to process the script's -a and -b flags:
    >>> blender --python my_script.py -a 1 -b 2

    To bypass this issue this class uses the fact that Blender will ignore all
    arguments given after a double-dash ('--'). The approach is that all
    arguments before '--' go to Blender, arguments after go to the script.
    The following calls work fine:
    >>> blender --python my_script.py -- -a 1 -b 2
    >>> blender --python my_script.py --
    """

    def _get_argv_after_doubledash(self):
        try:
            idx = sys.argv.index("--")
            return sys.argv[idx+1:] # the list after '--'
        except ValueError as e: # '--' not in the list:
            return []

    def parse_args(self):
        return super().parse_args(args=self._get_argv_after_doubledash())


def main():
    # Clear the scene
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # Process all unprocessed stl's in the current directory
    here = bpy.path.abspath(base_dir)

    for stl_fname in glob.glob(os.path.join(here, '*.stl')):
        if ('-smooth.stl' in stl_fname) or (os.path.exists(stl_fname.replace('.stl', '-smooth.stl'))):
            print('Skipping %r' % stl_fname)
            continue

        process(stl_fname)
    print('Quitting in 10 seconds...')

    time.sleep(10)
    bpy.ops.wm.quit_blender()


def process(stl_fname):
    print('Processing %r' % stl_fname)

    # Determine output filename.
    out_fname = stl_fname.replace('.stl', '-smooth.stl')

    # Import file
    bpy.ops.import_mesh.stl(filepath=stl_fname)

    # wizz bang stuff from John Smith
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.tris_convert_to_quads()
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.modifier_add(type='BEVEL')
    bpy.context.object.modifiers["Bevel"].width = 0.056
    bpy.context.object.modifiers["Bevel"].segments = 2
    bpy.context.object.modifiers["Bevel"].profile = 1
    bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
    bpy.context.object.modifiers["Bevel"].angle_limit = 0.698132
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers[subsurf].levels = 2

    if bpy.app.version >= (2, 90, 0):
        bpy.ops.object.modifier_apply()
    else:
        bpy.ops.object.modifier_apply(apply_as='DATA')

    # write out the new file and delete the mesh from blender
    print('Writing to %r' % out_fname)
    bpy.ops.export_mesh.stl(filepath=out_fname)
    bpy.ops.object.delete()


parser = ArgumentParserForBlender()
parser.add_argument('dir', nargs='?', default=os.getcwd(), help="Directory to process. Defaults to the current directory.")

args = parser.parse_args()

base_dir = args.dir

main()
