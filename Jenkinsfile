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
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', 
                                                     passwordVariable: 'DOCKER_PWD', 
                                                     usernameVariable: 'DOCKER_USER')]) {
                        
                        // Force a clean login.
                        sh "echo $DOCKER_PWD | docker login -u $DOCKER_USER --password-stdin"
                        
                
                        def IMAGE_TAG = "piratheepv20/ml-app:${env.BUILD_ID}"
                        
            
                        sh "docker build -t ${IMAGE_TAG} ."
                        
                
                        sh "docker push ${IMAGE_TAG}"
                        
                        sh "docker logout"
                    }
                }
            }
        }
    }
}