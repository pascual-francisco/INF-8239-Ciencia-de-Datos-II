
# Runbook

## Purpose

Definir las acciones requeridas para detectar, contener, investigar y resolver incidentes relacionados con el DSS.

## Detection

Detectar incidentes mediante:

- Monitoreo de desempeño
- Auditorías de equidad
- Reportes de usuarios
- Revisiones de gobernanza

## Examples of Incidents

- Recall por debajo del límite permitido.
- Brecha de equidad superior a la tolerancia.
- Uso de columnas prohibidas.
- Acceso no autorizado a información.
- Drift de datos o desempeño.

## Containment

1. Detener cambios y despliegues.
2. Preservar registros y evidencia.
3. Notificar responsables.
4. Evaluar impacto.

## Evidence Preservation

Conservar:

- Logs
- Métricas
- Versiones del modelo
- Versiones del dataset
- Resultados de auditoría

## Communication

Responsables:

- Product Owner
- ML Engineer
- Institutional Owner

Partes informadas:

- Usuarios
- Representantes afectados

## Rollback

1. Detener versión actual.
2. Restaurar último baseline aprobado.
3. Verificar métricas.
4. Confirmar estabilidad.

## Recovery

Antes de reanudar operaciones:

- Investigar causa raíz.
- Aplicar acciones correctivas.
- Ejecutar nuevamente auditorías.
- Obtener aprobación formal.

## Postmortem

Documentar:

- Fecha
- Descripción del incidente
- Impacto
- Causa raíz
- Acción correctiva
- Acción preventiva
- Responsable
- Fecha de cierre

## Human Oversight

El DSS únicamente recomienda acciones.

Toda decisión final debe ser revisada, aprobada o rechazada por un responsable humano.
