import yaml

Servers = [
    {'name': 'server-1', 'ip': '10.0.0.1', 'port': 9100},
    {'name': 'server-2', 'ip': '10.0.0.2', 'port': 9100},
]

targets = []
for s in Servers:
    ip = s['ip']
    port = s['port']
    target = f"{ip}:{port}"
    targets.append(target)

config = {
    'global': {
        'scrape_interval': '15s'
    },
    'scrape_configs': [
        {
            'job_name': 'node_exporter',
            'static_configs': [
                {
                    'targets': targets
                }
            ]
        }
    ]
}

# Print it to see the structure
print(config)

with open('prometheus.yml', 'w') as f:
    yaml.dump(config, f, default_flow_style=False)

print("✅ Generated prometheus.yml")