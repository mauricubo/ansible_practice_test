# Ansible Practice Exercises

### This is a repo with the examples of the Udemy advance ansible course

<i>To run this project you need to follow this:</i>

1. Clone this repo
2. Run the docker compose <br>
`$ docker compose up -d`
3. SSH to the pivot server<br>
`$ ssh ubuntu@localhost -p 2222`
4. cd to the mapped folder<br>
`$ cd ansible`
5. Execute the ansible command to test if everything is working<br>
`ansible -m ping -i inventory.txt all`

> **_NOTE:_** Default username and password is `ubuntu`: `ubuntu`<br>
> If you want to set your own password, set the environment variable `SSH_PASS=my_new_password` on the docker-compose.yaml
---
### Switching between different exercises
<i>In this project exist branches with the example of every section of the course.</i><br>
If you want to move and try the different exercises you only need to switch between the project branches.<br>
`$ git checkout sectionX`

--- 
### Docker images
The docker images used for this test environment are custom images. If you want to see the details you can check the `dockerhub repo`.<br>
- [ubuntu_ansible_sshd](https://hub.docker.com/r/mauricubo/ubuntu_ansible_sshd)
- [ubuntu_sshd](https://hub.docker.com/r/mauricubo/ubuntu_sshd)