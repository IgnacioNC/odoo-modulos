# Gestión de Camiones y Paquetería – Módulo Odoo Tarea 11

Este módulo es para gestionar una empresa de transporte.  
Incluye la creación de paquetes, camiones, historial de conductores y actualizaciones del envío.

---

## Modelos del módulo

### Modelo Paquete

Archivo: `models/paquete.py`

El modelo `paqueteria.paquete` representa un paquete real que la empresa transporta.

Tiene los campos:

- número de seguimiento  
- remitente  
- destinatario  
- dirección de entrega (país, región, municipio, calle y número)
- camión asignado  
- estado del envío

#### ¿Por qué se usan estas relaciones?

- **Many2one** cuando un paquete solo puede tener un remitente, un destinatario o un camión.
- **One2many** cuando un paquete puede tener muchas actualizaciones del estado de envío.

Esto permite mostrar automáticamente listas de actualizaciones dentro del formulario del paquete.

---

### Modelo Camión

Archivo: `models/camion.py`

El modelo `paqueteria.camion` guarda información de cada camión, en mi caso:

- matrícula  
- conductor actual  
- historial de conductores  
- fecha de ITV  
- paquetes transportados  

#### ¿Por qué se usan estas relaciones?

- Un camión solo puede tener un conductor actual, por eso es **Many2one**.
- Un camión puede tener muchos paquetes, por eso **One2many**.
- Un camión puede haber tenido muchos conductores en el pasado, por eso **One2many** hacia el historial.

---

### Modelo Historial de Conductores

Archivo: `models/historial_conductor.py`

Este modelo existe para poder guardar el conductor anterior de un camión, junto con la fecha.

Si esta información se guardara dentro del camión directamente, no se podría actualizar automáticamente al cambiar de conductor, habría que hacerlo manualmente y limitaría la finalidad.

Por eso se crea un modelo separado con:

- camión (relacionado)
- conductor (relacionado)
- email de trabajo del conductor
- fecha

#### ¿Por qué se usan estas relaciones?

- Un camión puede tener muchos historiales, pero cada historial pertenece solo a un camión **Many2one**.
- Un conductor puede aparecer muchas veces en el historial, pero cada registro del historial solo es de un conductor **Many2one**.



### Modelo Estado de Envío

Archivo: `models/estado_envio.py`

Este modelo guarda cada cambio de estado del paquete (en mi caso: recibido, en_transito, retrasado y entregado).

Tiene:

- paquete (relacionado)
- fecha  
- estado (lista con diferentes estados)
- notas

#### ¿Por qué se usan estas relaciones?

- Cada actualización pertenece a un único paquete, por eso es **Many2one**.

---

## Vistas

Dentro de `views` están todas las vistas del módulo, en este caso `paqueteria_view.xml`:

---

Incluye formularios y listas para:

- Paquetes
- Camiones
- Estados del envío

Menú principal:

Paquetería
  - Paquetes
  - Camiones
  - Estados de Envío

---

## Seguridad

En `security/security.xml` se definen los grupos que se usarán posteriormente para asignar los permisos
básicos para acceder y gestionar los modelos, estos se especifican en `security/ir.model.access.csv`.

---

## Repositorio GitHub

https://github.com/IgnacioNC/odoo-modulos
