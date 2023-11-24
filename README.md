# Jenkins Setup Guide

This guide provides step-by-step instructions for setting up Jenkins on a Linode server. For a visual walkthrough, refer to the accompanying [video tutorial](https://www.youtube.com/watch?v=f4idgaq2VqA).

## Prerequisites
1. Sign in to [Linode](https://www.linode.com) and navigate to the Marketplace.
2. Spin up a Jenkins server from the Marketplace to be used later.

## Installation Steps

### 1. Access Jenkins Dashboard
- Visit the IP address of your Jenkins server on port 8080 in your web browser.

### 2. Initial Server Configuration
- SSH into your server to retrieve the Jenkins initial password.
- Install essential tools: Git, Python, python3-venv, and Pip using `apt-get install`.

### 3. Plugin Installation
- On the Jenkins dashboard, click "Install suggested plugins" to set up the basic environment.

### 4. Blue Ocean Integration
- Navigate to "Manage Jenkins," then "Manage Plugins," and install the Blue Ocean plugin.

### 5. Docker Setup
- Install Docker and Docker Compose build step to enable Docker integration.

### 6. Open Blue Ocean
- Return to the Jenkins dashboard and click "Open Blue Ocean" to access the new user-friendly interface.

### 7. Pipeline Creation
- Create a pipeline and link it to your GitHub repository.

### 8. Repository Integration
- Select the repository you want to add to Jenkins. Ensure that Git is added to create Jenkins tasks.

### 9. Parallel Tasks
- For parallel tasks, add commands in the pipeline script. Example:
  ```groovy
  stages {
      stage('Parallel Stage') {
          parallel {
              stage('File List') {
                  steps {
                      sh 'ls -la'
                  }
              }
              stage('Environment Setup') {
                  steps {
                      sh 'python3 -m venv test'
                      sh 'source test/bin/activate'
                      sh 'pip3 install -r requirements.txt'
                      sh 'python3 utest.py'
                  }
              }
          }
      }
  }
  ```


By following these steps, you will have a fully configured Jenkins server with integrated plugins, Docker support, and a pipeline linked to your GitHub repository.
