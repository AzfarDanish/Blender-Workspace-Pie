from bpy.props import *
from bpy.types import PropertyGroup


class Properties(PropertyGroup):

    # Workspaces
    compositing : BoolProperty(default=True)
    geometry_nodes : BoolProperty(default=True)
    layout : BoolProperty(default=True)
    scripting : BoolProperty(default=True)
    sculpting : BoolProperty(default=True)
    shading : BoolProperty(default=True)
    texture_paint : BoolProperty(default=True)
    uv_editing : BoolProperty(default=True)
    animation : BoolProperty(default=False)
