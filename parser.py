from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    s = f.readlines()
    for i in range(len(s)):
        s[i] = s[i].strip()
    for i in range(len(s)):
        if s[i] == "line":
            args = s[i+1].split(" ")
            add_edge(points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
        if s[i] == "scale":
            #print "scale"
            args = s[i + 1].split(" ")
            scaleM = make_scale(int(args[0]), int(args[1]), int(args[2]))
            matrix_mult(scaleM, transform)
        if s[i] == "move":
            #print "move"
            args = s[i + 1].split(" ")
            translateM = make_translate(int(args[0]), int(args[1]), int(args[2]))
            matrix_mult(translateM, transform)
        if s[i] == "rotate":
            args = s[i + 1].split(" ")
            #print args[0]
            if args[0] == "x":
                #print "rotate x"
                rotX = make_rotX(int(args[1]))
                matrix_mult(rotX, transform)
            if args[0] == "y":
                #print "rotate y"
                rotY = make_rotY(int(args[1]))
                matrix_mult(rotY, transform)
            if args[0] == "z":
                #print "rotate z"
                rotZ = make_rotZ(int(args[1]))
                matrix_mult(rotZ, transform)
        if s[i] == "ident":
            #print "ident"
            identM = new_matrix()
            ident(identM)
            transform = identM
        if s[i] == "apply":
            #print "apply"
            matrix_mult(transform, points)
        if s[i] == "display":
            clear_screen(screen)
            #print points
            draw_lines(points, screen, color)
            display(screen)
        if s[i] == "save":
            args = s[i + 1]
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_ppm(screen, "image.ppm")
            save_extension(screen, args)
    #print points
