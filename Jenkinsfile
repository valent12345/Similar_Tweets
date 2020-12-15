pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Start testing App'
        sh 'git branch - a'
      }
    }

    stage('End') {
      steps {
        echo 'Done'
      }
    }

  }
}