pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'apt-get update'
                sh 'apt-get install python3'
                sh 'pip install django'
                sh 'pip install djangorestframework'
                sh 'pip install django-cors-headers'
            }
        }
        stage('Start MySQL') {
            steps {
                sh 'mysql -u root -p < create_db.sql'
            }
        }
        stage('Run Migrations') {
            steps {
                sh 'cd base'
                sh 'python manage.py makemigrations'
                sh 'python manage.py migrate'
            }
        }
        stage('Run Server') {
            steps {
                sh 'python manage.py runserver'
            }
        }
        stage('Install Frontend Dependencies') {
            steps {
                sh 'cd frontend'
                sh 'npm install'
                sh 'npm start'
            }
        }
    }
}
