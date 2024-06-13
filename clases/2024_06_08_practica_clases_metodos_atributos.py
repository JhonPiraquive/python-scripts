class Vulnerabilidad:
    nombre = ''
    severidad = ()
    descripcion = ''
    recomendacion = ''

    def __init__(self, nombre: str, severidad: str, descripcion: str):
        self.nombre = nombre
        if (self.es_severidad_valida(severidad) == False):
            raise print('La severidad no se encuentra dentro de los posibles valores ("Baja", "Media", "Alta", "Crítica")')
        else:
            self.severidad = severidad
        self.descripcion = descripcion

    def es_severidad_valida(self, severidad: str):
        return severidad in ("Baja", "Media", "Alta", "Crítica")
    
    def mostrar_info(self):
        print('\n------ Información de la vulnerabilidad ------\n')
        print(f'Nombre: {self.nombre}')
        print(f'Severidad: {self.severidad}')
        print(f'Descripción: {self.descripcion}')
        
    def recomendar_acciones(self):
        recomendaciones = {
            'Crítica': 'Aplicar parches de seguridad inmediatamente y revisar sistemas afectados.',
            'Alta': 'Realizar una auditoría de seguridad y aplicar medidas correctivas lo antes posible.',
            'Media': 'Monitorizar la actividad del sistema y planificar la aplicación de parches.',
            'Baja': 'Mantener bajo observación y revisar en el próximo ciclo de actualización.'
        }

        if (self.recomendacion == ''):
            self.recomendacion = recomendaciones.get(self.severidad)

        print(f'Acción recomendada: {self.recomendacion}')
        
        
registro_vulnerabilidades = [
    Vulnerabilidad('SQL Injection', 'Alta', 'Permite la ejecución de consultas SQL no autorizadas.'),
    Vulnerabilidad('XSS', 'Media', 'Permite la ejecución de scripts en el navegador del usuario.'),
    Vulnerabilidad('Desbordamiento de Buffer', 'Crítica', 'Permite la ejecución arbitraria de código.'),
]

for vulnerabilidad in registro_vulnerabilidades:
    vulnerabilidad.mostrar_info()
    vulnerabilidad.recomendar_acciones()