pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Validate Docker Compose') {
            steps {
                sh 'docker compose config'
            }
        }

        stage('Build Images') {
            steps {
                sh 'docker compose build app nginx'
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                docker compose stop app nginx || true
                docker compose rm -f app nginx || true
                docker compose up -d app nginx
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker compose ps'
            }
        }
    }
}
