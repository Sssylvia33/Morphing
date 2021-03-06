import cv2
import numpy as np
import random
from scipy.misc import imresize


# Check if a point is inside a rectangle
def rect_contains(rect, point) :
    if point[0] < rect[0] :
        return False
    elif point[1] < rect[1] :
        return False
    elif point[0] > rect[2] :
        return False
    elif point[1] > rect[3] :
        return False
    return True

# Draw a point
def draw_point(img, p, color ) :
    cv2.circle( img, p, 2, color, cv2.cv.CV_FILLED, cv2.CV_AA, 0 )


# Draw delaunay triangles
def draw_delaunay(img, subdiv, delaunay_color ) :

    triangleList = subdiv.getTriangleList();
    size = img.shape
    r = (0, 0, size[1], size[0])
    delaunayTri = []
    f = open('Tri.txt','w')

    for t in triangleList :
        pt = []
        pt.append((t[0], t[1]))
        pt.append((t[2], t[3]))
        pt.append((t[4], t[5]))
        
        pt1 = (t[0], t[1])
        pt2 = (t[2], t[3])
        pt3 = (t[4], t[5])
        
        if rect_contains(r, pt1) and rect_contains(r, pt2) and rect_contains(r, pt3) :
        
            cv2.line(img, pt1, pt2, delaunay_color, 1, cv2.CV_AA, 0)
            cv2.line(img, pt2, pt3, delaunay_color, 1, cv2.CV_AA, 0)
            cv2.line(img, pt3, pt1, delaunay_color, 1, cv2.CV_AA, 0)
            ind = []
            for j in xrange(0, 3):
                for k in xrange(0, 79):
                    if(abs(pt[j][0] - points[k][0]) < 1.0 and abs(pt[j][1] - points[k][1]) < 1.0):
                        ind.append(k)
            if len(ind) == 3:
                f.write('{} {} {} \n'.format(ind[0], ind[1], ind[2]))
                delaunayTri.append((ind[0], ind[1], ind[2]))
    f.close()
    return delaunayTri 


# Draw voronoi diagram
def draw_voronoi(img, subdiv) :

    ( facets, centers) = subdiv.getVoronoiFacetList([])

    for i in xrange(0,len(facets)) :
        ifacet_arr = []
        for f in facets[i] :
            ifacet_arr.append(f)
        
        ifacet = np.array(ifacet_arr, np.int)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        cv2.fillConvexPoly(img, ifacet, color, cv2.CV_AA, 0);
        ifacets = np.array([ifacet])
        cv2.polylines(img, ifacets, True, (0, 0, 0), 1, cv2.CV_AA, 0)
        cv2.circle(img, (centers[i][0], centers[i][1]), 3, (0, 0, 0), cv2.cv.CV_FILLED, cv2.CV_AA, 0)


if __name__ == '__main__':

    # Define window names
    win_delaunay = "Delaunay Triangulation"
    win_voronoi = "Voronoi Diagram"

    # Turn on animation while drawing triangles
    animate = True
    
    # Define colors for drawing.
    delaunay_color = (255,255,255)
    points_color = (0, 0, 255)

    # Read in the image.
    img = cv2.imread("./face/Rost.jpg");
    img = imresize(img,[600L,600L])
    
    # Keep a copy around
    img_orig = img.copy();
    
    # Rectangle to be used with Subdiv2D
    size = img.shape
    rect = (0, 0, size[1], size[0])
    
    # Create an instance of Subdiv2D
    subdiv = cv2.Subdiv2D(rect);

    # Create an array of points.
    points = [];
    
    # Read in the points from a text file
    with open("rostLandmarks.txt") as file :
        for line in file :
            x, y = line.split()
            points.append((int(x), int(y)))

    # Insert points into subdiv
    for p in points :
        subdiv.insert(p)
            
        ''''if animate : # Show animation
            img_copy = img_orig.copy()
            # Draw delaunay triangles
            draw_delaunay( img_copy, subdiv, (255, 255, 255) );
            cv2.imshow(win_delaunay, img_copy)
            cv2.waitKey(100)'''
    # Draw delaunay triangles
    delaunayTri = draw_delaunay( img, subdiv, (255, 255, 255) );

    # Draw points
    #f = open('savTri.txt','w')
    for p in points :
        draw_point(img, p, (0,0,255))

    # Allocate space for voronoi Diagram
    #img_voronoi = np.zeros(img.shape, dtype = img.dtype)

    # Draw voronoi diagram
    #draw_voronoi(img_voronoi,subdiv)
    
    

    # Show results
    cv2.imshow(win_delaunay,img)
    #cv2.imshow(win_voronoi,img_voronoi)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

