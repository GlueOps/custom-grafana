import yaml
import json
import re
import requests
from urllib.parse import urlparse
import os

# Function to extract and clean JSON from YAML content
def extract_clean_json(yaml_content):
    # Parse YAML content
    yaml_data = yaml.safe_load(yaml_content)
    
    # Get the first key from the 'data' dictionary
    first_key = next(iter(yaml_data['data']))
    
    # Extract JSON string using the first key
    json_string = yaml_data['data'][first_key]
    
    # Remove escaping from the JSON string
    cleaned_json_string = re.sub(r'\{\{`\{\{(.*?)\}\}`\}\}', r'{{\1}}', json_string)
    
    # Parse the cleaned JSON string
    json_data = json.loads(cleaned_json_string)
    
    return json_data, first_key

# Function to add filters to each expr in the targets
def add_filters_to_expr(json_data):
    filter_string = 'captain_domain="$glueops_captain_domain",__replica__="$glueops_prometheus_replica",'
    
    for panel in json_data.get('panels', []):
        for target in panel.get('targets', []):
            expr = target.get('expr')
            if expr:
                # Add the filter to every set of curly braces in the expr
                expr = re.sub(r'\{([^}]*)\}', r'{'+filter_string+r'\1}', expr)
                target['expr'] = expr

# Function to process URLs
def process_urls(urls):
    for url in urls:
        # Fetch content from URL
        response = requests.get(url)
        if response.status_code == 200:
            yaml_content = response.text
            json_data, first_key = extract_clean_json(yaml_content)
            
            # Add new entries to the beginning of the templating.list section
            new_entries = [
              {
                "current": {
                  "selected": False,
                  "text": "",
                  "value": ""
                },
                "definition": "label_values(captain_domain)",
                "hide": 0,
                "includeAll": False,
                "label": "glueops_captain_domain",
                "multi": False,
                "name": "glueops_captain_domain",
                "options": [],
                "query": {
                  "qryType": 1,
                  "query": "label_values(captain_domain)",
                  "refId": "PrometheusVariableQueryEditor-VariableQuery"
                },
                "refresh": 1,
                "regex": "",
                "skipUrlSync": False,
                "sort": 0,
                "type": "query"
              },
              {
                "current": {
                  "selected": False,
                  "text": "",
                  "value": ""
                },
                "definition": "label_values(__replica__)",
                "hide": 0,
                "includeAll": False,
                "label": "glueops_prometheus_replica",
                "multi": False,
                "name": "glueops_prometheus_replica",
                "options": [],
                "query": {
                  "qryType": 1,
                  "query": "label_values(__replica__)",
                  "refId": "PrometheusVariableQueryEditor-VariableQuery"
                },
                "refresh": 1,
                "regex": "",
                "skipUrlSync": False,
                "sort": 0,
                "type": "query"
              }
            ]

            if 'templating' in json_data and 'list' in json_data['templating']:
                json_data['templating']['list'] = new_entries + json_data['templating']['list']
            else:
                print("No templating section found")

            # Add filters to each expr in the targets
            add_filters_to_expr(json_data)
            
            # Use the first_key as the file name
            file_name = f"{first_key}"
            file_path = os.path.join('dashboards/', file_name)
            with open(file_path, 'w') as outfile:
                json.dump(json_data, outfile, indent=2)
        else:
            print(f"Failed to fetch content from URL: {url}")

# List of URLs to process
urls = [
    'https://raw.githubusercontent.com/GlueOps/platform-helm-chart-grafana-dashboards/v0.12.0/templates/cert-manager.yaml',
    'https://raw.githubusercontent.com/GlueOps/platform-helm-chart-grafana-dashboards/v0.12.0/templates/debezium-generic.yaml',
    'https://raw.githubusercontent.com/GlueOps/platform-helm-chart-grafana-dashboards/v0.12.0/templates/external-dns.yaml',
    'https://raw.githubusercontent.com/GlueOps/platform-helm-chart-grafana-dashboards/v0.12.0/templates/fluentbit',
    'https://raw.githubusercontent.com/GlueOps/platform-helm-chart-grafana-dashboards/v0.12.0/templates/ingress-by-host.yaml',
    'https://raw.githubusercontent.com/GlueOps/platform-helm-chart-grafana-dashboards/v0.12.0/templates/kafka-topics.yaml',
    'https://raw.githubusercontent.com/GlueOps/platform-helm-chart-grafana-dashboards/v0.12.0/templates/keda.yaml',
    'https://raw.githubusercontent.com/GlueOps/platform-helm-chart-grafana-dashboards/v0.12.0/templates/loki-logs.yaml',
    'https://raw.githubusercontent.com/GlueOps/platform-helm-chart-grafana-dashboards/v0.12.0/templates/network-exporter.yaml',
    'https://raw.githubusercontent.com/GlueOps/platform-helm-chart-grafana-dashboards/v0.12.0/templates/nginx-ingress.yaml',
    'https://raw.githubusercontent.com/GlueOps/platform-helm-chart-grafana-dashboards/v0.12.0/templates/strimzi-kafka-exporter.yaml',
    'https://raw.githubusercontent.com/GlueOps/platform-helm-chart-grafana-dashboards/v0.12.0/templates/strimzi-kafka.yaml',
    'https://raw.githubusercontent.com/GlueOps/platform-helm-chart-grafana-dashboards/v0.12.0/templates/vault.yaml'
]

# Process the URLs
process_urls(urls)
