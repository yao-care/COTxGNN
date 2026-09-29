---
layout: default
title: Finasteride
parent: Solo Predicción del Modelo (L5)
nav_order: 200
evidence_level: L5
indication_count: 6
---

# Finasteride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Finasterida: De Indicación No Especificada en el Registro a Hipertricosis Universal Congénita Tipo Ambras

## Resumen en Una Frase

Finasterida es un inhibidor de la 5-alfa reductasa tipo II, que reduce la dihidrotestosterona (DHT) y se usa en trastornos dependientes de andrógenos. En Colombia está comercializada, pero el registro sanitario no detalla su indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **hipertricosis universal congénita tipo Ambras**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción. Es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el texto del registro solo repite "FINASTERIDE") |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Finasterida inhibe la 5-alfa reductasa tipo II, la enzima que convierte la testosterona en DHT. Por eso es relevante en el crecimiento del cabello dependiente de andrógenos. La base de datos no trae un campo formal de mecanismo de acción (MOA), por lo que esta descripción proviene del análisis mecanístico incluido en el paquete de evidencia.

La dirección de la predicción (reducir el exceso de vello) es plausible en teoría. Sin embargo, el síndrome de Ambras es un trastorno congénito que en gran parte no depende de andrógenos. Se asocia con reordenamientos cromosómicos en 8q22 que afectan al gen *TRPS1*. Por lo tanto, el vínculo mecanístico es **especulativo** y no hay datos que lo respalden.

El puntaje alto de TxGNN (99.99%) refleja la cercanía en el grafo de conocimiento entre finasterida y los trastornos del cabello. No constituye evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Otras Predicciones del Modelo (Contexto)

| # | Indicación Predicha | Puntaje | Evidencia | Decisión |
|---|------|------|------|------|
| 2 | Hipertricosis (enfermedad) | 99.99% | L4: 1 ensayo (Fase 4, sin relación directa con finasterida) y 4 revisiones generales de trastornos del cabello | Pregunta de investigación |
| 3 | Malformación con componente dental/periodontal | 99.99% | L5: 20 artículos sobre periodontitis, ninguno menciona finasterida | Hold |
| 4 | Síndrome con malformación de Dandy-Walker | 99.99% | L5: sin datos | Hold |
| 5 | Anomalía genética aislada del tallo piloso | 99.99% | L5: sin datos | Hold |
| 6 | Tricomegalia familiar aislada | 99.15% | L5: sin datos | Hold |

Ninguna de estas predicciones tiene estudios que evalúen finasterida directamente. La hipertricosis es la única con algo de contexto, pero es indirecto. Por definición no depende de andrógenos y el ensayo recuperado (NCT04293822) evalúa cetirizina tópica frente a minoxidil en alopecia androgenética.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20135117 | BINFIN® 5.0 MG TABLETA RECUBIERTA (Hetero Labs Limited) | Tableta recubierta | Solo figura "FINASTERIDE" (sin texto de indicación) |

**Nota:** el sistema reporta 20 registros en total, pero las 5 filas disponibles corresponden todas al mismo número (20135117). Solo se pudo verificar un registro distinto. La vía de administración es oral (tableta recubierta y tableta cubierta con película).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal no tiene ensayos clínicos ni literatura (nivel L5), y el vínculo mecanístico es especulativo porque el síndrome de Ambras no depende de andrógenos. Un puntaje alto del modelo no basta para avanzar.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA para completar advertencias, contraindicaciones e indicación aprobada
- Confirmar el MOA en DrugBank (DB01216)
- Depurar los registros sanitarios duplicados para contar los 20 registros reales
- Buscar evidencia mecanística o reportes de casos de inhibidores de 5-alfa reductasa en hipertricosis congénita
- Evaluar como línea alternativa la hipertricosis general (rango 2) y trastornos del cabello dependientes de andrógenos, donde el mecanismo sí es aplicable

---

*Este informe es solo para referencia de investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

