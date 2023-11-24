# Jenkins
Here are the steps to setup Jenkins, more info on: https://www.youtube.com/watch?v=f4idgaq2VqA

1. go to https://www.linode.com
2. spin up two server from market place includ Jnekinse and docker to be able to use this later.
3. Then go to the ip of you Jenkise server on port 8080
4. Then ssh to your server and find the password and install git
5. then click in Install suggested plugins
6. go to manage Jenkins and then plugins and then install Blue ocean
7. install Docker and Docker Compose build step
8. Then retrun to the dashboard and Klick on Open Blue Ocean to go to the new interface and spin up the Jenkins
9. creat a pip line and then linkit to your github
10. you should select a repo you want to add Jenkise, first you need to add git here to create jenkise and then you can add tasks in paralel for example you can get the file list in parallel e.g. ls -la from shell script or in paralled you can add
