from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Soluciones Tecnológicas del Futuro</title>
    <style>
        body { font-family: sans-serif; text-align: center; background-color: #f0f4f8; margin: 0; padding: 0; }
        .container { margin-top: 50px; padding: 40px; background: white; display: inline-block; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border: 1px solid #d1d9e0; }
        h1 { color: #2c3e50; margin-bottom: 20px; }
        p { color: #7f8c8d; font-size: 1.1rem; line-height: 1.6; }
        .success { color: #27ae60; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>S.T.F. - Plataforma Financiera</h1>
        <p>Estado del Despliegue: <span class="success">Exitoso (CI/CD)</span></p>
        <p>Entorno: <strong>AWS Cloud9 + Docker</strong></p>
        <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
        <small style="color: #bdc3c7;">Proyecto: Soluciones Tecnológicas del Futuro</small>
    </div>
</body>
</html>
''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
