@ECHO OFF
ECHO Auto pulling, adding, commiting and pushing on Github.
ECHO ===================================================================================
D:
cd Works_Space\SOA_University
git pull
git status
git add .
git status
git commit -m"auto uploaded by bat file"
git push
ECHO ===================================================================================
ECHO Have a Good Day
PAUSE