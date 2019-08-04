pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''#!/bin/bash
virtualenv --python=python3.7 venv
source venv/bin/activate

python3 setup.py install'''
      }
    }
    stage('Test') {
      steps {
        sh 'python3 setup.py test'
      }
    }
  }
}