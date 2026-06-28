pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh '''
                cd /workspace
                docker compose build app nginx
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                cd /workspace
                docker compose up -d --build app nginx
                '''
            }
        }

        stage('Verify') {
            steps {
                sh '''
                docker ps
                '''
            }
        }
    }
}
