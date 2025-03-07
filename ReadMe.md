# "Pruebas Gestor Tareas en Python"

El proyecto **"Pruebas Gestor Tareas en Python"** es una aplicación de gestión de tareas en la que se pueden realizar diversas operaciones sobre las tareas, como agregar, eliminar, buscar, marcar como completadas, listar y filtrar tareas según su prioridad. El sistema está diseñado para almacenar y manipular una lista de tareas, con un enfoque en la organización eficiente de las mismas.

## Clases y Funciones:

- **GestorTareas**: Administra una lista de tareas, permite agregar nuevas tareas, eliminar tareas, buscar tareas por ID, marcar tareas como completadas y listar tareas.
- **Tarea**: Representa una tarea con atributos como título, descripción, estado de completado y prioridad.
  
## Pruebas Realizadas:

Se realizaron pruebas unitarias utilizando la librería `unittest` para asegurar que las funcionalidades operen correctamente. Las pruebas cubren los siguientes casos:

- **Agregar tarea**: Verifica que las tareas se agreguen correctamente con el título, descripción y prioridad.
- **Eliminar tarea**: Verifica que una tarea se elimine correctamente usando su ID.
- **Buscar tarea**: Valida que las tareas se puedan buscar por su ID y que devuelvan el resultado esperado.
- **Marcar tarea como completada**: Verifica que una tarea se marque correctamente como completada.
- **Listar tareas**: Valida la lista de todas las tareas y las tareas pendientes.
- **Filtrar tareas por prioridad**: Verifica que las tareas se puedan filtrar correctamente por prioridad.
- **Validación de prioridades**: Asegura que no se puedan agregar tareas con prioridades no válidas.
- **Comparación de tareas**: Verifica la comparación entre dos tareas con el mismo ID pero atributos diferentes.

## Librerías Usadas:

- `unittest`: Para la ejecución de pruebas unitarias y validación de funcionalidades.

## Autor:
Este proyecto fue desarrollado por **César Sánchez**.