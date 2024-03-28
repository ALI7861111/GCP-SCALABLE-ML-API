## ML MODEL INFRENECE USING SCALABLE REST API ON GCP


1. Got the Jupyter Data ,Notebook from : https://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning/data
2. Create flask app
3. create docker container
4. Create instance template on GCP.
5. Create a startup script for every instance to launch
6. Configure the loadbalancer. 


## CREATE SSH KEYS

ssh-keygen -t rsa -b 4096 -C "your_email@example.com"


# Push code to GCLOUD REPOSITORY
generate a ssh key and add it to the GCP : 

https://source.cloud.google.com/user/ssh_keys?register=true

```
ssh-keygen -t rsa -b 4096 -C "email"

CLONE FROM REPO 
git clone ssh://email@source.developers.google.com:2022/p/project_name/r/repo_name


cd Deployment
git add .
git commit -m "Initial commit"
git push -u origin master
```
# Google client
```
install Google Cloud SDK
gcloud init
gcloud source repos clone Deployment --project=project_name
```


# Command to build Docker Container
```
sudo docker build -t my-flask-app .
sudo docker run -p 5000:5000 my-flask-app
```



## Startup Script on Instance template

```sudo apt-get update
echo "Installing Docker"
sudo apt-get install -y docker.io
echo "Docker Installed
echo "Installing Git"
sudo apt-get install -y git
echo "Git Installed"
echo "Cloning the Repository"
gcloud source repos clone Deployment --project=mldeploy-tutorial-37280
echo "Repository Cloned"
cd Deployment
echo "Building the Docker Image"
sudo docker build -t my-flask-app .
echo "Docker Image Built"
echo "Running the Docker Image"
sudo docker run -d --restart=always -p 5000:5000 --name my_container my-flask-app```