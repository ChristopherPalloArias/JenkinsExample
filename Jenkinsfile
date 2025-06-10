pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
        GEMINI_API_KEY = credentials('GEMINI_API_KEY')
    }

    stages {
        stage('Clonar repo') {
            steps {
                git 'https://github.com/ChristopherPalloArias/JenkinsExample.git'
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
                // Levantar FastAPI en segundo plano y esperar que responda
                sh 'nohup ./venv/bin/uvicorn backend.main:app --host 127.0.0.1 --port 8000 &'
                sh 'for i in {1..10}; do curl -s http://127.0.0.1:8000 && break || sleep 1; done'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                // Correr pytest y guardar resultados en formato JUnit para reporte
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
            echo '❌ La API no pasó el control de calidad. Revisa errores en el reporte.'
        }
    }
}