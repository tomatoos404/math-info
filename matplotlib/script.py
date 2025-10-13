# from pylab import *

# y = [3,7,7,3,3]
# x = [3,3,7,7,3]
# plot(x,y)
# show()
# figure 2 le carré


# from pylab import *
# x = []
# y = []
# for i in range(5,16):
#     y.append(3)
#     x.append(i)
# plot(x,y,'r*')
# show()
# figure 2


# from pylab import *
# x = []
# y = []
# for z in range(5,16):
#     if len(x) == len(y):
#         for i in range(5,16):
#           y.append(5)
#           x.append(i)
#     y.append(3)
#     x.append(z)
# plot(x,y,'r*')
# show()
# figure 3


from pylab import *
x = []
y = []
for z in range(5,16):
    if len(x) == len(y):
        for i in range(5,16):
          y.append(5)
          x.append(i)
    y.append(3)
    x.append(z)
plot(x,y,'r*')
show()
# figure 4