import json
from urllib2 import Request, urlopen
values =  '''
  {
    "statuspage_id": "58090e3b7170c62119000fb8",
    "all_infrastructure_affected": "0",
    "infrastructure_affected": [
      "58090fa17170c62119000fcb-58090f8ce60a2e2019001161",
      "58090fa17170c62119000fcb-622b4c5fd4460104d135f475"
    ],
    "maintenance_name": "sb.assuresign.net",
    "maintenance_details": "Prod deployment is taking place on APAC_PRIMARY_ACCOUNT. No downtime is expected.",
    "message_subject": "Example notification message subject",
    "date_planned_start": "06/07/2022",
    "time_planned_start": "23:00",
    "date_planned_end": "06/07/2022",
    "time_planned_end": "23:30",
    "maintenance_notify_now": "0",
    "maintenance_notify_72_hr": "0",
    "maintenance_notify_24_hr": "0",
    "maintenance_notify_1_hr": "0",
    "automation": "0"
  }
'''
headers = {
  'Content-Type': 'application/json',
  'x-api-id': '1bc1f288-318b-4515-ba0b-8fd6e7d8aa4d',
  'x-api-key': 'yHlBaxHMCN2owL3u8qDmiHICl8clWxgNCpEAHbUQwWhjHYgec15x+K8/fSqGrbAO40fQD183OlyZPZVRrMeTog=='
}
request = Request('https://api.status.io/v2/maintenance/schedule', data=values, headers=headers)
response_body = urlopen(request).read()
data = json.loads(response_body)
con = data["result"]
with open('id.txt', 'w') as f:
    f.write(con)