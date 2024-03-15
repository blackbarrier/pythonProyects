import copy
import random

class Hat:
    def __init__(self, **dict):
        L=[]
        for item in dict:
            for color in range(dict[item]):
                color=item
                L.append(color)
        self.contents = L
    
    def draw(self, n):
        L=[]
        if n <= len(self.contents):
            max_index=len(self.contents)-1       
            for _ in range(n):
                x = random.randint(0, max_index)   
                L.append(self.contents.pop(x))
                max_index-=1
            return L
        else:
            return (self.contents)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    M=0

    #Iteration
    for _ in range(num_experiments):
        aux = copy.deepcopy(hat)            

        # Draw  
        draw=(aux.draw(num_balls_drawn)) 
        dict_draw = {}
        for color in draw:
            if color in dict_draw:
                dict_draw[color] += 1
            else:
                dict_draw[color] = 1

        #Comparation        
        color_coincidence=True
        for color in expected_balls:            
            if not color in dict_draw:
                color_coincidence=False        
    
        min_cant=True
        if color_coincidence:
            for color in expected_balls:
                if expected_balls[color]>dict_draw[color]:
                    min_cant=False  

        #Favorable cases    
        if min_cant==True and color_coincidence==True:
            M+=1

    prob =  M/num_experiments
    
    return(prob)
   
    


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)