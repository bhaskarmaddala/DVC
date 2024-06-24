--> Initilize the GIT in local folder 
    git init
--> cREATE Conda environment 
    conda create --prefix ./env python=3.8 -y

# Initilize DVC 
    dvc init

# How to perform data versionig in DVC 
    dvc add data/data.csv

# If we want to connect our DVC to any cloud server like Azure\GPC\AWS we can pass the url after storega
since we want to see how it works we are checking with our local path 
dvc remote add -d remote_storage F:/Ineuron/DVC/myremote