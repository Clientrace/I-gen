import requests
import json


def create_intent(name,msg,response):
	return {
		'name' : 'intent11',
		'auto' : True,
		'contexts':[],
		'templates':[],
		'userSays':[
			{
				'data': [
					{
						'text':msg
					}
				],
				'isTemplate': False,
				'count': 0
			}
		],
		'responses':[
			{
				'resetContexts': False,
				'action': '',
				'affectedContexts':[],
				'parameters':[],
				'speech': response
			}
			
		],
		'priority': 500000
	}
	
	

if __name__ == '__main__':
	data = create_intent('intent11','yeah','yoowh')
	ACCESS_TOKEN = '30fe3ab64d6c4acf9fdf6e0085d7c650'
	BASE_URL = 'https://api.api.ai/v1/'
	HEADERS = {'Authorization':'Bearer {}'.format(ACCESS_TOKEN)}
	response = requests.post(BASE_URL+'intents',headers=HEADERS,json=data)
	print(response)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
