# create pages
make clean;
make html;

# move pages and format
cd ../docs
rm -rf doctrees
mv html/* .
rm -rf html

# create nojekyll
touch .nojekyll
