import yaml
import subprocess

def create_tunnel():
	ssh_command = f"/usr/bin/ssh -NT {' '.join(tunneled_ports)} -R {port}:localhost:22 {username}@{hostname}"
	# print(ssh_command)
	subprocess.run(ssh_command, shell=True)

with open('tunnel_config.yaml', 'r') as f:
	config = yaml.safe_load(f)

hostname = config['hostname']
port = config['port']
username = config['username']

tunneled_ports = []
for port_config in config['tunneled_ports']:
	tunneled_ports.append(f"-R {port_config}")

create_tunnel()