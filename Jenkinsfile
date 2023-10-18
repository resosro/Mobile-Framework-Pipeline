/* 
Steps:
Pull from SCM 

Start Appium via CLI
Start Android Studio using WIndows Application Driver
    Windows application driver has to be started to start emulator 
    One file? 
Run Python Script in Jenkins Test stage
Reporting 

*/
pipeline{
    // Does agent {label 'Selenium'} work here? or does it have to be 
    // node {label 'Selenium '}
    agent {label 'RAppsDesktop11'}

    parameters{
        choice(name: "mobile_app", choices: ['Earth Mobile', "ArcGIS Mobile"], description: 'Select which mobile app to run')
        choice(name: "phone_version", choices: ["Pixel 4"], description: "Select which one to be used")
        choice(name: "android_os", choices: ["11.0"], description: "Select the Android OS")
        choice(name: "portal_os", choices: ["Lnx","Windows"], description: "Select the portal OS")
        choice(name: "portal_version", choices: ["11.2"], description: "Select the portal version")
        choice(name: "security_type", choices: ["BI"], description: "Select the security type")


        // choice("phone_version", choices: ['Pixel 4'],defaultValue: 'Pixel 4', description: 'Select which phone version')
        // choice("android_os ", choices: ['11.0'],defaultValue: '11.0', description: 'Select which version of Android the test will take place on')
        // choice("portal_os", choices: ['Windows','Linux'],defaultValue: 'Windows', description: 'Portal Operating System')
        // choice("portal_version", choices: ['1090', '1091', '1100'],defaultValue: '1100', description: 'Portal Version')
        // choice("security_type", choices: ['LDAP', 'IWA', 'PKI','BI','SAML'],defaultValue: 'BI', description: 'Security type')
    }

    options{
        timeout(time: 10, unit: 'SECONDS')
    }

    stages{

        stage("Build"){
            steps{
                bat cmd.exe
                bat 'appium'
                // Assuming that Android Studio is already installed along with all of the apps on the emulator
                // powershell "Invoke-Item 'C:/Program Files/Android/Android Studio/bin/studio64.exe'"


                // powershell "C:/Python372/python.exe framework-main.py"
                // git 


                

                
                
                // echo "initializing the jenkins file ${params.mobile_app}"
                
            }
            
        }

        // Seperate into seperate repos then test seperate application depending on the choice in jenkins
        stage("test"){
            steps{
                echo "deploying application"
            }
        }
        stage("deploy"){
            steps{
                echo "testing something"
            }
        }
    }
}
