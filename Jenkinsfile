pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t your_image_name:latest .'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'docker run --rm your_image_name:latest python -m unittest tests.py'
            }
        }
    }
}