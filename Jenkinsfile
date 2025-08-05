pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/sriludone/Week-2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("registration:v1")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker rm -f registration-container || true'
                    dockerImage.run('-d -p 5000:5000 --name registration-container')
                }
            }
        }
    }
}
