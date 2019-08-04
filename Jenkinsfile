pipeline {
  agent any
  stages {
    stage('build-and-test') {
      steps {
        sh '''#!/bin/bash
virtualenv --python=python3.7 venv
source venv/bin/activate

python3 setup.py install
python3 setup.py test'''
      }
    }
  }
}