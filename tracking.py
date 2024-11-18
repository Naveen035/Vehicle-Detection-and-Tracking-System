import math

class find_eucledian_dist:
    #Storing or initilizing the center and id 
    def __init__(self):
        self.center_points = {}
        self.id_count = 0
    
    def update(self,rect):
        #storing the boundaries
        object_boundries = []
        for r in rect:
            x,y,h,w = r
            cx = (x+x+w)//2
            cy = (y+y+h)//2
            same_obj_detected = False
            for id,points in self.center_points.items():
                #finding the eucledian distance
                eucledian_dist = math.hypot(cx - points[0],cy - points[1])
                if eucledian_dist < 25:
                    self.center_points[id] = (cx,cy)
                    print(self.center_points)
                    object_boundries.append([x,y,w,h,id])
                    same_obj_detected = True
            if same_obj_detected is False:
                self.center_points[self.id_count] = (cx,cy) 
                object_boundries.append([x,y,w,h,self.id_count])
                self.id_count += 1
        new_center_points = {}
        for id in object_boundries:
            _,_,_,_,object_id = id
            center = self.center_points[object_id]
            new_center_points[object_id] = center
        self.center_points = new_center_points.copy()
        return object_boundries

