#Maxavier Jeanphilippe
from github import Github

g = Github('87f55c9dede62bf6b2dbb639609c4c576a0a12e1')
repos = g.get_repos()
for r in repos:
    print(r)