import bpy

addon_keymaps = []

def _keymap():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    km = kc.keymaps.new(name="Window", space_type="EMPTY")
    kmi = km.keymap_items.new("wm.call_menu_pie",
                                type= "W",
                                value= "PRESS",
                                repeat= False,
                                ctrl=False,
                                alt=True,
                                shift=False)
    kmi.properties.name = "workspace_mt_menu"
    addon_keymaps.append((km, kmi))

def register_keymap():
    _keymap()

def unregister_keymap():
    for km,kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
