class Rectangle:
	def __init__(self, length, width):
		self.l = int(length)
		self.w = int(width)
	def __str__(self):
		rect = []
		for i in range(self.l):
			rect.append(self.w * self.l)
		rect = '\n'. join(rect)
		return rect


b = Rectangle(10, 3, '*')
print(b)





# class Rectangle:
#     def __init__(self, width, height, sign):
#         self.w = int(width)
#         self.h = int(height)
#         self.s = str(sign)
#     def __str__(self):
#         rect = []
#         for i in range(self.h):
#             rect.append(self.s * self.w) 
#         rect = '\n'.join(rect) 
#         return rect
 
# b = Rectangle(10, 3, '*')
# print(b)