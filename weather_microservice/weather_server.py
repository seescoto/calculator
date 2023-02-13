####
#sending/receiving data to audrie's weather app using weatherapi.com and zmq 

#weather api stuff
from __future__ import print_function 
import swagger_client 
from swagger_client.rest import ApiException 
from pprint import pprint 
import config #has api key

import time 

#configure api key authorization
configuration = swagger_client.Configuration() 
configuration['key'] = config.apiKey

#create instance of api class 
apiInstance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
query = 'London' #can pass zip code / postal code / lat and long degrees / city
days = 3 #number of days of weather to forecast 
hour = 12 #hour in military time

#get forecast
try:
   response = apiInstance.forecast(query, days, hour=hour) 
   pprint(response)
except ApiException as e:
   print("Exception calling APIsApi -> forecast_weather: %s \n" % e)
