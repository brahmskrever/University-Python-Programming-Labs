##########################################
# APS106 W2021 - Lab 6 - Corner Detector #
##########################################

#from lab6_image_utils import display_image, image_to_pixels # UNCOMMENT this line to use the load/display image utils
from operator import itemgetter

################################################
# PART 0 - Helper Functions        #
################################################
def OneD_to_TwoD(img, width, height):
    last = 0
    matrix = []
    for i in range(len(img)):
        if (i%height == 0 and i!=0):
            matrix.append(list(img[last:(i)]))
            last = i
    matrix.append(list(img[-1*height:]))
    return matrix

def Kernel_Product(kernel,matrix):
    Dot_Sum = []
    for i in range(len(kernel)):
        for j in range(len(kernel[0])):
            Dot_Sum.append(kernel[i][j] * matrix[i][j])
    
    return(int(sum(Dot_Sum)))

def TwoD_to_OneD(matrix):
    Empty = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            Empty.append(matrix[i][j])
    
    return Empty

def Euclidean_distance (List_A,List_B):
    Sum = ((List_A[0]-List_B[0])**2 + (List_A[1]-List_B[1])**2)**(1/2)
    return Sum

def Add_Zeros (List):
    zeros =[]
    for i in range(len(List)):
        List[i].insert(0,0)
        List[i].insert(len(List)+2,0)
    for n in range(len(List[0])):
        zeros.append(0)
    List.insert(0,zeros)
    List.insert(len(List)+1,zeros)
    
    return(List)
    
################################################
# PART 1 - RGB to Grayscale Conversion         #
################################################
def rgb_to_grayscale(rgb_img):
    """
    (list) -> list
    
    Function converts an image of RGB pixels to grayscale.
    Input list is a nested list of RGB pixels.
    
    The intensity of a grayscale pixel is computed from the intensities of
    RGB pixels using the following equation
    
        grayscale intensity = 0.3 * R + 0.59 * G + 0.11 * B
    
    where R, G, and B are the intensities of the R, G, and B components of the
    RGB pixel. The grayscale intensity should be rounded to the nearest
    integer.
    """
    Red=[]
    Green = []
    Blue = []
    Greyscale = []
    for i in range(len(rgb_img)):
        for j in range(len(rgb_img[i])):
            if(j==0):
                Red.append(rgb_img[i][j])
            elif(j==1):
                Green.append(rgb_img[i][j])
            else:
                Blue.append(rgb_img[i][j])
    
    for k in range(len(Red)):
        Greyscale.append(round(Red[k] * .3 + Green[k]*.59 + Blue[k]*.11))
    
    return(Greyscale)
             
    pass # TODO your code here


############################
# Part 2b - Dot Product    #
############################

def dot(x,y):
    """
    (List, List) -> float
    
    Performs a 1-dimensional dot product operation
    """
    Dot_Sum = 0.0
    for i in range(len(x)):
        Dot_Sum +=(x[i] * y[i])
    
    return (Dot_Sum)    

    # TODO your code here


######################################
# Part 2c - Extract Image Segment    #
######################################

def extract_image_segment(img, width, height, centre_coordinate, N):
    """
    (list, int, int, list, int) -> list
    
    Extracts a 2-dimensional NxN segment of a image centred around
    a given coordinate. The segment is returned as a list of pixels from the
    segment.
    
    img is a list of grayscale pixel values
    width is the width of the image
    height is the height of the image
    centre_coordinate is a two-element list defining a pixel coordinate
    N is the height and width of the segment to extract from the image
    
    """
    
    img = OneD_to_TwoD(img,width,height)
    matrix = []
    for i in range((centre_coordinate[1]-N//2),(centre_coordinate[1] -N//2 + N)):
        for j in range((centre_coordinate[0]-N//2),(centre_coordinate[0]  -N//2 + N)):
            matrix.append(img[i][j])
    
    return(matrix)
    
    
    pass # TODO your code here
    

######################################
# Part 2d - Kernel Filtering         #
######################################

def kernel_filter(img, width, height, kernel):
    """
    (list, int, int, list) -> list
    
    Apply the kernel filter defined within the two-dimensional list kernel to 
    image defined by the pixels in img and its width and height.
    
    img is a 1 dimensional list of grayscale pixels
    width is the width of the image
    height is the height of the image
    kernel is a 2 dimensional list defining a NxN filter kernel, n must be an odd integer
    
    The function returns the list of pixels from the filtered image
    """

    img = OneD_to_TwoD(img,height,height)
    MAT = []
    for i in range(1,height-1):
        for j in range(1,height-1):
            matrix = OneD_to_TwoD((extract_image_segment(TwoD_to_OneD(img),7,7,[j,i],3)),3,3)
            MAT.append(Kernel_Product(kernel, matrix))
    MAT= OneD_to_TwoD(MAT,height-1,height-1)
    print(MAT)  
    MAT = Add_Zeros(MAT)
    MAT= TwoD_to_OneD(MAT)
    return(MAT)


###############################
# PART 3 - Harris Corners     #
###############################

def harris_corner_strength(Ix,Iy):
    """
    (List, List) -> float
    
    Computes the Harris response of a pixel using
    the 3x3 windows of x and y gradients contained 
    within Ix and Iy respectively.
    
    Ix and Iy are  lists each containing 9 integer elements each.
    
    STUDENTS DO NOT NEED TO EDIT THIS FUNCTION

    """

    # calculate the gradients
    Ixx = [0] * 9
    Iyy = [0] * 9
    Ixy = [0] * 9
    
    for i in range(len(Ix)):
        Ixx[i] = (Ix[i] / (4*255))**2
        Iyy[i] = (Iy[i] / (4*255))**2
        Ixy[i] = (Ix[i] / (4*255) * Iy[i] / (4*255))
    
    # sum  the gradients
    Sxx = sum(Ixx)
    Syy = sum(Iyy)
    Sxy = sum(Ixy)
    
    # calculate the determinant and trace
    det = Sxx * Syy - Sxy**2
    trace = Sxx + Syy
    
    # calculate the corner strength
    k = 0.03
    r = det - k * trace**2
    
    return r

def harris_corners(img, width, height, threshold):
    """
    (list, int, int, float) -> list
    
    Computes the corner strength of each pixel within an image
    and returns a list of potential corner locations sorted from strongest
    to weakest.
    
    STUDENTS DO NOT NEED TO EDIT THIS FUNCTION
    """
    
    # perform vertical edge detection
    vertical_edge_kernel = [[-1, 0, 1],
                            [-2, 0, 2],
                            [-1, 0, 1]]
    Ix = kernel_filter(img, width, height, vertical_edge_kernel)
    
    # perform horizontal edge detection
    horizontal_edge_kernel = [[-1,-2,-1],
                              [ 0, 0, 0],
                              [ 1, 2, 1]]
    Iy = kernel_filter(img, width, height, horizontal_edge_kernel)
    
    # compute corner scores and identify potential corners
    offset = 1
    corners = []
    for i_y in range(offset, height-offset):
        for i_x in range(offset, width-offset):
            Ix_window = extract_image_segment(Ix, width, height, [i_x, i_y], 3)
            Iy_window = extract_image_segment(Iy, width, height, [i_x, i_y], 3)
            corner_strength = harris_corner_strength(Ix_window, Iy_window)
            if corner_strength > threshold:
                corners.append([corner_strength,[i_x,i_y]])

    # sort
    corners.sort(key=itemgetter(0))
    corner_locations = []
    for i in range(len(corners)):
        corner_locations.append(corners[i][1])

    return corner_locations


###################################
# PART 4 - Non-maxima Suppression #
###################################

def non_maxima_suppression(corners, min_distance):
    """
    (list, float) -> list
    
    Filters any corners that are within a region with a stronger corner.
    Returns a list of corners that are at least min_distance away from
    any other stronger corner.
    
    corners is a list of two-element coordinate lists representing potential
        corners as identified by the Harris Corners Algorithm. The corners
        are sorted from strongest to weakest.
    
    min_distance is a float specifying the minimum distance between any
        two corners returned by this function
    """
    F = []
    F.append(corners[0])
    
    
    for i in range(len(corners)):
        if(Euclidean_distance(F[i-1],corners[i]) >= min_distance):
            F.append(corners[i])
    
    return(F)
    
    pass # TODO your code here
    

