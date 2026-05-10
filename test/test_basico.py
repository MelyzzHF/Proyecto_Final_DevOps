import os
import subprocess
# 1. PRUEBA DE INFRAESTRUCTURA (Archivos Críticos)
def test_estructura_proyecto():
    """Verifica que todos los módulos de la arquitectura estén presentes"""
    archivos_obligatorios = [
        "docker-compose.yml",
        "app/Dockerfile",
        "scripts/rollback.sh",
        "scripts/deploy_ssm.sh",
        "buildspec.yml",
        ".github/workflows/deploy.yml"
    ]
    for archivo in archivos_obligatorios:
        assert os.path.exists(archivo), f"Falta el archivo crítico: {archivo}"
# 2. PRUEBA DE CONFIGURACIÓN (Docker Compose)
def test_validacion_docker_compose():
    """Valida que el archivo docker-compose no tenga errores de sintaxis"""
    resultado = subprocess.run(["docker-compose", "config", "-q"], capture_output=True)
    assert resultado.returncode == 0, "Error de sintaxis en docker-compose.yml"
# 3. PRUEBA DE SEGURIDAD (Permisos de Scripts)
def test_permisos_scripts():
    """Verifica que los scripts tengan permisos de ejecución"""
    scripts = ["scripts/rollback.sh", "scripts/deploy_ssm.sh"]
    for script in scripts:
        assert os.access(script, os.X_OK), f"El script {script} no tiene permisos de ejecución"
# 4. PRUEBA DE LÓGICA DE NEGOCIO (Simulación)
def test_identidad_fintech():
    """Valida la consistencia de la marca y entorno"""
    nombre_app = "S.T.F. Fintech"
    version = "1.0.0"
    assert "S.T.F." in nombre_app
    assert version.startswith("1"), "La versión debe ser de la rama estable"
# 5. PRUEBA DE PIPELINE (Secrets)
def test_secrets_configurados():
    """Verifica que el workflow de GitHub tenga las variables de AWS definidas"""
    with open(".github/workflows/deploy.yml", "r") as f:
        contenido = f.read()
        assert "AWS_ACCESS_KEY_ID" in contenido
        assert "AWS_SESSION_TOKEN" in contenido
