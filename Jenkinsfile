pipeline {
  agent any
  stages {
    stage('Build and Test') {
      steps {
        sh 'docker-compose build --no-cache'
        sh 'rm -f output.html'
        sh 'touch output.html'
        sh 'docker run -v $(pwd)/output.html:/usr/src/app/output.html duke/duke:latest debug'
      }
    }
    stage('Deploy Integration'){
      when {
        expression { BRANCH_NAME == 'integration' }
      }
      environment {
        WEBHOOKS_FILE = credentials('')
      }
      steps {
        sh 'cp $WEBHOOKS_FILE webhooks.yml'
        sh 'docker-compose down'
        sh 'docker-compose up -d'
      }
    }
    stage('Deploy Master'){
      when {
        expression { BRANCH_NAME == 'master' }
      }
      environment {
        WEBHOOKS_FILE = credentials('')
      }
      steps {
        sh 'cp $WEBHOOKS_FILE webhooks.yml'
        sh 'docker-compose down'
        sh 'docker-compose up -d'
      }
    }
  }
  post {
    success {
      script {
        if (env.CHANGE_ID) {
          archiveArtifacts artifacts: 'output.html'
          pullRequest.comment("Output.html uploaded to ${env.BUILD_URL}artifact/output.html")
        }
      }
    }
  }
}