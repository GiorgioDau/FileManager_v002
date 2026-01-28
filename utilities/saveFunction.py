import maya.cmds as cmds
import os

def save(path, name,):
    
    cmds.file(rename = os.path.join(path, prefix + name + ".ma"))
    cmds.file(save=True, type='mayaAscii', f=True)
    print("SAVE COMPLETED")