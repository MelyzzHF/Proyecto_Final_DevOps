import boto3
from botocore.exceptions import ClientError
from decimal import Decimal 

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('TransaccionesFintech')
def ejecutar_operaciones_dynamo():
    print("--- Iniciando Gestión Completa de DynamoDB (CRUD) ---")
    id_final = 'TX-2026-MELY'
    id_borrar = 'TX-PROEBA-BORRADO'
    try:
        #INSERTAR REGISTROS (Usando Decimal para el monto)
        print(f"Insertando registros {id_final} y {id_borrar}...")
        table.put_item(Item={
            'transaction_id': id_final, 
            'cliente': 'Estudiante Tecmilenio', 
            'monto': Decimal('7500.50'), 
            'estado': 'Pendiente'
        })
        table.put_item(Item={
            'transaction_id': id_borrar, 
            'cliente': 'Temporal', 
            'monto': Decimal('0'), 
            'estado': 'Para Eliminar'
        })
        print("Registros insertados con éxito.")
        #MODIFICAR REGISTRO
        print(f"Modificando {id_final}...")
        table.update_item(
            Key={'transaction_id': id_final},
            UpdateExpression="set estado = :s, monto = :m",
            ExpressionAttributeValues={
                ':s': 'Aprobado', 
                ':m': Decimal('8000.00') 
            }
        )
        print("Registro modificado correctamente.")
        #LEER
        respuesta = table.get_item(Key={'transaction_id': id_final})
        print(f"Datos actuales en la tabla: {respuesta.get('Item')}")
        #ELIMINAR
        print(f"Eliminando registro de prueba: {id_borrar}...")
        table.delete_item(Key={'transaction_id': id_borrar})
        print(f"Registro {id_borrar} eliminado exitosamente.")

    except ClientError as e:
        print(f"Error de AWS: {e.response['Error']['Message']}")

if __name__ == "__main__":
    ejecutar_operaciones_dynamo()
