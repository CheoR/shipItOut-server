#!/bin/bash

# To load fixures
# 
#  $ heroku run bash heroku_load_fixtures.sh
#
######################
# Data Order Example #
######################

appName="api"
pathToFixtures="data/fixtures"

declare -a fixturesArray=(appusers services vessels voyages carriers ports documents dues bkgstatuses cntrstatuses containers products bookings)


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
   python3 manage.py loaddata $pathToFixtures/$fixture
done

echo -e '\n================'
echo 'DONE'
echo '================'