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
      parallel {
        stage('build docker') {
          steps {
            sh '#docker build -f Dockerfile -t jenkins:1.0 .'
          }
        }

        stage('Sina') {
          steps {
            sh ''' withCredentials([string(credentialsId: \'passG\', variable: \'MY_SECRET\')]) {
                        // Inside this block, MY_SECRET variable is available
                        echo "Secret Value: ${MY_SECRET}"




                        // You can use the secret in other steps or commands
                        sh \'echo "Using secret for something"\'
                    }'''
            }
          }

        }
      }

      stage('docker login') {
        steps {
          sh 'echo ${passG} | docker login -u sinaakbarian --password-stdin ghcr.io'
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
              sh 'docker tag jenkins:1.0 ghcr.io/sinaakbarian/jenkins:1.0 && docker push ghcr.io/sinaakbarian/jenkins:1.0ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â '
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