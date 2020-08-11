from gl import Render, color, V2, V3
from obj import Obj, Texture
from shaders import *

r = Render()
r.glCreateWindow(1000,1000)

#r.active_texture = Texture('./models/earth.bmp')
r.active_texture = Texture('./models/model.bmp')

r.active_shader = gourad

#r.glLoadModel('./models/earth.obj', V3(500,500,0), V3(1,1,1))
r.glLoadModel('./models/model.obj',V3(500,500,0), V3(300,300,300))

r.glFinish('output.bmp')
