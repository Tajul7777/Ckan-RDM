from urllib.request import urlopen as uReq
import json
import requests
import re
import requests


def get_data():
	headers = {'Authorization': '71e2aebb-f605-4ad3-8d63-aa32f5be0bae',}
	jsondata = requests.get('http://localhost:5000/api/3/action/tag_list', headers=headers)
	
