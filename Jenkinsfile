pipeline{
    agent any
    stages{
        stage("Clone Repository"){
            steps{
                git url:"https://github.com/ShetManoj/weather-app.git", branch: "main"
                echo "Code clonning form github repo successful"
            }
        }
        stage("Build Image"){
            steps{
                sh 'docker build -t weather-app:latest .'
                echo "Image built successfully"
            }
        }
        stage("Run Image"){
            steps{
                sh 'docker run -d -p 5000:5000 weather-app:latest'
                echo "Application deployed successfully"
            }
        }
        
    }
}