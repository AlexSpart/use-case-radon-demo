pipeline {
    agent any
        environment {
            GMT_DOCKER_COMPOSE_URL="https://github.com/radon-h2020/radon-gmt/blob/project/radon/docker-compose.yml"
            GMT_HTTP_PORT="18080"
            PARTICLES_URL="https://github.com/radon-h2020/radon-particles.git"
            PARTICLES_BRANCH="master"
            PARTICLES_DIR="/tmp/radon-particles"
            CTT_DOCKER_NAME="RadonCTT"
            CTT_SERVER_DOCKER="radonconsortium/radon-ctt"
            CTT_VOLUME="/tmp/RadonCTT"
            CTT_PORT="18080"
            CTT_EXT_PORT="7999"
            CTT_ENDPOINT="http://localhost:${CTT_EXT_PORT}/RadonCTT"
            CTT_RESULT_FILE="/tmp/result.zip"
            REPO_DEMO_URL="https://github.com/AlexSpart/use-case-radon-demo.git"
            REPO_DEMO_BRANCH="master"
            REPO_DEMO_DIR="/tmp/repo-demo-dir"
            SUT_CSAR_FN="sut.csar"
            SUT_CSAR="/tmp/${SUT_CSAR_FN}"
            TI_CSAR_FN="ti.csar"
            TI_CSAR="/tmp/${TI_CSAR_FN}"
            }
    stages {
        stage('Install requirements') {
            environment {
                ENV_VAR2 = "exmp"
            }
            steps {
                
                sh 'python3 -m pip install docker jq ansible --user'
            }
        }
        stage('\u27A1 Verify Docker') {
            steps {
                sh 'docker run --rm hello-world'
            }
        }
        stage('CALL CTT') {
            environment {
                NAME="CTT-master"
                CTT_SERVER_DOCKER_TAG="latest"
                SUT_EXPORT_URL="http://127.0.0.1:${GMT_HTTP_PORT}/winery/servicetemplates/radon.blueprints/SockShopTestingExample/?yaml&csar"
                SUT_DEPLOYMENT_PORT="80"
                SUT_DEPOYMENT_URL="http://localhost:${SUT_DEPLOYMENT_PORT}"
                TI_EXPORT_URL="http://127.0.0.1:${GMT_HTTP_PORT}/winery/servicetemplates/radon.blueprints.testing/JMeterMasterOnly/?yaml&csar"
                TI_DEPLOYMENT_PORT="5000"
                TI_DEPLOYMENT_URL="http://localhost:${TI_DEPLOYMENT_PORT}"
                }
            steps {
                sh 'mkdir ${CTT_VOLUME}'
                sh 'docker run --rm --name "${CTT_DOCKER_NAME}" -d -p "127.0.0.1:${CTT_EXT_PORT}:${CTT_PORT}" -v /var/run/docker.sock:/var/run/docker.sock -v "${CTT_VOLUME}:/tmp/RadonCTT" "${CTT_SERVER_DOCKER}:${CTT_SERVER_DOCKER_TAG}"'
                sh 'git clone --single-branch --branch "${REPO_DEMO_BRANCH}" "${REPO_DEMO_URL}" "${REPO_DEMO_DIR}"'

                // CTT: Create Project
                sh 'export CTT_PROJECT_UUID=$(./curl_uuid.sh \"${CTT_ENDPOINT}/project\" \"{\\\"name\\\":\\\"use-case-radon-demo\\\",\\\"repository_url\\\":\\\"${REPO_DEMO_URL}\\\"}\")'
                sh 'echo "$CTT_PROJECT_UUID"'
                // CTT: Create Test-Artifact
                sh 'export CTT_TESTARTIFACT_UUID=$(./curl_uuid.sh \"${CTT_ENDPOINT}/testartifact\" \"{\\\"project_uuid\\\":\\\"${CTT_PROJECT_UUID}\\\",\\\"sut_tosca_path\\\":\\\"radon-ctt/${SUT_CSAR_FN}\\\",\\\"ti_tosca_path\\\":\\\"radon-ctt/${TI_CSAR_FN}\\\"}\")'
                // CTT: Create Deployment
                sh 'export CTT_DEPLOYMENT_UUID=$(./curl_uuid.sh  \"${CTT_ENDPOINT}/deployment\" \"{\\\"testartifact_uuid\\\":\\\"${CTT_TESTARTIFACT_UUID}\\\"}\")'
                // Give deployments some time to succeed.
                sh 'sleep 120'
                sh 'echo \"DEPLOYMENT_UUID: ${CTT_DEPLOYMENT_UUID}\"'
                
                sh 'docker stop RadonCTT'
            }
        }
        stage('Test functionality') {
            environment {
                ENV_VAR3 = "exmp"
            }
            steps {
                sh 'echo "finisshh"'

            }
        }
    }
}
