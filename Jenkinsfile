pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'python test_app.py'
      }
    }

    stage('Finish') {
      steps {
        sh 'echo \'It is done\''
      }
    }

  }
}