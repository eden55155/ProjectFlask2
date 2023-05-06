import jenkins


def create_jenkins_job_and_user(job_name, user_name, user_token):
    server = jenkins.Jenkins('http://localhost:8080', username=user_name, password=user_token)
    job_config = '<?xml version="1.0" encoding="UTF-8"?><project><builders/><publishers/><buildWrappers/></project>'
    server.create_job(job_name, job_config)
    server.create_user(user_name)


@app.route('/create-job', methods=['POST'])
def create_job():
    job_name = request.form['job_name']
    user_name = request.form['user_name']
    user_token = request.form['user_token']
    create_jenkins_job_and_user(job_name, user_name, user_token)
    return f'Successfully created Jenkins job "{job_name}" and user "{user_name}".'
