import yaml

tutorials = [
    {'id': 1,
     'job_portal': 'Portal1',
     'status': 'A',
     'company_id': 1
    },
    {'id': 2,
     'job_portal': 'Portal2',
     'status': 'I',
     'company_id': 2
    },
    {'id': 3,
     'job_portal': 'Portal3',
     'status': 'A',
     'company_id': 3
    },
]


with open(r'data.yaml', 'w') as f:
    documents = yaml.dump(tutorials, f)
