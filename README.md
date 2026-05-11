
#Proyecto Final DevOps de Melissa Hernandez 

## Descripción
Este proyecto implementa una arquitectura de nube robusta diseñada para una Fintech, enfocándose en la automatización, seguridad y alta disponibilidad mediante servicios de AWS.

##ecnologías Utilizadas
* **Infraestructura:** AWS EC2, CloudFormation.
* **Base de Datos y Almacenamiento:** DynamoDB, Amazon S3.
* **Serverless:** AWS Lambda, API Gateway.
* **Monitoreo:** Amazon CloudWatch (Logs & Alarms), AWS Config.
* **DevOps:** Docker, GitHub Actions, Conventional Commits.

##Seguridad
* **Políticas de IAM:** Uso de LabRole para privilegios mínimos.
* **Network Security:** Security Groups restringidos por IP administrativa.
* **Gobernanza:** Protección de secretos mediante `.gitignore`.

##Monitoreo y Auditoría
* Agente de CloudWatch configurado para rastrear `/var/log/syslog`.
* Alarma de CPU configurada al 80% con notificaciones SNS.
* Logs de auditoría de cambios almacenados en S3.

