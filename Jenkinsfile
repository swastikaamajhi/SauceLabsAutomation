// pipeline {
//     agent any
//
//     stages {
//       stage('Install Dependencies') {
//           steps {
//               bat 'python -m pip install --upgrade pip'
//               bat 'python -m pip install -r requirements.txt'
//           }
//       }
//
//         stage('Run Tests') {
//             steps {
//                 bat 'pytest --alluredir=allure-results'
//             }
//         }
//     }
// }

// pipeline {
//     agent any
//
//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }
//
//         stage('Check Python') {
//             steps {
//                 bat 'python --version'
//             }
//         }
//
//         stage('Install Dependencies') {
//             steps {
//                 bat 'python -m pip install --upgrade pip'
//                 bat 'python -m pip install -r requirements.txt'
//             }
//         }
//
//         stage('Run Tests') {
//             steps {
//                 bat 'python -m pytest --alluredir=allure-results'
//             }
//         }
//     }
// }

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest --alluredir=allure-results'
            }
        }
    }
}