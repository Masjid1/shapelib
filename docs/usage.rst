========
Usage
========

To use shapelib in a project::

	import shapelib
    # create a line perpendicular to another
    l = shapelib.line(0, 0, 0, 1)
    perp = shapelib.perpendicular_at(l, (0, 0.5), 2)

    # rotate a geometry
    rot = shapelib.rotate(l, 45)

    # convert a geometry to an 2D array
    img = shapelib.rasterize(l)

    