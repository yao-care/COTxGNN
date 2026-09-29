---
layout: default
title: Olmesartan
parent: Solo Predicción del Modelo (L5)
nav_order: 304
evidence_level: L5
indication_count: 10
---

# Olmesartan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Olmesartán: De Antihipertensivo (ARA-II) a Angina de Prinzmetal

## Resumen en Una Frase

Olmesartán es un bloqueador del receptor AT1 de la angiotensina II. En Colombia está registrado en combinación con diuréticos (olmesartán medoxomilo). El modelo TxGNN predice que podría ser efectivo para **angina de Prinzmetal**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta indicación específica. La predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Olmesartán medoxomilo y diuréticos (texto del registro sanitario) |
| Nueva Indicación Predicha | Angina de Prinzmetal |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de origen. Según la información conocida, olmesartán es un antagonista del receptor AT1 de la angiotensina II, usado en el manejo de la presión arterial en combinación con diuréticos.

La angiotensina II produce vasoconstricción a través del receptor AT1. Por eso, mecanísticamente, podría contribuir al vasoespasmo coronario que define la angina de Prinzmetal, y bloquear ese receptor sería una vía posible. Sin embargo, este vínculo es **especulativo**. No se recuperaron ensayos ni literatura que lo respalden, y el puntaje del modelo es el único sustento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Otras Indicaciones Predichas con Más Evidencia

Estas indicaciones no son la principal, pero tienen más respaldo que la angina de Prinzmetal:

| Indicación | Puntaje TxGNN | Nivel | Recomendación | Comentario |
|------|------|------|------|------|
| Migraña | 99.64% | L3 | Pregunta de investigación | Cuatro publicaciones: una revisión sistemática de IECA/ARA-II (2019, nivel de clase), un estudio clínico pequeño con olmesartán en hipertensos (PMID [16618270](https://pubmed.ncbi.nlm.nih.gov/16618270/), 2006) y dos comentarios/revisiones generales. El posible beneficio puede confundirse con la reducción de la presión arterial. El diseño de los estudios se dedujo solo de los títulos y debe verificarse en texto completo. |
| Hipertensión pulmonar | 99.61% | L4 | Pregunta de investigación | Solo estudios preclínicos en ratas y ratones (p. ej., PMID [18209564](https://pubmed.ncbi.nlm.nih.gov/18209564/), [16336959](https://pubmed.ncbi.nlm.nih.gov/16336959/)). No hay datos de eficacia en humanos. El único ensayo recuperado (NCT04330300, COVID-19) no evalúa esta indicación. |
| Glaucoma de ángulo abierto | 99.40% | L4 | Hold | La única publicación es una revisión general de tratamiento de glaucoma (PMID [19902393](https://pubmed.ncbi.nlm.nih.gov/19902393/)), y no se confirma que analice olmesartán. |

Las demás predicciones (alopecia y variantes de hipotricosis, migraña con aura de tronco encefálico, cardiopatía cifoescoliótica) son solo del modelo (L5), sin vínculo mecanístico creíble. Varias parecen artefactos del grafo de conocimiento.

## Información de Mercado en Colombia

El registro incluye 20 entradas. Las cinco primeras corresponden al mismo registro sanitario, por lo que se presenta una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20103712 | OLMEDOXTAN H® 40MG/12.5MG | Tableta recubierta | Olmesartán medoxomilo y diuréticos |

La vía de administración registrada es oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como señal de seguridad de la literatura recuperada (casos clínicos y serie de casos), los ARA-II se asocian con fetopatía cuando se usan en el embarazo, por ejemplo oligohidramnios y daño renal fetal (PMID [21271514](https://pubmed.ncbi.nlm.nih.gov/21271514/), [41815228](https://pubmed.ncbi.nlm.nih.gov/41815228/)). Esto es relevante para mujeres en edad fértil. Además, la hipotensión sistémica es una preocupación para cualquier indicación nueva.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para angina de Prinzmetal solo existe la predicción del modelo (L5), sin ensayos ni literatura, y el vínculo mecanístico es especulativo. No hay base para avanzar con esta indicación por ahora.

**Para avanzar se necesita:**
- Revisión bibliográfica dirigida sobre bloqueadores del receptor AT1 y vasoespasmo coronario
- Obtener el prospecto del INVIMA para completar advertencias y contraindicaciones
- Datos de mecanismo de acción desde DrugBank
- Si se quiere priorizar otra indicación, verificar en texto completo los estudios de migraña (la de mayor evidencia, L3) y controlar el efecto de la presión arterial como factor de confusión

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

