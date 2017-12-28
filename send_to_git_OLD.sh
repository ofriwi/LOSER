git add ./
echo "Write Description"
read desc
git commit -m "$desc"
git push -u origin master
read wait