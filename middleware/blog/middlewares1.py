from django.shortcuts import HttpResponse

# class MyProcessMiddleWare:
# 	def __init__(self,get_response):
# 		self.get_response = get_response

# 	def __call__(self,request):
# 		response = self.get_response(request)
# 		return response

# 	def process_view(request,*args,**kwargs):
# 		print("This is process_view Before View")
# 		# return HttpResponse("This is Before View")
# 		return None


class MyExceptionMiddleWare:
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		response = self.get_response(request)
		return response

	def process_exception(self,request,exception):
		print("Exception Occured")
		msg = exception
		class_name = exception.__class__.__name__
		print(class_name)
		print(msg)
		return HttpResponse(msg)


class MyTemplateResponseMiddleWare:
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		response = self.get_response(request)
		return response

	def process_template_response(self,request,response):
		print("Process Templates Response From Middleware")
		response.context_data['name'] = 'Sandhya'
		return response