# ssh-keygen -t rsa -b 4096 -C "ravi.munnangi@gmail.com"

# eval "$(ssh-agent -s)"

# vi ~/.ssh/config
# add below contents:

# Host *
#   AddKeysToAgent yes
#   IdentityFile ~/.ssh/id_rsa

# ssh-add -K ~/.ssh/id_rsa