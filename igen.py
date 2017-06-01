import urllib.request
import json

global ACCESS_TOKEN
global BASE_URL
global HEADERS

def create_intent(name,msg,response):
    return {
        'name' : name,
        'auto' : True,
        'contexts' : [],
        'templates' : [],
        'userSays' : [
                {
                    'data' : [
                            {
                                'text' : msg
                            }
                        ],
                        'isTemplate' : False,
                        'count' : 0
                }
            ],
        'responses' : [
                {
                    'resetContexts' : False,
                    'action' : '',
                    'affectedContexts' : [],
                    'parameters' : [],
                    'speech' : response
                }
            ],
            'priority' : 500000
    }
    
def post_intent(name,msg,response):
    global BASE_URL
    global HEADERS
    
    intentJson = create_intent(name,msg,response)
    data = json.dumps(intentJson).encode('utf8')
    
    req = urllib.request.Request(BASE_URL+'intents',data,HEADERS)
    response = urllib.request.urlopen(req)
    print(response.read())
    
    

def get_intent(intentId):
    global BASE_URL
    global HEADERS
    
    req = urllib.request.Request(BASE_URL+'intents'+intentId,headers=HEADERS)
    response = urllib.request.urlopen(req)
    
    return response.read()

def get_intents():
    global BASE_URL
    global HEADERS
    
    req = urllib.request.Request(BASE_URL+'intents',headers=HEADERS)
    response = urllib.request.urlopen(req)
    
    return response.read()
    

def lambda_handler(event, context):
    global ACCESS_TOKEN
    global BASE_URL
    global HEADERS
    
    ACCESS_TOKEN = '30fe3ab64d6c4acf9fdf6e0085d7c650'
    BASE_URL = 'https://api.api.ai/v1/'
    HEADERS = {
        'Authorization':'Bearer {}'.format(ACCESS_TOKEN),
        'Content-Type':'application/json'
    }
    
    intents = json.loads(get_intents().decode("utf-8"))
    for intent in intents:
        print(intent['name'])
        
    post_intent('sample1','sample message','sample reply')
    
    return 'Hello from Lambda'
    
if __name__ == '__main__':
	lambda_handler('test','test')
    
    
    
    
