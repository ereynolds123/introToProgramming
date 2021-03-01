# # draw 3 triangles before functions
# 
# # draw a triangle
# # print two spaces, 1 *
# print("  *")
# # print one space, 3*
# print(" ***")
# # print 5*
# print("*****")
# 
# # draw another triangle
# # print two spaces, 1 *
# print("  *")
# # print one space, 3*
# print(" ***")
# # print 5*
# print("*****")
# 
# # draw another triangle
# # print two spaces, 1 *
# print("  *")
# # print one space, 3*
# print(" ***")
# # print 5*
# print("*****")

# A function that can draw triangle
def draw():
    print("  *")
    print(" ***")
    print("*****")
# 
# drawTriangle()
# drawTriangle()
# drawTriangle()
#     
# #you could also make a drawThreeTriangles function and call it once. 

#For loop
def drawThreeTriangles():
    amountToDraw = int(input("How many triangles would you like to draw: "))
    for index in range(amountToDraw):
        draw()
        
drawThreeTriangles()