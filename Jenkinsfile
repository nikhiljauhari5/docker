#!groovy

pipeline {
  agent {
       label 'master'
  }
  stages {

    stage('Docker Build and Run Tests') {
        steps {
            sh 'docker build -t sel:latest .'
            sh 'docker run sel:latest'
        }
    }
    }
  }
