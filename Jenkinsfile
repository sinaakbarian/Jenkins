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
            sh '''python3 -m venv test && source test/bin/activate && pip install -r requirements.txt && python3 unittest.py
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