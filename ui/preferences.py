import rna_keymap_ui
from bpy.types import AddonPreferences
from bpy.props import EnumProperty
from . keymap import *
from .. import bl_info

class AddonPreferences(AddonPreferences):
    bl_idname = __name__.partition('.')[0]

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        self.draw_general(context, box)

    def draw_general(self, context, box):
        scene = context.scene
        prop = scene.properties
        # box = box.box()
        split = box.split(align=False,factor=0.4)
        box = split.box()
        col = box.column(align=True)
        col.scale_y = 1.1
        col.label(text='Workspaces', icon='WORKSPACE')
        col.prop(prop, 'compositing', text='Compositing', toggle=True, icon='NODE_COMPOSITING')
        col.prop(prop, 'geometry_nodes', text='Geometry Nodes', toggle=True, icon='NODETREE')
        col.prop(prop, 'layout', text='Layout', toggle=True, icon='OBJECT_DATAMODE')
        col.prop(prop, 'scripting', text='Scripting', toggle=True, icon='FILE_SCRIPT')
        col.prop(prop, 'sculpting', text='Sculpting', toggle=True, icon='SCULPTMODE_HLT')
        col.prop(prop, 'shading', text='Shading', toggle=True, icon='NODE_MATERIAL')
        col.prop(prop, 'texture_paint', text='Texture Paint', toggle=True, icon='TPAINT_HLT')
        col.prop(prop, 'uv_editing', text='UV Editing', toggle=True, icon='UV')
        col.prop(prop, 'animation', text='Animation', toggle=True, icon='RENDER_ANIMATION')

        box = split.column()
        self.draw_changelog(box)

        box.separator()

        box = box.box()
        self.draw_keymap(box)

    def draw_keymap(self, box):
        box.label(text="Keymap List:",icon="KEYINGSET")
        wm = bpy.context.window_manager
        kc = wm.keyconfigs.user
        old_km_name = ""
        get_kmi_l = []
        for km_add, kmi_add in addon_keymaps:
            for km_con in kc.keymaps:
                if km_add.name == km_con.name:
                    km = km_con
                    break

            for kmi_con in km.keymap_items:
                if kmi_add.idname == kmi_con.idname:
                    if kmi_add.name == kmi_con.name:
                        get_kmi_l.append((km,kmi_con))

        get_kmi_l = sorted(set(get_kmi_l), key=get_kmi_l.index)

        for km, kmi in get_kmi_l:
            if not km.name == old_km_name:
                box.label(text=str(km.name),icon="DOT")
            box.context_pointer_set("keymap", km)
            rna_keymap_ui.draw_kmi([], kc, km, kmi, box, 0)
            old_km_name = km.name

    def draw_changelog(self,box):
        changelog = [
            "Bugs Fix",
            "Press ctrl to add workspace"
        ]
        if changelog:
            box = box.box()
            version = str(bl_info['version'])[1:-1].replace(",",".").replace(" ","")
            box.label(text=f"Changelog for v{version}:")
            col = box.column(align=True)
            col.enabled = True
            for entry in changelog:
                col.label(text="   • " + entry)
