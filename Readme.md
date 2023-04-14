# Ansible Practice Exercises

## This is a repo with the examples of the Udemy advance ansible course
---
### To run this project you need to follow this

1. Clone this repo
2. Run the docker compose <br>
`$ docker compose up -d`
3. SSH to the pivot server<br>
`$ ssh ubuntu@localhost -p 2222`
4. cd to the mapped folder<br>
`$ cd ansible`
5. Execute the ansible command to test if everything is working<br>
`ansible -m ping -i inventory.txt all`

