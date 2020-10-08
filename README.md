# Test Zero Client using Selenium

This will perform automated tests against a Zero Client AWI using Selenium. \
The Zero Client will send the resulting logs to an external syslog server. \
After the tests, the syslogs will be zipped and shipped to a persistent storage location, \
such as an S3 bucket, after which the syslog server will be shut down.  

## Requirements
### Tooling
- Ansible >= 2.9.10

# Directions for usage
This may be run as a playbook from a local workstation. 

## Steps 
1. Clone the repo onto the local workstation to run the playbook locally.
2. Modify the hosts file consisting of the public IPs and host variables of the target hosts.  
3. Modify the vars/main.yml file with the proper variables.
4. Run the script:
```
ansible-playbook -i hosts.ini main.yml -vv
```
Optional:
Run the script against a specific host or host category in the host file
```
ansible-playbook -i hosts.ini main.yml -vv -l <instance IP or host category>
``` 

