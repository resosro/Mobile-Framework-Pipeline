
pipeline{
    // Does agent {label 'Selenium'} work here? or does it have to be 
    // node {label 'Selenium '}
    agent {label 'RAppsDesktop10'}

    parameters{
        choice(name: "mobile_app", choices: ['Earth Mobile', "ArcGIS Mobile"], description: 'Select which mobile app to run')
        choice(name: "phone_version", choices: ["Pixel 4"], description: "Select which one to be used")
        // choice("phone_version", choices: ['Pixel 4'],defaultValue: 'Pixel 4', description: 'Select which phone version')
        // choice("android_os ", choices: ['11.0'],defaultValue: '11.0', description: 'Select which version of Android the test will take place on')
        // choice("portal_os", choices: ['Windows','Linux'],defaultValue: 'Windows', description: 'Portal Operating System')
        // choice("portal_version", choices: ['1090', '1091', '1100'],defaultValue: '1100', description: 'Portal Version')
        // choice("security_type", choices: ['LDAP', 'IWA', 'PKI','BI','SAML'],defaultValue: 'BI', description: 'Security type')
    }

    options{
        timeout(time: 1, unit: 'SECONDS')
    }

    stages{

        stage("build"){
            steps{
                // start 
                echo "initializing the jenkins file ${params.mobile_app}"
                
            }
            
        }

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
