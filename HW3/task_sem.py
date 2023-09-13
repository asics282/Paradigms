class Shape:
    def get_area(self):
        pass


    def get_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        # super().__init__(r)
        self.r = int(r)


    def get_area(self):
        return 3.14*self.r**2
        

    def get_perimeter(self):
        return 2*3.14*self.r
    

circul1 = Circle(3)
print('Площадь: ',circul1.get_area())
print('Периметр: ', circul1.get_perimeter())


class Triangle(Shape):
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3


    def get_perimeter(self, s1, s2, s3):
        return s1+s2+s3
    

    def get_area(self, s1, s2, s3):
        p = (s1 + s2 + s3)/2
        return (p*(p - s1)*(p - s2)*(p - s3))**0.5 #теорема Герона
    

tri = Triangle(2, 3, 4)
print('Периметр треугольника: ', tri.get_perimeter(2, 3, 4))
print('Площадь треугольника: ', tri.get_area(2, 3, 4))

# про гетеры и сеттеры
class A:
    __m = 55

    @property
    def m(self):
        return self.__m

    @m.setter
    def m(self, value):
        if isinstance(value, int) and value > 0:
            self.__m = value
        else:
            self.__m = value

    @m.getter
    def m(self):
        return self._m1


a = A()

a.m = 13

print(a.m)