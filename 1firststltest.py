import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# your_mesh = mesh.Mesh.from_file('/home/clayton/cubo.stl')
your_mesh = mesh.Mesh.from_file('/home/clayton/Documentos/3D_Diff/models/modelos_cascavel/cascavelasc.stl')
# your_mesh = mesh.Mesh.from_file('/home/clayton/Vídeos/cilindroconefinalascii2.stl')
# your_mesh = mesh.Mesh.from_file('/home/clayton/Vídeos/cilindrofreecadfinalascii2.stl')
# your_mesh = mesh.Mesh.from_file('/home/clayton/Vídeos/conefinalascii.stl')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

scale = your_mesh.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)

pyplot.show()
