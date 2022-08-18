from urllib2 import Request, urlopen

values =  '''
    {
    "statuspage_id": "58090e3b7170c62119000fb8",
    "infrastructure_affected": [
      "58090fa17170c62119000fcb-58090f8ce60a2e2019001161",
      "58090fa17170c62119000fcb-622b4c5fd4460104d135f475"
    ],
    "incident_name": "Test by skhan",
    "incident_details": "Investigating database connection issue",
    "message_subject": "Example notification message subject",
    "notify_email": "0",
    "notify_sms": "1",
    "notify_webhook": "0",
    "social": "0",
    "irc": "0",
    "hipchat": "0",
    "msteams": "0",
    "slack": "0",
    "current_status": 300,
    "current_state": 100,
    "all_infrastructure_affected": "0"
  }
'''
headers = {
  'Content-Type': 'application/json',
  'x-api-id': '1bc1f288-318b-4515-ba0b-8fd6e7d8aa4d',
  'x-api-key': 'yHlBaxHMCN2owL3u8qDmiHICl8clWxgNCpEAHbUQwWhjHYgec15x+K8/fSqGrbAO40fQD183OlyZPZVRrMeTog=='
}
request = Request('https://api.status.io/v2/incident/create', data=values, headers=headers)
response_body = urlopen(request).read()
print (response_body)