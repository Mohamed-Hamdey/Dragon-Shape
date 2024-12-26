"""
Module: __init__

This module initializes the `assets` package by exposing commonly used
data structures like vertices, edges, colors, and polygons for easy import.

Exports:
    vertices (dict): Defines the vertices for the rendering system.
    edges (list): Defines the edges connecting the vertices.
    colors (list): Defines the colors used for rendering polygons.
    polygons (list): Defines the polygons formed by groups of vertices.
"""
from .vertices import vertices
from .edges import edges
from .colors import colors
from .polygons import polygons