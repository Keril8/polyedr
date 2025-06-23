import unittest
from unittest.mock import patch, mock_open
from math import isclose, sqrt

from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr

tk = TkDrawer()


class TestPolyedr1(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	45.0	45.0	30.0
8	4	16
-0.5	-0.5	0.5
-0.5	0.5	0.5
0.5	0.5	0.5
0.5	-0.5	0.5
-0.5	-0.5	-0.5
-0.5	0.5	-0.5
0.5	0.5	-0.5
0.5	-0.5	-0.5
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5"""
        fake_file_path = 'data/holey_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 4)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 16)


class TestPolyedr2(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0 0.0 0.0 0.0
        8 2 8
        2.0 2.0 0.0
        2.0 3.0 0.0
        3.0 3.0 0.0
        3.0 2.0 0.0
        2.0 2.0 1.0
        2.0 3.0 1.0
        3.0 3.0 1.0
        3.0 2.0 1.0
        4 1 2 3 4
        4 5 6 7 8
"""
        

        fake_file_path = 'data/octahedron.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 2)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 8)
    
    def test_planes_1(self):
        self.assertEqual(self.polyedr.calculate(), 0.0)

class TestPolyedr3(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0 0.0 0.0 0.0
        8 2 8
        2.0 2.0 0.0
        2.0 4.0 0.0
        4.0 4.0 0.0
        4.0 2.0 0.0
        3.0 1.0 1.0
        3.0 3.0 1.0
        5.0 3.0 1.0
        5.0 1.0 1.0
        4 1 2 3 4
        4 5 6 7 8
"""
        

        fake_file_path = 'data/octahedron.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 2)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 8)
    
    def test_planes_2(self):
        self.assertEqual(self.polyedr.calculate(), 400.0)

class TestPolyedr4(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """20.0 0.0 0.0 0.0
        8 2 8
        -1.5 0.0 0.0
        -1.5 2.0 0.0
        0.5 2.0 0.0
        0.5 0.0 0.0
        -0.5 -1.0 1.0
        -0.5 1.0 1.0
        1.5 1.0 1.0
        1.5 -1.0 1.0
        4 1 2 3 4
        4 5 6 7 8
"""
        

        fake_file_path = 'data/octahedron.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 2)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 8)
    
    def test_planes_3(self):
        self.assertEqual(self.polyedr.calculate(), 20.0)
