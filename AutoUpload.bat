@ECHO OFF
ECHO ====== SOA UNIVERSITY ======
ECHO Auto pulling, adding, commiting and pushing on Github.
ECHO ===================================================================================

git pull
git status
git add .
git status
git commit -m"updating classwork contents"
git push

ECHO ===================================================================================
ECHO Don't Have a Good Day, Have a Great Day
PAUSE