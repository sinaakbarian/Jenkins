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
      parallel {
        stage('print') {
          steps {
            echo 'The test pass successfully'
          }
        }

        stage('test') {
          steps {
            sh 'echo $pass'
          }
        }

      }
    }

    stage('build docker') {
      environment {
        sina = 'credentials(\'3477edf3-4b7b-45b6-8ef1-645f5310816f"\')'
      }
      steps {
        sh 'docker build -f Dockerfile -t jenkins:1.0 .'
      }
    }

    stage('docker login') {
      environment {
        pass = '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'
      }
      steps {
        sh '''echo "$pass" | docker login --username "sinaakbarian" --password-stdin ghcr.io
'''
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
            sh 'docker tag jenkins:1.0 ghcr.io/sinaakbarian/jenkins:1.0 && docker push ghcr.io/sinaakbarian/jenkins:1.0Â '
          }
        }

      }
    }

    stage('done') {
      steps {
        echo 'Done'
      }
    }

  }
}