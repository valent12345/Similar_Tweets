pipeline {
  agent {
    docker {
      image 'python:3.7.2'
    }

  }
  stages {
    stage('build') {
      steps {
        echo 'Start building'
        sh 'pip install -r requirements.txt'
      }
    }

    stage('test') {
      parallel {
        stage('test') {
          steps {
            sh 'python test.py'
          }
        }

        stage('Stress_test') {
          steps {
            sh 'python stress_test_app.py'
          }
        }

      }
    }

    stage('End') {
      steps {
        echo 'Finish'
      }
    }

  }
}