import json
import numpy as  np
values = """
  {
    "infrastructure_affected": [
      "53d746c0383cd493cf00001a-58090f8ce60a2e2019001161",
      "53d746c0383cd493cf00001a-622b4c5fd4460104d135f475"
    ]
  }
"""
database = "env.json"
data_comp = json.loads(open(database).read())

data = json.loads(values)
con = data["infrastructure_affected"]
arr = np.array(con)
for i in range(len(arr)):
 text = ((str(arr[i]).split('-')))
 print (text[1])
 for item in data_comp["container"]:
    if item["id"] == text[1]: 
      print  (item["env"])
      break

