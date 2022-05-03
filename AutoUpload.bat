@ECHO OFF
ECHO Hello World! My first batch file was printed on the screen successfully.
D:
cd Works_Space\SOA_University
git pull
git status
git add .
git status
git commit -m"auto uploaded by bat file"
git push
PAUSE