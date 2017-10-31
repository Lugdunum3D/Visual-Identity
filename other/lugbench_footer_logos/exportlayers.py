#!/usr/bin/env python

"""
Export selected layers from Inkscape SVG.
"""

from xml.dom import minidom
import codecs


def export_layers(src, dest, select):
    """
    Export selected layers of SVG in the file `src` to the file `dest`.

    :arg  str    src:  path of the source SVG file.
    :arg  str   dest:  path to export SVG file.
    :arg  str select:  layers to select.

    """
    svg = minidom.parse(open(src))
    for g in svg.getElementsByTagName("g"):
        if g.getAttribute("inkscape:groupmode") == "layer":
            if g.getAttribute("inkscape:label") != select:
                g.parentNode.removeChild(g)
    export = svg.toxml()
    codecs.open(dest, "w", encoding="utf8").write(export)


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('select', help='layer to show.')
    parser.add_argument('src', help='source SVG file.')
    parser.add_argument('dest', help='path to export SVG file.')
    args = parser.parse_args()
    export_layers(**vars(args))


if __name__ == '__main__':
    main()
