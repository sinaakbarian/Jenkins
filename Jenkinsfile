pipeline {
  agent any
  stages {
    stage('Check Out Code') {
      steps {
        git(url: 'https://github.com/sinaakbarian/Jenkins', branch: 'main')
      }
    }

    stage('ls') {
      parallel {
        stage('get directory') {
          steps {
            sh 'ls -la'
          }
        }

        stage('Install requirement and run unittest') {
          steps {
            sh '''python3 -m venv test
. test/bin/activate
pip3 install -r requirements.txt
python3 utest.py
'''
          }
        }

      }
    }

    stage('build docker') {
      steps {
        sh 'docker build -f Dockerfile -t jenkins:1.0 .'
      }
    }

    stage('get docker images') {
      parallel {
        stage('get docker images') {
          steps {
            sh 'docker ps'
          }
        }

        stage('tag docker') {
          steps {
            sh 'docker tag jenkins:1.0 ghcr.io/sinaakbarian/jenkins:1.0'
          }
        }

      }
    }

    stage('Push docker') {
      steps {
        echo 'Done'
        script {
          withCredentials([string(credentialsId: 'passG', variable: 'Pass')]) {
            sh "docker login -u sinaakbarian -p $Pass ghcr.io"
            sh "docker push ghcr.io/sinaakbarian/jenkins:1.0"
          }
        }

      }
    }

  }
}