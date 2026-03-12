pipeline {
    agent any
    
    stages {
        stage('Build & Push') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', 
                                                     passwordVariable: 'DOCKER_PWD', 
                                                     usernameVariable: 'DOCKER_USER')]) {
                        
                        // Log in to Docker Hub
                        sh "echo $DOCKER_PWD | docker login -u $DOCKER_USER --password-stdin"
                        
                        // Build your image
                        sh "docker build -t your-dockerhub-username/your-app-name:latest ."
                        
                        // Push your image
                        sh "docker push your-dockerhub-username/your-app-name:latest"
                        
                        // Logout 
                        sh "docker logout"
                    }
                }
            }
        }
    }
}