import maya.cmds as cmds
import os

def reference_file(path, namespaceAttr = ""):
    cmds.file(path, reference = True, namespace = namespaceAttr)
    print("IMPORT REFERENCE COMPLETED")