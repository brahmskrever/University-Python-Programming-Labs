##############################
# APS106 Winter 2021 - Lab 4 #
##############################

def rectangle_overlap(rect1_bl_x,rect1_bl_y,
                      rect1_tr_x,rect1_tr_y,
                      rect2_bl_x,rect2_bl_y,
                      rect2_tr_x,rect2_tr_y):

    if  ((rect1_bl_x,rect1_bl_y,rect1_tr_x,rect1_tr_y) == (rect2_bl_x,rect2_bl_y,rect2_tr_x,rect2_tr_y)):
        return "identical coordinates"
    elif (((rect1_bl_x,rect1_bl_y) < (rect2_bl_x,rect2_bl_y)) and ((rect1_tr_x,rect1_tr_y) > (rect2_tr_x,rect2_tr_y))):
        return 'rectangle 2 is contained within rectangle 1'
    elif (((rect1_bl_x,rect1_bl_y) > (rect2_bl_x,rect2_bl_y)) and ((rect1_tr_x,rect1_tr_y) < (rect2_tr_x,rect2_tr_y))):
        return  'rectangle 1 is contained within rectangle 2'
    elif(((rect1_tr_y > rect2_bl_y) and (rect1_tr_y < rect2_tr_y)) and ((rect1_tr_x > rect2_bl_x) and (rect1_tr_x < rect2_tr_x)) or ((rect1_tr_y < rect2_bl_y) and (rect1_tr_y > rect2_tr_y)) and ((rect1_tr_x < rect2_bl_x) and (rect1_tr_x > rect2_tr_x))):
        return 'rectangles overlap'
    else:
        return 'no overlap'

