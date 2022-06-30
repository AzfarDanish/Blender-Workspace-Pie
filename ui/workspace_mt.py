from bpy.types import Menu


class Workspace_MT_Menu(Menu):
    bl_idname = "workspace_mt_menu"
    bl_label = 'Workspaces'

    def draw(self, context):
        scene = context.scene
        prop = scene.properties

        layout = self.layout

        pie = layout.menu_pie()
        if prop.compositing == True:
            pie.operator('object.workspaces', text="Compositing", icon="NODE_COMPOSITING").Workspace = "Compositing"
        if prop.layout == True:
            pie.operator('object.workspaces', text="Layout", icon="OBJECT_DATAMODE").Workspace = "Layout"
        if prop.sculpting == True:
            pie.operator('object.workspaces', text="Sculpting", icon="SCULPTMODE_HLT").Workspace = "Sculpting"
        if prop.shading == True:
            pie.operator('object.workspaces', text="Shading", icon="NODE_MATERIAL").Workspace = "Shading"
        if prop.texture_paint == True:
            pie.operator('object.workspaces', text="Texture Paint", icon="TPAINT_HLT").Workspace = "Texture Paint"
        if prop.uv_editing == True:
            pie.operator('object.workspaces', text="UV Editing", icon="UV").Workspace = "UV Editing"
        if prop.geometry_nodes == True:
            pie.operator('object.workspaces', text="Geometry Nodes", icon="NODETREE").Workspace = "Geometry Nodes"
        
        if (prop.compositing and prop.layout and prop.sculpting and prop.shading and prop.texture_paint and prop.uv_editing and prop.geometry_nodes) == False:
            if prop.animation == True:
                pie.operator('object.workspaces', text="Animation", icon="RENDER_ANIMATION").Workspace = "Animation"
            if prop.scripting == True:
                    pie.operator('object.workspaces', text="Scripting", icon="FILE_SCRIPT").Workspace = "Scripting"
        else:
            box = pie.box()
            col = box.column(align=True)
            row = col.row(align=True)
            row.scale_y=1.3
            if prop.animation == True:
                row.operator('object.workspaces', text="Animation", icon="RENDER_ANIMATION").Workspace = "Animation"
            if prop.scripting == True:
                row.operator('object.workspaces', text="Scripting", icon="FILE_SCRIPT").Workspace = "Scripting"
        