pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Validate Docker Compose') {
            steps {
                sh '''
                cd $WORKSPACE
                docker compose config
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                cd $WORKSPACE
                docker compose build
                '''
            }
        }
    
        stage('Deploy Application') {
            steps {
                sh '''
                cd $WORKSPACE
                docker compose down
                docker compose up -d --build
                '''
             }
         }

        stage('Verify Docker Images') {
            steps {
                sh 'docker images'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
