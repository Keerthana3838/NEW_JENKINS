pipeline {
    agent any
    
    stages {
        stage('Checkout code') {
            steps {
                git credentialsid : 'PATDemo' , url : 'https://github.com/Keerthana3838/NEW_JENKINS.git' , branch : 'master'

            }
        }
        stage('Install dependencies') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install pytest
                '''
            }
        }
        stage('Run python script') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest test.py
                    '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application'
                bat '''
                    call venv\\Scripts\\activate
                    python sub.py
                    '''
            }
        }

    }
    post {
        success {
            echo 'Pipeline succeeded'
        }
        failure {
            echo 'pipeline failed'
        }
    }

}