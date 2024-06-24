# Initilize the GIT in local folder 
    --> git init
# cREATE Conda environment 
    --> conda create --prefix ./env python=3.8 -y

#Difference Between GIT , MLFLOW , DVC

GIT: Source code Management i.e for code versioning

MLFLOW : this is for Experimental Tracking , this will track artifacts, logs and parameter
        we have UI for Mlflow 
        we can do model registry and model versioning

DVC : This is for Data Versioning and Pipeline versioning

# Purpose of dvc is to track the changes of Data Versioning and Pipeline versioning
# Initilize DVC 
   --> dvc init

# How to perform data versionig in DVC 
   --> dvc add data/data.csv

# If we want to connect our DVC to any cloud server like Azure\GPC\AWS we can pass the url after storega
#since we want to see how it works we are checking with our local path #    
    --> dvc remote add -d remote_storage F:/Ineuron/DVC/myremote

# Complete tutorial about DVC 
    --> https://realpython.com/python-data-version-control/

# Next step created a two py files stage_01 and Stage_02 , stage_01 create a txt file and write whereas Stage_02 read the created file
stage_02 is dependent on stage_02 file 

to create a ppipeline we are doing below steps
# create a dvc.yaml file to write the configuration i.e

# if want dvc reproducebility , here is the command for it 
    --> dvc repro    

# below command shows the dependecies of which was there  
# DAG(Direct acyclic Graph) we dont have any loop 
--> dvc dag 
eg: stage_01.py is dependent on stage_02.py

# Now there are no changes made in the stage files , if we run dvc repro then it will skip as changes were not made and it will display pipline are up to date 
    --> dvc repro
dvc repro will defualt call the dvc.yaml file and it will try to execute the command mentioned in it 
once we run the we will get the dvc.lock file it will have every information regarding the pipeline
every information of the pipeline will be saved in .dvc/cache/file 

# by using this dvc we can track the entire pipeline if we are making any changes in the file we can track (pipeline versioning) its doing with dvc.yaml file 



