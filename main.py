from idlelib.macosx import addOpenEventSupport

from flask import Flask, jsonify, request


app  = Flask(__name__)

alunos = [
    {"Id": 1, "nome": "Ana", "curso": "Tecnico em Informatica"},
    {"Id": 2, "nome": "Bruno", "curso": "Tecnico em Desenvovimento de Sistemas"},
    {"Id": 3, "nome": "Carla", "curso": "Tecnico em Informatica"}
]

tarefas = [
    {
     "Id": 1,
     "titulo": "Estudar Flask",
     "descricao": "Criar minha primeira API",
     "concluida": False
    },
    {
    "Id": 2,
    "titulo": "Fazer Exercicios",
    "descricao": "Praticar endpoints da API",
    "concluida": False
    }
]

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Minha primeira API esta funcionando",
        "status": "ok"
                    })
@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "mensagem": "API esta saudavel e funcionando"

    })
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify(alunos)

@app.route('/alunos/<int:id>')
def buscar_aluno(id):
    for aluno in alunos:
        if aluno["Id"] == id:
            return jsonify(aluno)
    return jsonify({"erro": "Aluno nao encontrado"}), 404

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas/<int:id>', methods=['GET'])
def buscar_tarefas(id):
    for tarefa in tarefas:
        if tarefa["Id"] == id:
            return jsonify(tarefa)
        return jsonify({"erro": "Tarefa nao encontrado"}), 404

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado foi enviado"}), 400

    if "titulo" not in dados or "descricao" not in dados:
        return jsonify({"erro": "Os campos 'titulo' e 'descricao' sao obrigatorios"}), 400

    nova_tarefa={
        "Id": len(tarefas)+1,
        "titulo": dados["titulo"],
        "descricao": dados["descricao"],
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201
@app.route('/alunos', methods=['POST'])
def criar_alunos():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado foi enviado"}), 400

    if "nome" not in dados or "curso" not in dados:
        return jsonify({"erro": "Os campos 'nome' e 'curso' sao obrigatorios"}), 400

    novo_aluno = {
        "Id": len(alunos)+1,
        "nome": dados['nome'],
        "curso": dados['curso']
    }

    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201

@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefas(id):
    dados = request.get_json()

    campos_obrigatorios = ["titulo", "descricao", "concluida"]
    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"erro": f"Campo {campo} e obrigatorio"}), 400
    for tarefa in tarefas:
        if tarefa["Id"] == id:
            tarefa["titulo"] = dados["titulo"]
            tarefa["descricao"] = dados["descricao"]
            tarefa["concluida"] = dados["concluida"]

            return jsonify(tarefa), 201

    return jsonify({"erro": "Nao encontrado"}), 404
###########
@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_alunos(id):
    dados_alunos = request.get_json()

    campos_obrigatorios = ["nome", "curso"]
    for campo in campos_obrigatorios:
        if campo not in dados_alunos:
            return jsonify({"erro": f"Campo {campo} e obrigatorio"}), 400
    for aluno in alunos:
        if aluno["Id"] == id:
            aluno["nome"]= dados_alunos["nome"]
            aluno["curso"]= dados_alunos["curso"]
            return jsonify(aluno), 201

    return jsonify({"erro": "ID aluno Nao encontrado"}), 404

@app.route('/tarefas/<int:id>', methods=['PATCH'])
def atualizar_campo_tarefas(id):
    dados_tarefas = request.get_json()

    for tarefa in tarefas:
        if tarefa["Id"] == id:
            if "titulo" in dados_tarefas:
                tarefa["titulo"] = dados_tarefas["titulo"]

            if "descricao" in dados_tarefas:
                tarefa["descricao"] = dados_tarefas["descricao"]

            if "concluida" in dados_tarefas:
                tarefa["concluida"] = dados_tarefas["concluida"]

            return jsonify(tarefa), 201

    return jsonify({"erro": "ID tarefa nao encontrado"}), 404

     #### outra forma - tarefas

@app.route('/tarefas/<int:id>', methods=['PATCH'])
def atualizar_campo_tarefas1(id):
        dados_tarefas = request.get_json()

        for tarefa in tarefas:
            if tarefa["Id"] == id:
                tarefa["titulo"] = dados_tarefas.get("titulo", tarefa["titulo"])
                tarefa["descricao"] = dados_tarefas.get("descricao", tarefa["descricao"])
                tarefa["concluida"] = dados_tarefas.get("concluida", tarefa["concluida"])

                return jsonify(tarefa), 201

        return jsonify({"erro": "ID tarefa nao encontrado"}), 404

### metodo Delete - tarefas

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir_tarefas(id):
    for tarefa in tarefas:
        if tarefa["Id"] == id:
            tarefas.remove(tarefa)

            return jsonify({"mensagem":"tarefa removida com sucesso"}), 200

        return jsonify({"erro": "Id tarefa nao encontrado"}), 400

#### outra forma - alunos
app.route('/alunos/<int:id>', methods=['PATCH'])


def atualizar_campo_alunos(id):
    dados_alunos = request.get_json()

    for aluno in alunos:
                if aluno["Id"] == id:
                    aluno["nome"] in dados_alunos.get("nome", aluno["nome"])
                    aluno["curso"] = dados_alunos.get("nome", aluno["curso"])

                    return jsonify(aluno), 201

                return jsonify({"erro": "ID nome nao encontrado"}), 404

    ### metodo Delete - alunos


@app.route('/alunos/<int:id>', methods=['DELETE'])
def excluir_alunos(id):
    for aluno in alunos:
        if aluno["Id"] == id:
            alunos.remove(aluno)

            return jsonify({"mensagem": "aluno removida com sucesso"}), 200

        return jsonify({"erro": "Id aluno nao encontrado"}), 400

if __name__ == '__main__':
    app.run(debug=True)