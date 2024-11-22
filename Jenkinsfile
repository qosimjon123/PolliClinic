pipeline {
    agent {
        label "Yuriy"
    }

    environment {
        MYSQLDATABASE = credentials('MYSQLDATABASE')
        MYSQLUSER = credentials('MYSQLUSER')
        MYSQLPASSWORD = credentials('MYSQLPASSWORD')
        MYSQLPASSWORDROOT = credentials('MYSQLPASSWORDROOT')
        SECRETKEYAPP = credentials('SECRETKEYAPP')
        DOCKERHUB = credentials('DockerHub')
    }

    

    stages {
        stage('Download Resources') {
            steps {
                script {
                    sh 'pwd'
                    sh 'rm -rf policlinic'

                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: 'feature']],
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [[$class: 'SubmoduleOption', recursiveSubmodules: true]],
                        userRemoteConfigs: [[url: 'https://github.com/qosimjon123/PolliClinic.git']]
                    ])

                }
            }
        }
        stage('Static testing') {
            steps {
                script {



                    sh 'pipenv install flake8 bandit '
                    sh 'sudo apt install trufflehog -y'




                    sh 'pipenv run flake8 --format=pylint --exit-zero --config=./policlinic/.flake8 ./policlinic > flake8-report.xml'


                    def flake8Output = readFile('flake8-report.xml')
                    if (flake8Output.trim()) {
                        error("Flake8 обнаружил проблемы:\n${flake8Output}")
                    }




                    def result = sh(script: 'pipenv run bandit -r ./policlinic -l -iii --exclude ./policlinic/test', returnStatus: true)

                    if (result == 1) {
                        error("Bandit обнаружил проблемы. Сборка прервана.")
                    }

                    def result2 = sh(script: 'trufflehog filesystem policlinic | grep -v "unverified"', returnStatus: true)

                    if (result2 != 0) {
                        error("trufflehog обнаружил проблемы (Найден пароль в открытом виде). Сборка прервана.")
                    }

                }
            }
            post {
                always {
                    recordIssues(
                        tools: [
                            flake8(pattern: 'flake8-report.xml'),

                        ]
                    )

                }
            }
        }


        stage('Stop, Remove Images & Volumes') {
            steps {
                script {
                    sh 'docker-compose -f policlinic/docker-compose.yaml down --rmi all --volumes'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'pwd'
                    sh 'docker-compose -f policlinic/docker-compose.yaml build --no-cache'
                }
            }
        }
        // stage('Push to DockerHub') {
        //     steps {
        //         script {
        //             sh 'pwd'
        //             // sh 'docker login -u $DOCKERHUB_USR -p $DOCKERHUB_PSW'
        //             // sh 'docker tag policlinic_django noname12/policlinic:v2'
        //             // sh 'docker push noname12/policlinic:v2'
        //         }
        //     }
        // }
        stage('Run the server') {
            steps {
                script {
                    sh 'docker-compose -f policlinic/docker-compose.yaml up -d'
                }
            }
        }
        stage('Config') {
            steps {
                script {
                    sh './policlinic/docker_volumes/beckup_mysql.sh root $MYSQLPASSWORDROOT policlinic_db'
                    sh 'docker exec --tty policlinic_django_1 /bin/bash -c "pipenv run coverage run --source=tests manage.py test --verbosity 2"'
                    sh 'docker exec --tty policlinic_django_1 /bin/bash -c "pipenv run coverage report -m"'


                }
            }
        }
    }
}
