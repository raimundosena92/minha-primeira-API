from flask import Flask, jsonify


app  = Flask(__name__)

alunos = [
    {"Id": 1, "nome": "Ana", "curso": "Tecnico em Informatica"},
    {"Id": 2, "nome": "Bruno", "curso": "Tecnico em Desenvovimento de Sistemas"},
    {"Id": 3, "nome": "Carla", "curso": "Tecnico em Informatica"}
]
@app.route('/')
def home():
    return jsonify({
        "message": "Minha primeira API esta funcionando",
        "status": "ok"
                    })
@app.route('/health')
def health():
    return jsonify({
        "status": "ok",
        "mensagem": "API esta saudavel e funcionando"

    })
@app.route('/alunos')
def listar_alunos():
    return jsonify(alunos)

@app.route('/alunos/<int:id>')
def buscar_aluno(id):
    return jsonify(alunos)
@app.route('/alunos/<int:id>')
def buscar_aluno(id):
    for aluno in alunos:
        if aluno["Id"] == id:
            return jsonify(aluno)
    return jsonify({"erro": "Aluno nao encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)