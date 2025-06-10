pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
        GEMINI_API_KEY = credentials('GEMINI_API_KEY')
    }

    stages {
        stage('Clonar repo') {
            steps {
                git 'https://github.com/ChristopherPalloArias/PALLO-CHRISTOPHER-EXAMENPARCIALPRACTICO.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Levantar API') {
            steps {
                sh 'nohup ./venv/bin/uvicorn backend.main:app --host 0.0.0.0 --port 8000 & sleep 5'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh './venv/bin/pytest tests/test_api.py --junitxml=report.xml || true'
            }
        }

        stage('Publicar resultados') {
            steps {
                junit 'report.xml'
            }
        }
    }

    post {
        success {
            echo '✅ La API funciona correctamente y pasó el control de calidad.'
        }
        failure {
            echo '❌ La API no pasó el control de calidad. Revisar errores.'
        }
    }
}
