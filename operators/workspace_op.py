import bpy
from bpy.props import StringProperty

class Workspace_OT_Operator(bpy.types.Operator):
    bl_idname = "object.workspaces"
    bl_label = "workspace"
    bl_description = '''Workspace
    
Ctrl  -  Add Workspace'''

    Workspace: StringProperty(name='workspace', default="Animation")

    def invoke(self, context, event):
        if not event.ctrl:
            if self.Workspace in bpy.data.workspaces:
                context.window.workspace = bpy.data.workspaces[self.Workspace]
                return {'FINISHED'}
            else:
                self.report({'WARNING'}, "No workspace found")
                return {'CANCELLED'}
        if event.ctrl:
            bpy.ops.workspace.append_activate(
                idname=self.Workspace,
                filepath= '<startup.blend>')
            
        return {'FINISHED'}
