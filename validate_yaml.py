import yaml

try:
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    print('Valid YAML. Content:', config)
except yaml.YAMLError as e:
    print('Invalid YAML:', e)
except FileNotFoundError:
    print('config.yaml not found in current directory.')
except Exception as e:
    print('Error:', e)