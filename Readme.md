# Section 10

## Inventory
1. `$ ansible-vault encrypt inventory.txt`
2. `$ ansible-playbook playbook.yaml -i inventory.txt --ask-vault-pass`
3. `$ ansible-playbook playbook.yaml -i inventory.txt --vault-password-file ~/.password.txt`
4. `$ ansible-playbook playbook.yaml -i inventory.txt --vault-password-file ~/script_password.py`
5. `$ ansible-vault view inventory.txt`

[official documentation](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_filters.html#filters-for-formatting-data)