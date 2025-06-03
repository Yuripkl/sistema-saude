from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = ''
    if request.method == 'POST':
        sintomas = {
            'febre': request.form.get('febre'),
            'tosse': request.form.get('tosse'),
            'coriza': request.form.get('coriza'),
            'falta_ar': request.form.get('falta_ar'),
            'dor_cabeca': request.form.get('dor_cabeca'),
            'manchas': request.form.get('manchas'),
            'espirros': request.form.get('espirros'),
            'coceira': request.form.get('coceira'),
            'dor_corpo': request.form.get('dor_corpo'),
            'nausea': request.form.get('nausea'),
            'fadiga': request.form.get('fadiga')
        }

        # Regras simples de diagnóstico
        if (
            sintomas['febre'] == 'sim' and
            sintomas['tosse'] == 'sim' and
            sintomas['falta_ar'] == 'sim' and
            sintomas['fadiga'] == 'sim'
        ):
            resultado = '⚠️ Possível COVID-19. Procure orientação médica.'
        elif (
            sintomas['espirros'] == 'sim' and
            sintomas['coriza'] == 'sim' and
            sintomas['tosse'] == 'sim'
        ):
            resultado = 'ℹ️ Pode ser um resfriado comum.'
        elif (
            sintomas['manchas'] == 'sim' and
            sintomas['febre'] == 'sim'
        ):
            resultado = '⚠️ Possível caso de dengue. Busque atendimento médico.'
        elif (
            sintomas['coceira'] == 'sim' and
            sintomas['manchas'] == 'sim'
        ):
            resultado = 'ℹ️ Pode ser uma reação alérgica.'
        elif (
            sintomas['nausea'] == 'sim' and
            sintomas['fadiga'] == 'sim' and
            sintomas['dor_corpo'] == 'sim'
        ):
            resultado = 'ℹ️ Sintomas inespecíficos. Acompanhe e, se persistirem, procure um médico.'
        else:
            resultado = '✅ Nenhuma doença detectada.'

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
