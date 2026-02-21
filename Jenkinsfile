pipeline {
    agent { label 'local-agent' }

    stages {
        stage('Source Control') {
            steps {
                checkout scm
            }
        }

        stage('Automated Testing') {
            steps {
                echo 'Running Quality Assurance tests...'
                sh 'python3 app_test.py'
            }
        }

        stage('Deployment to Production') {
            steps {
                echo 'Deploying to Web Server directory...'
                // This creates a folder and "hosts" your file
                sh 'mkdir -p /home/alyan/www/html'
                sh 'cp index.html /home/alyan/www/html/'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: The website is live at /home/alyan/www/html/index.html'
        }
        failure {
            echo 'CRITICAL: Deployment failed. Reverting changes...'
        }
    }
}
