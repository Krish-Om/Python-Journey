# We can say that Python looks for object components in the following order:

# inside the object itself;
# in its superclasses, from bottom to top;
# if there is more than one class on a particular inheritance path, Python scans them from left to right.


class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left, Right): # the order in here decides which class to check first, in this case class "Left" is checked first
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())
    