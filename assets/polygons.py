"""
Module: polygons

This module defines a list of polygons for the rendering system.
Each polygon is represented as a list of vertex labels that form
the polygon's boundary.

Polygons are used in rendering to create filled shapes that enhance
the visual representation of the object.

Attributes:
    polygons (list): A list of lists, where each inner list contains
    vertex labels (str) defining a polygon.

Example:
    [
        ['N2', 'M2', 'P2', 'O2'],  # A polygon with four vertices
        ['A2', 'Z1', 'W1', 'V1'],  # Another polygon with four vertices
        ...
    ]
"""
polygons = [
    ['N2', 'M2', 'P2', 'O2'],
    ['A2', 'Z1', 'W1', 'V1'],
    ['G1', 'H1', 'F1', 'E1'],
    ['E1', 'F1', 'A3', 'D1'],
    ['F1', 'H1', 'I1', 'T1', 'R1', 'Q1'],
    ['D1', 'A3', 'C1', 'R'],
    ['R', 'C1', 'B1', 'A1'],
    ['R1', 'Q1', 'O1', 'P1'],
    ['E', 'A1', 'B1'],
    ['F', 'O1', 'P1'],
    ['S1', 'U1', 'D2', 'C2', 'W1', 'V1', 'A2'],
    ['D', 'Z2', 'Q', 'R'],
    ['Z2', 'C', 'P', 'Q'],
    ['P', 'G', 'O'],
    ['O', 'H', 'N'],
    ['W2', 'I', 'K'],
    ['M', 'K', 'J', 'L'],
    ['R', 'Q', 'S'],
    ['Q', 'P', 'O', 'N', 'T', 'S'],
    ['T', 'M', 'N'],
    ['N', 'H', 'W2', 'K', 'M'],
    ['R', 'S', 'T', 'G1', 'E1', 'D1'],
    ['G1', 'T', 'M', 'U', 'W', 'N1', 'L1'],
    ['U', 'M', 'L', 'H2'],
    ['K1', 'L1', 'N1', 'M1', 'L2'],
    ['N1', 'M1', 'V', 'W'],
    ['V', 'W', 'U', 'Z', 'J2'],
    ['L2', 'M1', 'V', 'J2', 'I2', 'K2'],
    ['I2', 'J2', 'Z', 'H2', 'G2'],
    ['G2', 'H2', 'F2'],
    ['K2', 'I2', 'G2', 'F2', 'E2', 'D2', 'B2', 'C2', 'V2', 'U2', 'T2', 'S2', 'R2', 'Q2'],
    ['Q2', 'R2', 'S2'],
    ['T2', 'U2', 'V2'],
    ['C2', 'B2', 'D2'],
    ['H1', 'G1', 'L1', 'K1', 'J1', 'I1'],
    ['J1', 'K1', 'L2', 'M2', 'N2'],
    ['M2', 'L2', 'K2', 'Q2', 'P2'],
    ['T1', 'I1', 'J1', 'N2', 'O2', 'S1'],
    ['S1', 'O2', 'P2', 'Q2', 'S2', 'T2', 'V2', 'C2', 'W1', 'Z1', 'A2'],
    ['A2', 'Z1', 'W1', 'V1']
]