Download or Clone the CentosWithActiveDirectory git project in your base linux Machine (Preferably Centos7) 

Create a centos 7 VM with DHCP enable (this will be your NFS client machine), login to the console of the VM to make its interface up using `ifup <interface-name>` command and note down the IP address got assigned to the interface using `ip a` command 

Set the ssh keys auth for the NFS client from the base machine (where you will run the ansible playbooks). Below command needs to be excuted from the base machine  
`ssh-copy-id root@IP-of-client-machine `  

Install Ansible on the Base machine (if Centos) as below:   
```sudo yum -y install epel-release   
sudo yum -y install ansible  
sudo yum -y install python3* ``` 

Once the above has been installed navigate to CentosWithActiveDirectory Dierctory(downloaded git project). Make sure you are inside the directory  
Execute `python ./input.py` 
The above will ask you to provide inputs for different parameters  
Once done you need to run the ansible playbook one by one as below:  

```ansible-playbook -i inventory.ini 1_networking.yml --extra-vars='@Attrib.json' 
ansible-playbook -i inventory.ini 2_installing_services.yaml  
ansible-playbook -i inventory.ini 3_ntp.yml --extra-vars='@Attrib.json'  
ansible-playbook -i inventory.ini 4_services.yml  
ansible-playbook -i inventory.ini 5_copy-conf-files.yml  
ansible-playbook -i inventory.ini 6_promtp.yml --extra-vars='@Attrib.json'  
ansible-playbook -i inventory.ini 7_sssd-command.yml  ```
