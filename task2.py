import boto.utils
import json
from nested_lookup import nested_lookup
from nested_lookup import get_all_keys

def search_metadata():
        input1=input("Enter partiular instance key for data to be retrieved or type quit for exit : ")
        if(input1=="quit"):
           exit()

        if(input1 in get_all_keys(metadata1)):

           print(nested_lookup(input1, metadata1))
           search_metadata()

        else:
           print("You have entered wrong metadata key or no such key exist")

data=boto.utils.get_instance_metadata(version='latest', url='http://169.254.169.254', data='meta-data/', timeout=None, num_retries=5)
metadata = json.dumps(data, indent=4)
metadata1 = json.loads(metadata)

print(metadata)
search_metadata()
