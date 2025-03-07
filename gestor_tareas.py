class Tarea:
    def __init__(self, id, titulo, descripcion = "", completada=False, prioridad="normal"):
        # Asignamos los valores basico de la tarea
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = completada
        
        # Definimos la prioridades validas para validacion.
        prioridades_validas = ["baja", "normal", "alta"]
        
        # Verificar que la prioridad proporcionada sea valida
        
        if prioridad not in prioridades_validas:
            raise ValueError(f"Prioridad no valida. Debe ser un de: {prioridades_validas}")
        
        # Asignamos la prioridad si paso la validacion
        self.prioridad = prioridad
    
    def __eq__(self, other):
        if not isinstance(other, Tarea):
            return False
        return self.id == other.id

# La clase GestorTareas maneja una coleccion de objetos Tarea
class GestorTareas:
    def __init__(self):
            #Lista para almacenar todas las tareas
            self.tareas = []
        
            # Contador para asignar ID's unicos a las tareas
            self.contador_id = 0

    def agregar_tarea(self, titulo, descripcion="", prioridad="normal"):
        #Incrementamos el contador para obtener un nuevo ID unico
        self.contador_id += 1
        
        #Creamos la nueva tarea con los parametros proporcionados
        nueva_tarea = Tarea(self.contador_id, titulo, descripcion, False, prioridad)
        
        # Añadimos la tarea a nuestra lista
        self.tareas.append(nueva_tarea)
        
        #Retornamos la tarea creada para que pueda ser utilizado
        return nueva_tarea
    
    def eliminar_tarea(self, tarea_id):
        # Inicializamos la variable para almacenar la tarea a eliminar (si se encuentra)
        tarea_eliminado = None

        # Recorremos la lista de tareas para buscar la tarea con el ID especificado
        for tarea in self.tareas:
            if tarea.id == tarea_id:
                tarea_eliminado = tarea  # Se encuentra la tarea a eliminar
                break  # Salimos del bucle, ya no es necesario seguir buscando

        # Si se encontró la tarea, se eliminar dentro de la lista
        if tarea_eliminado:
            self.tareas.remove(tarea_eliminado)
            return tarea_eliminado  # Retornamos la tarea eliminada
        # Si no se encontró la tarea, retornamos None
        return None

    def buscar_tarea(self, tarea_id):
        ## Buscar una tarea en la lista por su ID.
        for tarea in self.tareas:
            if tarea.id == tarea_id:
                return tarea  # Se retorna la tarea encontrada
        return None  # Si no se encontró ninguna tarea, se retorna None
        
    def marcar_completada(self, tarea_id):
        # Buscar la tarea utilizando el método buscar_tarea (funcion anterior)
        tarea = self.buscar_tarea(tarea_id)
        
        if tarea:
            # Si se encuentra la tarea, se marca como completada
            tarea.completada = True
            return tarea  # Se actualiza la tarea a tarea completada
        return None  # Si la tarea no existe, se retorna None
    
    def listar_tareas(self, pendientes=False):
        
        # Mostrar todas las tarea pendientes
        if pendientes:
            tareas_pendientes = []
            # Recorrer cada tarea en la lista de tareas
            for tarea in self.tareas:
                # Si la tarea no está completada, agregarla a la lista de pendientes
                if not tarea.completada:
                    tareas_pendientes.append(tarea)
            # Retornar la lista de tareas pendientes
            return tareas_pendientes
        else:
            # Si no se solicita filtrado, retornar todas las tareas
            return self.tareas
    
    def tareas_por_prioridad(self, prioridad):
        ## Filtra y retorna las tareas que coinciden con la prioridad dada.
        tareas_filtradas = []
        for tarea in self.tareas:
            if tarea.prioridad == prioridad:
                tareas_filtradas.append(tarea)
        return tareas_filtradas