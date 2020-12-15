pipeline {
  agent any
  stages {
    stage('Go to feature Branch') {
      steps {
        sh 'echo \'start testing\''
      }
    }

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