class RequestLogMilddleWare:

    def __init__(self, get_response):
        self.get_response = get_response
        # get_response is the next middleware or view

    def __call__(self, request):
        # code before view(requestphase)
        print("Requested Path: ", request.path)

        response = self.get_response(request)
        # call the next middleware/view

        # code after view (response phase)
        print("Response Status Code: ",response.status_code)

        return response