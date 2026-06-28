pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Validate Docker Compose') {
            steps {
                sh 'docker compose config'
            }
        }

        stage('Deploy Application') {
            steps {
                sh 'docker compose down'
                sh 'docker compose up -d --build'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
