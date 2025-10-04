pipeline {
    agent any
    
    environment {
        // Set Python path and virtual environment
        PYTHONPATH = "${WORKSPACE}"
        VIRTUAL_ENV = "${WORKSPACE}/.venv"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv .venv
                            source .venv/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv .venv
                            .venv\\Scripts\\activate.bat
                            python -m pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running pytest...'
                script {
                    if (isUnix()) {
                        sh '''
                            source .venv/bin/activate
                            pytest --junitxml=test-results.xml --cov=. --cov-report=xml --cov-report=html
                        '''
                    } else {
                        bat '''
                            .venv\\Scripts\\activate.bat
                            pytest --junitxml=test-results.xml --cov=. --cov-report=xml --cov-report=html
                        '''
                    }
                }
            }
        }
    }
    
    post {
        always {
            echo 'Publishing test results and cleanup...'
            
            // Publish test results
            publishTestResults testResultsPattern: 'test-results.xml'
            
            // Publish coverage reports
            publishCoverage adapters: [
                coberturaAdapter('coverage.xml')
            ], sourceFileResolver: sourceFiles('STORE_LAST_BUILD')
            
            // Archive test reports
            archiveArtifacts artifacts: 'htmlcov/**, test-results.xml, coverage.xml', 
                             allowEmptyArchive: true
            
            // Clean workspace
            cleanWs()
        }
        
        success {
            echo 'Pipeline completed successfully!'
        }
        
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
        
        unstable {
            echo 'Pipeline completed with test failures or unstable results.'
        }
    }
}