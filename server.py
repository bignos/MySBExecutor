import flask
import flask_restful
import json
import subprocess

# -[ Configuration ]-
PORT   = '1979'
BASH   = '/bin/bash'
SCRIPT = './script.bsh'
# -------------------

app = flask.Flask('MySBExecutor')
api = flask_restful.Api(app)

class Executor(flask_restful.Resource):
    def get(self):
        result = subprocess.run([BASH, SCRIPT], stdout=subprocess.PIPE)
        if result.returncode == 0:
            result_stdout = result.stdout.decode('utf-8')
            return result_stdout
        else:
            if result.stderr:
                print("{}".format(result.stderr))
            elif result.stdout:
                print("{}".format(result.stdout))

            return 'ERROR'

api.add_resource(Executor, '/executor')

if __name__ == '__main__':
    app.run(port=PORT)
