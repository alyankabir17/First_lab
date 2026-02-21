pipeline {
    agent { label 'local-agent' }
    options {
        // Keeps only the last 10 builds and deletes anything older than 7 days
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '5', daysToKeepStr: '7'))
        
        // Prevents multiple builds of the same job from running at the same time
        disableConcurrentBuilds()
        
        // Adds a timestamp to every line in the console log
        timestamps()
    }
    tools{
        maven 'Maven'
        gradle 'Gradle'
        jdk 'Jdk'
    }
    parameters {
        string(name:'' ,defaultValue: '', description: '')
        choice(name:'' ,choices :['',''] , description: '')
        booleanparam(name:'executeTests' ,defaultValue: '', description: '')
    stages {
        stage('Source Control') {
            
            steps {
                checkout scm
            }
        }

        stage('Automated Testing') {
            when {
                expression {
                    params.executeTests
                }
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
                echo " deploying version ${params.VERSION} "
            }
        }
        stage('Example') {
            steps {
                echo 'Cleaning up build history automatically...'
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
