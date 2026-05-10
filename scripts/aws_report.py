import boto3
from datetime import datetime, timedelta

def generar_reporte_proyecto_final():
    region = 'us-east-1'
    ec2 = boto3.client('ec2', region_name=region)
    s3 = boto3.client('s3', region_name=region)
    cw = boto3.client('cloudwatch', region_name=region)
    asg = boto3.client('autoscaling', region_name=region)

    print("-----------------------------------------------------------------------")
    print("REPORTE DE INFRAESTRUCTURA: SOLUCIONES TECNOLÓGICAS DEL FUTURO")
    print(f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-----------------------------------------------------------------------")

    # --- 1. LISTADO DE INSTANCIAS Y MÉTRICAS (CloudWatch) ---
    print("\nMONITOREO DE INSTANCIAS EC2")
    try:
        instancias = ec2.describe_instances()
        hay_instancias = False
        for reserva in instancias.get('Reservations', []):
            for inst in reserva['Instances']:
                hay_instancias = True
                id_i = inst['InstanceId']
                estado = inst['State']['Name']
                tipo = inst['InstanceType']

                # Obtener métrica de CPU de los últimos 30 minutos
                metric = cw.get_metric_statistics(
                    Namespace='AWS/EC2',
                    MetricName='CPUUtilization',
                    Dimensions=[{'Name': 'InstanceId', 'Value': id_i}],
                    StartTime=datetime.utcnow() - timedelta(minutes=30),
                    EndTime=datetime.utcnow(),
                    Period=300,
                    Statistics=['Average']
                )

                cpu = f"{metric['Datapoints'][0]['Average']:.2f}%" if metric['Datapoints'] else "Sin datos"
                print(f"ID: {id_i} | Tipo: {tipo} | Estado: {estado} | CPU (Avg 30m): {cpu}")

        if not hay_instancias:
            print("No se encontraron instancias EC2 activas.")
    except Exception as e:
        print(f"Error al listar EC2/CloudWatch: {e}")

    # --- BUCKETS S3 Y SUS OBJETOS ---
    print("\nALMACENAMIENTO EN S3")
    try:
        buckets = s3.list_buckets()
        if not buckets['Buckets']:
            print("No hay buckets en la cuenta.")
        else:
            for b in buckets['Buckets']:
                nombre_b = b['Name']
                print(f" Bucket: {nombre_b}")

                # Listar objetos dentro del bucket
                objetos = s3.list_objects_v2(Bucket=nombre_b)
                if 'Contents' in objetos:
                    for obj in objetos['Contents']:
                        print(f"   - Objeto: {obj['Key']} | Tamaño: {obj['Size']} bytes")
                else:
                    print("   - (Bucket vacío)")
    except Exception as e:
        print(f"Error al listar S3: {e}")

    # --- GESTIÓN DE AUTO SCALING ---
    print("\nCONFIGURACIÓN DE AUTO SCALING")
    try:
        grupos = asg.describe_auto_scaling_groups()
        if not grupos['AutoScalingGroups']:
            print(" No hay Grupos de Auto Scaling configurados.")
        else:
            for g in grupos['AutoScalingGroups']:
                nombre_asg = g['AutoScalingGroupName']
                cap_deseada = g['DesiredCapacity']
                cap_min = g['MinSize']
                cap_max = g['MaxSize']

                print(f" ASG: {nombre_asg}")
                print(f"   - Capacidad: Deseada({cap_deseada}) Min({cap_min}) Max({cap_max})")

    except Exception as e:
        print(f" > Error al consultar Auto Scaling: {e}")

    print("FIN DEL REPORTE")
    print("---------------------------------------------------------")

if __name__ == '__main__':
    generar_reporte_proyecto_final()
