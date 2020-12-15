pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'echo \'Start testing App\''
        sh 'python test_app.py'
      }
    }

    stage('End') {
      steps {
        sh 'echo \'Done\''
      }
    }

  }
}