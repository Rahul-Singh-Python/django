from django.shortcuts import HttpResponse

# # Function Based Middleware

# # One Time Hi Initilization hoga server me
# def my_middleware(get_response):
# 	print("One Time Initilization")
# 	def my_function(request):
# 		print("This is Before View.")
# 		response = get_response(request)
# 		print("This is After View")
# 		return response
# 	return my_function




# Class Based Middleware

# # One Time Hi Initilization hoga server me
# class my_middleware:
# 	def __init__(self,get_response):
# 		self.get_response = get_response
# 		print("One Time Initilization")

# 	def __call__(self,request):
# 		print("This is Before View")
# 		response = self.get_response(request)
# 		print("This is After View")
# 		return response



# # More than middleware 
# class BrotherMiddelware:
# 	def __init__(self,get_response):
# 		self.get_response = get_response
# 		print("One Time Brother Initilization")

# 	def __call__(self,request):
# 		print("This is Brother Before View")
# 		response = self.get_response(request)
# 		print("This is Brother After View")
# 		return response

# class FatherMiddelware:
# 	def __init__(self,get_response):
# 		self.get_response = get_response
# 		print("One Time Father Initilization")

# 	def __call__(self,request):
# 		print("This is Father Before View")
# 		response = self.get_response(request)
# 		print("This is Father After View")
# 		return response

# class MummyMiddelware:
# 	def __init__(self,get_response):
# 		self.get_response = get_response
# 		print("One Time Mummy Initilization")

# 	def __call__(self,request):
# 		print("This is Mummy Before View")
# 		response = self.get_response(request)
# 		print("This is Mummy After View")
# 		return response




# Three Middleware me nhi jana hai sirf do hi me jana hai
class BrotherMiddelware:
	def __init__(self,get_response):
		self.get_response = get_response
		print("One Time Brother Initilization")

	def __call__(self,request):
		print("This is Brother Before View")
		response = self.get_response(request)
		print("This is Brother After View")
		return response

class FatherMiddelware:
	def __init__(self,get_response):
		self.get_response = get_response
		print("One Time Father Initilization")

	def __call__(self,request):
		print("This is Father Before View")
		response = HttpResponse('Get out')
		print("This is Father After View")
		return response

class MummyMiddelware:
	def __init__(self,get_response):
		self.get_response = get_response
		print("One Time Mummy Initilization")

	def __call__(self,request):
		print("This is Mummy Before View")
		response = self.get_response(request)
		print("This is Mummy After View")
		return response

