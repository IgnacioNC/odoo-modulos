# TAREA 10

En esta tarea he creado un módulo de Odoo para gestionar ordenadores y componentes.

---

## Modelos creados

### 1. Componentes (componente.py)

Tiene:

- Nombre del componente
- Especificaciones
- Precio

Este modelo sirve para crear los componentes que pueden tener los ordenadores.

### 2. Ordenadores (ordenador.py)

Tiene:

- Número del equipo
- Usuario (relación Many2one con res.users)
- Componentes del ordenador (Many2many con Componentes)
- Última modificación
- Precio total (calculado automáticamente)
- Incidencias

## Funciones dentro de Ordenadores

### \_comprobar_fecha:

- La fecha de última modificación no puede ser futura. Si se intenta guardar una fecha posterior a hoy aparece un mensaje de error.

### \_compute_total:

- El precio total del ordenador se calcula sumando los precios de todos sus componentes.
- Este campo no se puede editar manualmente, es automático.

## Vistas

He creado la vista de lista y formulario "ordenadores_view", en la que se pueden gestionar
los componentes y ordenadores.

## Seguridad

He añadido el archivo security.xml con 2 grupos, admin y usuario avanzado.
En ir.model.access.csv le he asignado los permisos a cada grupo de usuarios:
Admin tendrá todos los permisos mientras que el usuario avanzado solo podrá leer y escribir.

## Menú

En el menú principal de Odoo aparecerá "Ordenadores", donde podremos gestionar tanto los ordenadores como los componentes
cambiando de vista mediante las categorías de la barra superior: "Registro ordenadores" y "Registro componentes".
