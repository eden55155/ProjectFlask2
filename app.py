from flask import Flask, request, render_template
import jenkins

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        username = request.form['username']
        return f'Hello, {username}!'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

def create_jenkins_job(job_name):
    server = jenkins.Jenkins('http://localhost:8080', username='user', password='123456')
    job_config = '''
                   <flow-definition plugin="workflow-job@2.17">
                     <definition class="org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition" plugin="workflow-cps@2.32">
                       <scm class="hudson.plugins.git.GitSCM" plugin="git@3.9.1">
                         <configVersion>2</configVersion>
                         <userRemoteConfigs>
                           <hudson.plugins.git.UserRemoteConfig>
                             <url>https://github.com/eden55155/ProjectFlask2.git</url>
                           </hudson.plugins.git.UserRemoteConfig>
                         </userRemoteConfigs>
                         <branches>
                           <hudson.plugins.git.BranchSpec>
                             <name>*/master</name>
                           </hudson.plugins.git.BranchSpec>
                         </branches>
                         <extensions/>
                       </scm>
                       <scriptPath>Jenkinsfile</scriptPath>
                       <lightweight>true</lightweight>
                     </definition>
                   </flow-definition>
                  '''
    server.create_job(job_name, job_config)

@app.route('/create-job', methods=['POST'])
def create_job():
    job_name = request.form['job_name']
    create_jenkins_job(job_name)
    return f'Successfully created Jenkins job "{job_name}".'