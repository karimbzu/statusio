import sys
import json
import numpy as np
import requests, urllib
headers = {
  'Content-Type': 'application/json',
  'x-api-id': '1bc1f288-318b-4515-ba0b-8fd6e7d8aa4d',
  'x-api-key': 'yHlBaxHMCN2owL3u8qDmiHICl8clWxgNCpEAHbUQwWhjHYgec15x+K8/fSqGrbAO40fQD183OlyZPZVRrMeTog=='
}
import os

#to get the current working directory

os.chdir('./templates/statusio/')
directory = os.getcwd()
print(directory)

def extract_id():
  with open('id.txt', 'r') as f:
    for line in f:
      return line
id = str(extract_id())
values_maintenance = """
  {
    "statuspage_id": "58090e3b7170c62119000fb8",
    "maintenance_id": \""""+id+"""\",
    "maintenance_details": "Starting maintenance activity now",
    "message_subject": "Example notification message subject",
    "notify_email": "0",
    "notify_sms": "1",
    "notify_webhook": "0",
    "social": "0",
    "irc": "0",
    "hipchat": "0",
    "msteams": "0",
    "slack": "0"
  }
"""
def start_maintenance():
  with open("environments.txt", "r") as a_file:
    for line in a_file:
      stripped_line = line.strip()
      if stripped_line == sys.argv[1]:
        r = requests.post('https://api.status.io/v2/maintenance/start', data=values_maintenance, headers=headers)
start_maintenance()