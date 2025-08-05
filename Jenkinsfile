pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/sriludone/Week-2.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t registration:v1 .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker rm -f registration-container || exit 0'
                bat 'docker run -d -p 5000:5000 --name registration-container registration:v1'
            }
        }
    }
}
