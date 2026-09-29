---
layout: default
title: Natalizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 293
evidence_level: L5
indication_count: 5
---

# Natalizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Natalizumab: De Esclerosis Múltiple a Bronquitis

## Resumen en Una Frase

Natalizumab es un anticuerpo monoclonal que bloquea la integrina alfa-4 y se comercializa en Colombia como Tysabri®. La literatura asociada lo ubica en el tratamiento de la esclerosis múltiple recurrente-remitente; el registro sanitario solo lista el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **Bronquitis**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (solo figura "NATALIZUMAB"); la literatura lo asocia con esclerosis múltiple |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.46% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 4 filas (2 números de registro únicos: 20241992 y 20006016) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, natalizumab bloquea la migración de leucocitos mediada por la integrina alfa-4, lo que reduce el paso de linfocitos hacia los tejidos inflamados. Esta acción es la base de su uso en enfermedades autoinmunes.

Con estos datos no se puede sustentar un vínculo mecanístico con la bronquitis. La puntuación de 0.995 proviene solo de una predicción basada en grafos de conocimiento, sin estudios reales que la acompañen.

Además, natalizumab es un agente inmunosupresor y podría aumentar el riesgo de infecciones respiratorias. Esto va en dirección contraria al beneficio predicho. Por ahora la predicción no tiene respaldo y conviene tratarla con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Las 4 filas del registro corresponden a 2 números de registro sanitario, cada uno repetido dos veces.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20241992 | TYSABRI® SUBCUTÁNEO 150MG/ML (BIIB Colombia SAS) | Solución inyectable | No detallada en el registro (solo figura "NATALIZUMAB") |
| 20006016 | TYSABRI® (BIIB Colombia S.A.S.) | Solución concentrada para infusión | No detallada en el registro (solo figura "NATALIZUMAB") |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de bronquitis está en el nivel L5: solo hay un puntaje del modelo, sin ensayos ni publicaciones. Además, el perfil inmunosupresor de natalizumab sugiere un posible aumento del riesgo de infecciones respiratorias, no un beneficio.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que muestren un beneficio real de natalizumab en bronquitis.
- Datos de seguridad del prospecto de INVIMA (advertencias y contraindicaciones), que hoy faltan y bloquean el tamizaje de seguridad.
- Datos del mecanismo de acción desde DrugBank para analizar el vínculo mecanístico.
- Confirmar la indicación aprobada en Colombia, ya que el registro solo lista el nombre del principio activo.
- Como referencia, otras predicciones del mismo fármaco (por ejemplo, psoriasis) tienen más literatura, pero es contradictoria: hay reportes de psoriasis inducida o agravada por natalizumab y un reporte de mejoría en pacientes con esclerosis múltiple. Por eso también están en Hold.

*Este informe es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

