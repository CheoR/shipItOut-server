#!/usr/bin/zsh

# Note: This is only after you already have created your db, ran migations, migrate and filled it with data.
# If you need to create fixtures, you can do something like
#
# $ python3 manage.py dumpdata app1.service --indent 2 > data/fixtures/services.json
#
# Where app1 is the app name.
#
# Script clears tables from the postgreql db.
# Then recreates the migrations and migrates to db.
# Then loads your data into the tables with fixtures.
#
# appName - rename to your app
# tablesToDropArray - array of tabes to drop
# fixturesArray - array of fixtures to load
# -e enables interpretation of backslash escapes
#
# Use:
#  $ bash seed_data.sh
#
######################
# Data Order Example #
######################
# python manage.py loaddata users
# python manage.py loaddata tokens
# python manage.py loaddata customers
# python manage.py loaddata product_category


appName="api"
pathToFixtures="data/fixtures"

declare -a tablesToDropArray=($appName authtoken auth users tokens appusers ports vessels voyages bookings containers products)
# TODO: dump new data fixtures to reflect new db configutation
declare -a fixturesArray=(users tokens appusers ports vessels voyages bookings containers products)


echo -e '\n==============='
echo 'Dropping tables'
echo '==============='

for val in ${tablesToDropArray[@]}; do
   echo -e "\n*************"
   echo "Dropping $val"
   echo "*************"
   python manage.py migrate $val zero
done


echo -e '\n========================'
echo 'Deleteing app migrations'
echo '========================'
rm -rf $appName/migrations


echo -e '\n============================='
echo 'Running makemigrations on app'
echo '============================='
python3 manage.py makemigrations $appName


echo -e '\n==============='
echo 'Running migrate'
echo '==============='
python3 manage.py migrate


echo -e '\n================'
echo 'Loading fixtures'
echo '================'

for fixture in ${fixturesArray[@]}; do
   echo -e "\n*************"
   echo "Loading $fixture"
   echo "*************"
   python manage.py loaddata $pathToFixtures/$fixture
done

echo -e '\n================'
echo 'DONE'
echo '================'