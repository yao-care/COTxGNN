---
layout: default
title: Sacituzumab Govitecan
parent: Solo Predicción del Modelo (L5)
nav_order: 353
evidence_level: L5
indication_count: 4
---

# Sacituzumab Govitecan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Sacituzumab govitecan: De Oncología a Osteoporosis Inducida por Fármacos

## Resumen en Una Frase

Sacituzumab govitecan (Trodelvy®) es un conjugado anticuerpo-fármaco dirigido contra Trop-2, que lleva como carga citotóxica el SN-38, un inhibidor de la topoisomerasa I. Se usa en oncología.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción. Es una señal solo del modelo, sin sustento clínico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Oncología (el registro INVIMA solo consigna el nombre de la sustancia, "SACITUZUMAB GOVITECAN", sin texto de indicación detallado) |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 99.78% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 3 (todos bajo el mismo número de registro, 20235052) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, sacituzumab govitecan es un conjugado anticuerpo-fármaco dirigido a Trop-2 que libera SN-38, un inhibidor de la topoisomerasa I. Es un agente citotóxico oncológico, y no se le conoce acción anabólica ni antirresortiva sobre el hueso.

**Con los datos disponibles no se encontró un vínculo mecanístico que respalde esta predicción.** La quimioterapia citotóxica y su contexto de cuidados de soporte se asocian con más frecuencia a pérdida ósea que a protección ósea. El puntaje alto (0.998) probablemente refleja cercanía dentro del grafo de conocimiento y no una razón terapéutica. Por eso no debe interpretarse como evidencia de beneficio.

Las otras tres predicciones del modelo tampoco tienen sustento. Son retinopatía diabética no proliferativa grave, retinopatía diabética y catarata diabética, todas con puntajes entre 0.991 y 0.997 y sin ensayos ni literatura. Las dos primeras no son señales independientes, porque una es la categoría más amplia de la otra. Además, un fármaco citotóxico sistémico con mielosupresión y toxicidad gastrointestinal marcadas tiene un perfil beneficio-riesgo desfavorable para afecciones crónicas no malignas, donde ya existen tratamientos establecidos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20235052 | TRODELVY® (GILEAD SCIENCES IRELAND UC) | Polvo liofilizado para reconstituir a solución inyectable | SACITUZUMAB GOVITECAN (el registro no detalla el texto de indicación) |

Nota: los tres registros del Evidence Pack son idénticos (mismo número, producto, forma y fabricante), por lo que se presentan una sola vez.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida: conjugado anticuerpo-fármaco (anti-Trop-2) con carga citotóxica inhibidora de topoisomerasa I (SN-38) |
| Riesgo de Mielosupresión | Alto (mielosupresión marcada y toxicidad gastrointestinal, según la evaluación del caso) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, electrolitos, y síntomas gastrointestinales |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible. Además, el perfil de toxicidad de un citotóxico sistémico es difícil de justificar para una indicación no oncológica.

**Para avanzar se necesita:**
- Un fundamento mecanístico creíble que relacione la inhibición de topoisomerasa I o Trop-2 con el metabolismo óseo
- Estudios preclínicos o de mecanismo que apoyen la hipótesis
- Datos de seguridad del prospecto INVIMA (advertencias y contraindicaciones), aún pendientes
- Datos del mecanismo de acción (MOA) desde DrugBank
- Un análisis de beneficio-riesgo frente a las terapias osteoporóticas ya establecidas

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

