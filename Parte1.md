# SisEmb2_Lab1
# Parte1 
# 1
mkdir -p "ice cream 2023/water flavors/Cinnabon apple" "ice cream 2023/water flavors/pineapple" "ice cream 2023/milk flavors/chocolate" "ice cream 2023/milk flavors/cappuccino"

tree

# 2
touch color
nano color ->Rojo
cat color
mkdir colors
mv color colors/
cd colors
nano color -> añadimos
cat color

# 3
touch nombre
nano nombre->kevin
mkdir "student registry"
cp nombre "student registry"/
cd "student registry"
gedit nombre ->Calani
cat nombre

# Parte2
# 1
sudo groupadd Distribution

sudo useradd -m -s /bin/bash -G Distribution,sudo Company
sudo passwd Company

sudo useradd -m -s /bin/bash -G Distribution Engineer
sudo passwd Engineer

sudo useradd -m -s /bin/bash -G Distribution Operator
sudo passwd Operator

# 2
mkdir "Designed tasks"
cd "Designend tasks"
mkdir "Maintenance" "Production Line" "Fixes" "Costs"

cd Maintenance
touch Dates
nano Dates
cd ..

cd "Production Line"
touch Dates
nano Dates
cd ..

cd Fixes
touch Dates
nano Dates
cd ..

cd Costs
touch Dates
nano Dates
cd ..

mkdir -p "Products"/"One" "Products"/"TWO" "Products"/"TREE"

cd Maintenance
gedit Dates
cd..

cd "Production Line"
gedit Dates
cd..

cd Fixes
gedit Dates
cd..

cd Costs
gedit Dates
cd..

# 3
sudo useradd -m -s /bin/bash Supervisor

sudo passwd Supervisor

sudo usermod -a -G Distribution Supervisor

sudo chown Supervisor:Distribution "Designed tasks"

sudo chmod 770 "Designed tasks"
