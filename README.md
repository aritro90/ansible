Download or Clone the CentosWithActiveDirectory

Set the ssh keys auth for the NFS client from the machine where you like to run these ansible playbooks
ssh-copy-id root@IP-of-client-machine

Install Ansible on the Base machine (if Centos) as below:
sudo yum install epel-release
sudo yum install ansible
