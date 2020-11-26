# Test Zero Client using Selenium

This will perform automated tests against a Zero Client AWI using Selenium. \
The Zero Client will send the resulting logs to an external syslog server. \
After the tests, the syslogs will be zipped and shipped to a persistent storage location, \
such as an S3 bucket, after which the syslog server will be shut down. 

**Please see the syslog-server/README.md file for more info on the syslog server infrastructure and its requirements.**

## Requirements
### Tooling
- Ansible >= 2.9.10
- Terraform = 0.12.28 (for Terraform submodule)

# Directions for usage
This may be run as a playbook from a local workstation. 

## Steps 
1. Clone the repo onto the local workstation to run the playbook locally.
2. Update syslog-server/terraform.tfvars with all desired variables. 
3. Update the hosts.ini file with the remote syslog server's connection variables. 
4. Run the script:
```
ansible-playbook -i hosts.ini main.yml -vv
```
Optional:
Run the script against a specific host or host category in the host file
```
ansible-playbook -i hosts.ini main.yml -vv -l <instance IP or host category>
``` 

## Notes
- The connection to the Zero Client web interface must be trusted in order to run the Selenium tests in headless mode.
    - It is assumed that the connection to the Zero Client web interface is trusted already. The ca cert should be added to the trusted root store, if necessary.
