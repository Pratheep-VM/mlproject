pipeline {
    agent any // Tells Jenkins to run this on any available executor

    stages {
        stage('Checkout') {
            steps {
                // Jenkins automatically checks out code if configured via SCM
                echo 'Checking out code from repository...'
            }
        }
        stage('Build') {
            steps {
                echo 'Building the application...'
                
            }
        }
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                // Example: sh 'npm test'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}