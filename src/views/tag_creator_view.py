from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        respnsobality for interact with http
    '''
    
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]
        
        print('test')
        
        return HttpResponse(status_code=200, body ={"hello": "world"})