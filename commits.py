from random import randint
from datetime import date, timedelta as td

d1 = date(2010, 1, 1)
d2 = date(2011, 12, 31)

delta = d2 - d1

print("""
#!/bin/bash
REPO=temporal
git init temporal
cd testing
touch README.md
git add README.md
touch tox
git add tox
""")

for i in range(delta.days + 1):
    current = str(d1 + td(days=i))
    for j in range(randint(1,10)):
    	command = 'GIT_AUTHOR_DATE=' + current + 'T12:00:00 GIT_COMMITTER_DATE=' + current + 'T12:00:00 git commit --allow-empty -m "tox" > /dev/null'
    	print(command)

print("""

git remote add origin git@github.com:toxtli/temporal.git
git pull origin master
git push -u origin master

""")
