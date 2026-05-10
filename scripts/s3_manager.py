import boto3
BUCKET_NAME = 'bucket-respaldo-fintech-mely'
s3 = boto3.client('s3')

def ejecutar_respaldo_s3():
    file_name = 'reporte_mensual.txt'
    # 1. Crear un archivo de prueba
    with open(file_name, 'w') as f:
        f.write("Reporte de Transacciones Fintech - Confidencial")

    print(f"--- Iniciando carga a S3 en el bucket: {BUCKET_NAME} ---")

    # 2. Automatizar la carga con Boto3
    try:
        s3.upload_file(file_name, BUCKET_NAME, file_name)
        print(f"Archivo '{file_name}' respaldado exitosamente.")

        # 3. Verificar Cifrado y Disponibilidad
        response = s3.head_object(Bucket=BUCKET_NAME, Key=file_name)
        cifrado = response.get('ServerSideEncryption', 'No detectado')
        version = response.get('VersionId', 'No disponible')

        print(f"Verificación de Seguridad:")
        print(f"   - Cifrado en reposo: {cifrado}")
        print(f"   - ID de Versión (Backup): {version}")

    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    ejecutar_respaldo_s3()
