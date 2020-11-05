pipeline {

agent any

tools {
        maven 'maven'

   }
   
stages {

        stage('checking maven installation') {
   
             steps {
                    sh 'mvn -v'
             }
        }
        
        stage('building java project ') {
        
              steps {
                      
                      sh 'cd jspapp-master ; mvn clean package'
                      sh 'chmod 755 jspapp-master/target/ -R'
              
              }
        }
        
        stage('deploy war file in local docker engine'){
                steps {
                        sh 'docker-compose down ; docker-compose up -d'
                
                }          
                
        }
     
              

  }



}
