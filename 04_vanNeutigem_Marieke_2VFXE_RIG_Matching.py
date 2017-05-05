#----------------------------SCRIPT01---------------------------------------
import maya.cmds as cmds
#script to set from FK to IK (left arm)

Shoulder_rot = cmds.xform("L_Shoulder_IK_Jnt", q = True, ws = True, ro = True)
cmds.xform("L_Shoulder_FK_Ctrl", ws = True, ro = Shoulder_rot)

Elbow_rot = cmds.xform("L_Elbow_IK_Jnt", q = True, ws = True, ro = True)
cmds.xform("L_Elbow_FK_Ctrl", ws = True, ro = Elbow_rot)

Elbow_trans = cmds.xform("L_Elbow_IK_Jnt", q = True, ws = True, t = True)
cmds.xform("L_Elbow_FK_Ctrl", ws = True, t = Elbow_trans)

Wrist_rot = cmds.xform("L_Arm_IK_Ctrl", q = True, ws = True, ro = True)
cmds.xform("L_Wrist_FK_Ctrl", ws = True, ro = Wrist_rot)

Wrist_trans = cmds.xform("L_Arm_IK_Ctrl", q = True, ws = True, t = True)
cmds.xform("L_Wrist_FK_Ctrl", ws = True, t = Wrist_trans)
#---------------------------------------------------------------------------
#----------------------------SCRIPT02---------------------------------------
import maya.cmds as cmds
#script to set from IK to FK (left arm)

Elbow_rot = cmds.xform("L_Elbow_FK_Ctrl", q = True, ws = True, ro = True)
cmds.xform("L_Elbow_IK_Ctrl", ws = True, ro = Elbow_rot)

Elbow_trans = cmds.xform("L_Elbow_FK_Ctrl", q = True, ws = True, t = True)
cmds.xform("L_Elbow_IK_Ctrl", ws = True, t = Elbow_trans)

Wrist_rot = cmds.xform("L_Wrist_FK_Ctrl", q = True, ws = True, ro = True)
cmds.xform("L_Arm_IK_Ctrl", ws = True, ro = Wrist_rot)

Wrist_trans = cmds.xform("L_Wrist_FK_Ctrl", q = True, ws = True, t = True)
cmds.xform("L_Arm_IK_Ctrl", ws = True, t = Wrist_trans)
#---------------------------------------------------------------------------
#----------------------------SCRIPT03---------------------------------------
import maya.cmds as cmds
#script to set from FK to IK (right arm)

Shoulder_rot = cmds.xform("R_Shoulder_IK_Jnt", q = True, ws = True, ro = True)
cmds.xform("R_Shoulder_FK_Ctrl", ws = True, ro = Shoulder_rot)

Elbow_rot = cmds.xform("R_Elbow_IK_Jnt", q = True, ws = True, ro = True)
cmds.xform("R_Elbow_FK_Ctrl", ws = True, ro = Elbow_rot)

Elbow_trans = cmds.xform("R_Elbow_IK_Jnt", q = True, ws = True, t = True)
cmds.xform("R_Elbow_FK_Ctrl", ws = True, t = Elbow_trans)

Wrist_rot = cmds.xform("R_Arm_IK_Ctrl", q = True, ws = True, ro = True)
cmds.xform("R_Wrist_FK_Ctrl", ws = True, ro = Wrist_rot)

Wrist_trans = cmds.xform("R_Arm_IK_Ctrl", q = True, ws = True, t = True)
cmds.xform("R_Wrist_FK_Ctrl", ws = True, t = Wrist_trans)
#---------------------------------------------------------------------------
#----------------------------SCRIPT04---------------------------------------
import maya.cmds as cmds
#script to set from IK to FK (right arm)

Elbow_rot = cmds.xform("R_Elbow_FK_Ctrl", q = True, ws = True, ro = True)
cmds.xform("R_Elbow_IK_Ctrl", ws = True, ro = Elbow_rot)

Elbow_trans = cmds.xform("R_Elbow_FK_Ctrl", q = True, ws = True, t = True)
cmds.xform("R_Elbow_IK_Ctrl", ws = True, t = Elbow_trans)

Wrist_rot = cmds.xform("R_Wrist_FK_Ctrl", q = True, ws = True, ro = True)
cmds.xform("R_Arm_IK_Ctrl", ws = True, ro = Wrist_rot)

Wrist_trans = cmds.xform("R_Wrist_FK_Ctrl", q = True, ws = True, t = True)
cmds.xform("R_Arm_IK_Ctrl", ws = True, t = Wrist_trans)
#---------------------------------------------------------------------------