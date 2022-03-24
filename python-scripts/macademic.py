########### Python 2.7 #############
import http.client as httplib
import base64
import urllib.parse

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '{7ce3c703-fa79-43f8-8e2d-b747e8dd0fa4}',  # Put your key here. This should look something like: 'Ocp-Apim-Subscription-Key': '3b45....'
}

# I removed the `'orderby': '{string}',` field as I didn't check what values it could take. You can look for this and other parameters which may be relevant to you.
params = urllib.parse.urlencode({
    # Request parameters
    'model': 'latest',
    'count': '10',
    'offset': '0',
    'attributes': 'Id',
})

# define your 'exp' here. I am calling it 'my_exp'. Note that the title's value  should all be in lowercase. The urllib.quote() is needed to ensure that the spaces between words are proprely url encoded before sending to the API server. 
my_exp = urllib.parse.quote("Ti='imagenet classification with deep convolutional neural networks'")  # an example title

try:
    conn = httplib.HTTPSConnection('api.labs.cognitive.microsoft.com')
    conn.request("GET", "/academic/v1.0/evaluate?expr=%s&%s" % (my_exp,params), "", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
# Voila!