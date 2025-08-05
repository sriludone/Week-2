pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/sriludone/Week-2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image using Dockerfile
                    dockerImage = docker.build("myapp-image")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the image
                    dockerImage.run()
                }
            }
        }

        stage('Cleanup') {
            steps {
                // Optional: remove all stopped containers
                sh 'docker container prune -f'
            }
        }
    }
}
