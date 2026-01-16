import maya.cmds as cmds
import os

def save(path, name, prefix ="none"):
    if not prefix:
        prefix = "base_"
    cmds.file(rename = os.path.join(path, prefix + name + ".ma"))
    cmds.file(save=True, type='mayaAscii')
    print("SAVE COMPLETED")