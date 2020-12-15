pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Start testing App'
        bat 'python test_app.py'
      }
    }

    stage('End') {
      steps {
        echo 'Done'
      }
    }

  }
}
