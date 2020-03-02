from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 100, 100, 255]
edges = []
transform = new_matrix()

parse_file( 'script2', edges, transform, screen, color )
