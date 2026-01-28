import maya.cmds as cmds
import os

def import_file(path):
    cmds.file(path, i=True, f = True)
    print("IMPORT COMPLETED")