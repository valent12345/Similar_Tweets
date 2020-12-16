pipeline{
  agent any
  stages {
    stage('Build Flask app'){
      steps{
        sh 'docker build -t myflaskapp .'
      }
    }
     stage('Run Flask App'){
       steps{
            sh 'docker run -d -p 5000:5000 --name myflaskapp_c myflaskapp'
          }
        }
     
  
    stage('Testing'){
      steps{
        sh 'python test_app.py'
      }
    }
    stage('Docker images down'){
      steps{
        sh 'docker rm -f myflaskapp_c'
        sh 'docker rmi -f myflaskapp'
      }
    }
  }
}
