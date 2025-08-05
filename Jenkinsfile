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
                    dockerImage = docker.build("myapp-image")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    bat "docker run --rm myapp-image"
                }
            }
        }

        stage('Cleanup') {
            steps {
                bat 'docker container prune -f'
            }
        }
    }
}
