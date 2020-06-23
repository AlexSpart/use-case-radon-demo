pipeline {
    agent { docker { image 'python:3.5.1' } }
    triggers {
        githubPush()
    }    
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                echo 'ok Vbbbfjvre mlk'
            }
        }
    }
}
