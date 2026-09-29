---
layout: default
title: Adenosine
parent: Solo Predicción del Modelo (L5)
nav_order: 28
evidence_level: L5
indication_count: 2
---

# Adenosine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Adenosina: De Taquicardias a Bloqueo de Rama (término obsoleto)

## Resumen en Una Frase

La adenosina es un fármaco de uso cardiovascular, utilizado originalmente para tratar taquicardias.
El modelo TxGNN predice que podría ser efectiva para **bloqueo de rama (término obsoleto de la ontología)**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, y el efecto farmacológico conocido apunta en sentido contrario.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Taquicardias (uso clínico según la farmacología; el texto de los registros dice solo «ADENOSINA») |
| Nueva Indicación Predicha | Bloqueo de rama (término obsoleto) |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información farmacológica, la adenosina actúa sobre los receptores de adenosina A1, A2A, A2B y A3, y también sobre TRPM4 y las enzimas PI4K2A y PI4K2B. En el nodo auriculoventricular, la activación de A1 enlentece la conducción.

Esta predicción **no parece razonable**. El puntaje es muy alto (0.999), pero no hay ningún respaldo clínico. Además, «bloqueo de rama obsoleto» es una etiqueta antigua de la ontología, por lo que la predicción podría ser un artefacto del grafo de conocimiento. Como la adenosina frena la conducción AV, es más probable que provoque o revele un bloqueo de conducción que que lo trate. La dirección del efecto parece desfavorable.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los 12 registros incluyen entradas repetidas. Se muestran solo los registros distintos:

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20148959 | ADENOTROY (Troikaa Pharmaceuticals Limited) | Solución inyectable | ADENOSINA |
| 20139028 | ADENOSINA SOLUCIÓN INYECTABLE 6MG/2ML (Setaa Pharma S.A.S.) | Solución inyectable | ADENOSINA |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: no se registraron interacciones entre medicamentos. Los 7 registros de la consulta corresponden a dianas farmacológicas: receptores A1 (ADORA1), A2A (ADORA2A), A2B (ADORA2B), A3 (ADORA3), TRPM4, PI4K2A y PI4K2B.
- Consultar el prospecto para información de advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje de TxGNN es muy alto, pero no hay ensayos ni literatura, y la etiqueta de la enfermedad es un término obsoleto. Además, el efecto de la adenosina sobre la conducción AV va en dirección opuesta a un beneficio en el bloqueo de rama.

**Para avanzar se necesita:**
- Confirmar si la predicción es un artefacto de una etiqueta obsoleta y si existe un término vigente equivalente.
- Obtener el prospecto del INVIMA con advertencias y contraindicaciones, y los datos del mecanismo de acción desde DrugBank.
- Considerar como línea de investigación la segunda predicción, **taquicardia ventricular polimórfica catecolaminérgica** (puntaje 99.42%, nivel L4, «pregunta de investigación»). Su única señal clínica es un reporte de caso con ATP, no con adenosina. El ensayo de fase 2a NCT07263139 (AGP100, n=10) no está verificado como relacionado con la adenosina. Por su vida media muy corta, la adenosina serviría, como mucho, para terminar episodios agudos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

