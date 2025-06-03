from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/diagnostico", methods=["POST"])
def diagnostico():
    data = request.json
    febre = data.get("febre")
    tosse = data.get("tosse")
    corpo = data.get("corpo")
    respirar = data.get("respirar")
    olfato = data.get("olfato")

    # Se todos forem 'n', retorna que não há sintomas
    if all(resposta == "n" for resposta in [febre, tosse, corpo, respirar, olfato]):
        return jsonify({"resposta": "✅ Nenhuma doença detectada."})

    # Casos com sintomas
    if febre == "s" and tosse == "s" and respirar == "s":
        return jsonify({"resposta": "⚠️ Suspeita de infecção respiratória. Procure atendimento médico."})
    if febre == "s" and corpo == "s":
        return jsonify({"resposta": "⚠️ Pode ser um quadro viral. Fique em repouso e hidrate-se."})
    if olfato == "s":
        return jsonify({"resposta": "⚠️ Perda de olfato pode estar associada a virose. Fique atento."})

    # Caso tenha sintomas, mas nenhum caso mais crítico identificado
    return jsonify({"resposta": "ℹ️ Sintomas leves detectados. Mantenha repouso e observe a evolução."})

if __name__ == "__main__":
    app.run(debug=True)
