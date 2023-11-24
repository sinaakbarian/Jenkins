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
            sh '''pip install -r requirements.txt && python unittest.py
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

  }
}