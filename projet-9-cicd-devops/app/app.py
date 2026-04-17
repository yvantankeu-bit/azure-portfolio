from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok", "service": "data-platform-api"})

@app.route('/info')
def info():
    return jsonify({
        "project": "Projet 9 - CI/CD Azure DevOps",
        "stack": "Flask + Azure DevOps + App Service"
    })

if __name__ == '__main__':
    app.run()
