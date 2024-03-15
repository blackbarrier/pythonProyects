class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width=width

    def set_height(self, height):
        self.height=height
    
    def get_area(self):
        return (self.width*self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):        
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture=""
        if not self.width>50 or self.height>50 :
            for line in range(self.height):
                picture+=("*"*self.width+"\n")
        else:
            picture="Too big for picture."
        return picture

    def get_amount_inside(self, shape):
        if self.width>=shape.width and self.height>=shape.height:
            amountWidth=self.width//shape.width
            amountHight=self.height//shape.height
            total=amountWidth*amountHight            
        else:
            total=0

        return total

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self,side,side)
        self.side=side
    
    def __str__(self):
        pass
        return f"Square(side={self.side})"
    
    def set_side(self, side):
        self.side=side
        self.width=side
        self.height=side
    
    def set_width(self, side):
        self.side=side

    def set_height(self, side):
        self.side=side