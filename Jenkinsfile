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
                    // Use credentials to log in
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', 
                                                     passwordVariable: 'DOCKER_PWD', 
                                                     usernameVariable: 'DOCKER_USER')]) {
                        
                        // Log in
                        sh "echo $DOCKER_PWD | docker login -u $DOCKER_USER --password-stdin"
                        
                        // Build
                        sh "docker build -t your-docker-username/ml-app:${env.BUILD_ID} ."
                        
                        // Push
                        sh "docker push your-docker-username/ml-app:${env.BUILD_ID}"
                        
                        //  Tag as latest
                        sh "docker tag your-docker-username/ml-app:${env.BUILD_ID} your-docker-username/ml-app:latest"
                        sh "docker push your-docker-username/ml-app:latest"
                        
                        // Logout
                        sh "docker logout"
                    }
                }
            }
        }
    }
}