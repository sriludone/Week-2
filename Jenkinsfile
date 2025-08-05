pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/sriludone/Week-2.git'
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
                    dockerImage.run()
                }
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker ps -a'
                sh 'docker rm $(docker ps -aq) || true'
            }
        }
    }
}
