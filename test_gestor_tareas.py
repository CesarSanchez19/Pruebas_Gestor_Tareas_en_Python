# Importamos el módulo unittest para realizar pruebas
import unittest

# Importamos las clases a probar
from gestor_tareas import GestorTareas, Tarea

# Definir la clase de prueba GestorTareas
class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        # Creamos una nueva instancia de GestorTareas para cada prueba
        self.gestor = GestorTareas()
        
        # Agregamos tres tareas de ejemplo con diferentes prioridades
        self.tarea1 = self.gestor.agregar_tarea("Realizar tarea", "Elaborar tarea de testing", "alta")
        self.tarea2 = self.gestor.agregar_tarea("Estudiar Python", "Pruebas unitarias", "normal")
        self.tarea3 = self.gestor.agregar_tarea("Proyecto integrador", "Avanzar con el proyecto de desarrollo", "baja")

    def test_agregar_tarea(self):
        # Agregamos una tarea con valores de prueba
        tarea = self.gestor.agregar_tarea("Prueba", "Descripcion de prueba")

        # Verificamos que la tarea se haya añadido a la lista de tareas
        self.assertIn(tarea, self.gestor.tareas)
        
        # Verificamos que los atributos de la tarea sean los correctos
        self.assertEqual(tarea.titulo, "Prueba")
        self.assertEqual(tarea.descripcion, "Descripcion de prueba")
        self.assertEqual(tarea.prioridad, "normal")  # Valor por defecto
        self.assertFalse(tarea.completada)  # Por defecto no está completada
        
        # Verificamos que el ID sea el siguiente en la secuencia (4)
        self.assertEqual(tarea.id, 4)
    
    def test_eliminar_tarea(self):

        # Verificamos que la tarea exista para hacer la eliminacion correcta
        tarea_eliminada = self.gestor.eliminar_tarea(self.tarea1.id)
        self.assertIsNotNone(tarea_eliminada)  # Verifica que no sea None
        self.assertEqual(tarea_eliminada.id, self.tarea1.id)  # Verifica que sea la tarea correcta
        self.assertNotIn(self.tarea1, self.gestor.tareas)  # Verifica que ya no esté en la lista

        # Verificamos al eliminar una tarea que no existe
        tarea_inesistente = self.gestor.eliminar_tarea(777) #Referencia a veggeta777
        self.assertIsNone(tarea_inesistente)  # Verifica que devuelva None
        
    def test_buscar_tarea(self):
        ## Verificar la busqueda de una tarea existente por su id
        tarea_encontrada = self.gestor.buscar_tarea(self.tarea2.id)
        self.assertIsNotNone(tarea_encontrada)  # La tarea debe existir dentro de la lista
        self.assertEqual(tarea_encontrada.id, self.tarea2.id)
        self.assertEqual(tarea_encontrada.titulo, self.tarea2.titulo)
        
        ## Verificar la busqueda de una tarea inexistente por id, si no lo encuentra retornara None
        tarea_inexistente = self.gestor.buscar_tarea(132)  # ID que no existe
        self.assertIsNone(tarea_inexistente)
        
    def test_marcar_completada(self):
        ## Verificamos que se marque y actualice correctamente una tarea existente como completada.
        
        tarea_finalizada = self.gestor.marcar_completada(self.tarea1.id)# Marcar la tarea existente
        
        self.assertIsNotNone(tarea_finalizada) # Verifica que se haya retornado tarea completada = True
        self.assertTrue(tarea_finalizada.completada)
        
        ## Verificamos el comportamiento al intentar marcar una tarea que no exista (inexistente).
        tarea_inexistente = self.gestor.marcar_completada(19)# Intentar marcar una tarea con un ID que no existe
        
        self.assertIsNone(tarea_inexistente)# Se espera que retorne None
    
    def test_listar_todas_las_tareas(self):
        
        ## Verificamos el listado de todas las tareas
        listado = self.gestor.listar_tareas()
        
        self.assertEqual(len(listado), 3)
        # También se verifica que cada tarea agregada esté en el listado
        self.assertIn(self.tarea1, listado)
        self.assertIn(self.tarea2, listado)
        self.assertIn(self.tarea3, listado)
        
        ## Verificamos el listado filtrado por tareas pendientes
        
        # Marcamos una tarea como completada (tarea2)
        self.gestor.marcar_completada(self.tarea2.id)
        
        listado_pendientes = self.gestor.listar_tareas(pendientes=True)
        
        # Verifica que la tarea completada no se incluya en el listado de pendientes
        self.assertNotIn(self.tarea2, listado_pendientes)
        # Las otras tareas deben aparecer como tareas pendientes
        self.assertIn(self.tarea1, listado_pendientes)
        self.assertIn(self.tarea3, listado_pendientes)
        
        # Además, se verifica que todas las tareas del listado estén pendientes
        for tarea in listado_pendientes:
            self.assertFalse(tarea.completada)
            
    def test_tareas_por_prioridad(self):
        ## Verificamos que se filtren correctamente las tareas con prioridad 'alta'.
        tareas_alta = self.gestor.tareas_por_prioridad("alta")
        self.assertEqual(len(tareas_alta), 1)
        self.assertIn(self.tarea1, tareas_alta)

        ## Verificamos que se filtre correctamente la tarea con prioridad 'normal'.
        tareas_normal = self.gestor.tareas_por_prioridad("normal")
        self.assertEqual(len(tareas_normal), 1)
        self.assertIn(self.tarea2, tareas_normal) 

        ## Verificamos que se filtre correctamente la tarea con prioridad 'baja'
        tareas_baja = self.gestor.tareas_por_prioridad("baja")
        self.assertEqual(len(tareas_baja), 1)
        self.assertIn(self.tarea3, tareas_baja)

        ## Verifica que si se solicita una prioridad no existente se retorne una lista vacía.
        tareas_inexistente = self.gestor.tareas_por_prioridad("no existente")
        self.assertEqual(len(tareas_inexistente), 0)
    
    def test_prioridad_invalida(self):
        
        # Verificamos que se lance una excepción al usar una prioridad no permitida.
        with self.assertRaises(ValueError):  # Se espera que lanzar un error de tipo ValueError
            self.gestor.agregar_tarea("Tarea con prioridad inválida", "Tarea de prueba invalida", "Excelencia")  # Prioridad inválida

        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("Otra tarea inválida", "Terminar la ingeneria", "desconocida")  # Otra prioridad inválida

        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("Sin prioridad", "No se sabe que tarea es", "")  # Prioridad vacía no es válida

    def test_tarea_equal(self):
        tarea_uno = Tarea(1, "Foso_1", "Free_class", "alta")
        tarea_dos = Tarea(1, "Comprar una ESP32", "basico kit", "baja")  # Mismo ID pero diferente contenido
        tarea_tres = Tarea(2, "Terminar el codigo en React", "Pasar todo el proyecto a React con Vite", "normal")  # Diferente ID
        objeto_extraño = "No soy una tarea"

        # Verificamos que dos tareas con el mismo ID pero diferentes atributos se consideren iguales
        self.assertEqual(tarea_uno, tarea_dos)

        # Verificamos que dos tareas con diferente ID se consideren diferentes
        self.assertNotEqual(tarea_uno, tarea_tres)

        # Verificamos que una tarea no sea igual a un objeto de otro tipo
        self.assertNotEqual(tarea_uno, objeto_extraño)

if __name__ == "__main__":
    unittest.main()
