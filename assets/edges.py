"""
Module: edges

This module defines a list of edges for the rendering system.
Each edge is represented as a tuple of vertex labels, indicating
a connection between two vertices.

Edges are used to construct the geometric structure by connecting
the vertices in a meaningful way.

Attributes:
    edges (list): A list of tuples where each tuple contains two
    vertex labels (str) representing an edge between them.

Example:
    [
        ('C', 'P'),
        ('C', 'Z2'),
        ...
    ]
"""
edges = [
    ('C', 'P'),
    ('C', 'Z2'),
    ('P', 'Q'),
    ('D', 'Z2'),
    ('Z2', 'Q'),
    ('P1', 'R1'),
    ('T', 'G1'),
    ('F1', 'Q1'),
    ('G', 'P'),
    ('O', 'N'),
    ('Q', 'S'),
    ('N', 'T'),
    ('N', 'M'),
    ('H', 'N'),
    ('W2', 'K'),
    ('H', 'W2'),
    ('W2', 'I'),
    ('I', 'K'),
    ('K', 'J'),
    ('K', 'M'),
    ('J', 'L'),
    ('L', 'M'),
    ('L', 'H2'),
    ('M', 'U'),
    ('M', 'T'),
    ('S', 'T'),
    ('S', 'R'),
    ('O', 'G'),
    ('E', 'B1'),
    ('E', 'A1'),
    ('A1', 'B1'),
    ('B1', 'C1'),
    ('A1', 'R'),
    ('R', 'C1'),
    ('C1', 'F1'),
    ('R', 'D1'),
    ('D1', 'A3'),
    ('D1', 'E1'),
    ('E1', 'F1'),
    ('E1', 'G1'),
    ('G1', 'H1'),
    ('A3', 'F1'),
    ('F1', 'H1'),
    ('H1', 'I1'),
    ('Q1', 'R1'),
    ('Q1', 'O1'),
    ('O1', 'F'),
    ('F', 'P1'),
    ('O1', 'P1'),
    ('R1', 'T1'),
    ('T1', 'S1'),
    ('T1', 'I1'),
    ('I1', 'J1'),
    ('J1', 'N2'),
    ('J1', 'K1'),
    ('K1', 'L1'),
    ('G1', 'L1'),
    ('L1', 'N1'),
    ('N1', 'W'),
    ('N1', 'M1'),
    ('K1', 'L2'),
    ('L2', 'M2'),
    ('M1', 'L2'),
    ('M1', 'V'),
    ('V', 'W'),
    ('U', 'W'),#102
    ('U', 'Z'),
    ('V', 'J2'),
    ('J2', 'I2'),
    ('J2', 'Z'),
    ('Z', 'H2'),
    ('H2', 'G2'),
    ('G2', 'I2'),
    ('G2', 'F2'),
    ('F2', 'H2'),
    ('F2', 'E2'),
    ('E2', 'D2'),
    ('D2', 'B2'),
    ('B2', 'C2'),
    ('D2', 'C2'),
    ('U1', 'D2'),
    ('U1', 'S1'),
    ('S1', 'O2'),
    ('N2', 'M2'),
    ('P2', 'O2'),#103
    ('N2', 'O2'),
    ('P2', 'Q2'),
    ('M2', 'P2'),
    ('K2', 'L2'),
    ('K2', 'Q2'),
    ('Q2', 'L2'),
    ('Q2', 'R2'),
    ('R2', 'S2'),
    ('T2', 'U2'),
    ('V2', 'U2'),
    ('Q2', 'S2'),
    ('S2', 'T2'),
    ('T2', 'V2'),
    ('V2', 'C2'),#104
    ('S1', 'A2'),
    ('A2', 'V1'),#105
    ('W1', 'V1'),
    ('A2', 'Z1'),
    ('Z1', 'W1'),
    ('W1', 'C2'),
    ('R', 'D'),
    ('P','O'),
    ('O','H'),
    ('Q','R'),
    ('I2','K2')
]