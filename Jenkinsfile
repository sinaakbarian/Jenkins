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
        stage('ls') {
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

    stage('print') {
      steps {
        echo 'The test pass successfully'
      }
    }

    stage('build docker') {
      steps {
        sh 'docker build -f Dockerfile -t jenkins:1.0 .'
      }
    }

    stage('docker login') {
      steps {
        sh 'docker login -u $username -p $password ghcr.io'
      }
    }

  }
  environment {
    password = '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'
    username = 'sinaakbarian'
  }
}