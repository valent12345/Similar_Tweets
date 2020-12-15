pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Start testing App'
        sh 'python stress_test_app.py'
      }
    }

    stage('End') {
      steps {
        echo 'Done'
      }
    }

  }
}