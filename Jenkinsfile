pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = 'piratheepv20/ml-app' 
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build & Push') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-login') {
                        // Build the image
                        def customImage = docker.build("${DOCKER_IMAGE_NAME}:${env.BUILD_ID}")
                        // Push to Docker Hub
                        customImage.push('latest')
                    }
                }
            }
        }
    }
}