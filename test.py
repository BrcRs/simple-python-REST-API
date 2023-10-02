# let's send a request

import requests

BASE = "http://127.0.0.1:5000/" # local host


# response = requests.post(BASE + "helloworld") # post request will not work because if not defined!

# print(response.json())


response = requests.put(BASE + "video/1", {
                                        "likes": 14_000, 
                                        "views": 666_000, 
                                        "name": "Python REST API Tutorial - Building a Flask REST API"}) # send info through a *form* instead of public url
print(response.json())

input()

response = requests.get(BASE + "video/1") # send get request to url

print(response.json())

input()

response = requests.get(BASE + "video/545") # send get request to url

print(response.json())

input("Now for the fun part...\n(Press enter)")

data = [
    {"likes": 77, "views": 1000, "name": "Best video ever"},
    {"likes": 54, "views": 2, "name": "Holiday in Paris.mp4"},
    {"likes": 1685416516, "views": 6354546354156416, "name": "TRENDY VIDEO"}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

    input("Request " + str(i) + " done")

# response = requests.delete(BASE + "video/6")
# print(response)

# input()

# response = requests.delete(BASE + "video/2")

# print(response)

response = requests.get(BASE + "video/58485484")

print(response.json())

response = requests.patch(BASE + "video/1", {"views": 0})
print("heheee")
print(response.json())
# print(response.json())


response = requests.get(BASE + "video/1") # send get request to url

print(response.json())