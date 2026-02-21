pipeline {
    agent { label 'local-agent' }

    stages {
        stage('Checkout') {
            steps {
                checkout scm //automatically pulls code from your github repository
            }
        }

        stage('Testing') {
            when{
                expression{
                    BRANCH_NAME='main'
                }

            }
            steps {
                echo 'Performing Syntax Check...'
                // This checks if the python code is valid without actually running the full script
                sh 'python3 -m py_compile jenkins.py' // Standard Python syntax check
                echo 'Testing Complete: No syntax errors found.'
            }
        }

        stage('Run Script') {
            steps {  
                echo 'Executing main logic...'
                sh 'python3 jenkins.py'
            }
        }

        stage('Deployment') {
            steps {
                echo 'Deploying application...'
                // Creating a "production" directory and copying the script there
                sh 'mkdir -p /home/alyan/production_app'
                sh 'cp jenkins.py /home/alyan/production_app/'
                echo 'Application successfully deployed to /home/alyan/production_app'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the specific stage logs.'
        }
    }
}
