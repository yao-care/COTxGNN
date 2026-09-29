---
layout: default
title: Dienogest
parent: Solo Predicción del Modelo (L5)
nav_order: 163
evidence_level: L5
indication_count: 10
---

# Dienogest
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

# Dienogest: De Indicación Original No Detallada a Amenorrea

## Resumen en Una Frase

Dienogest es un progestágeno que en Colombia se comercializa en combinación con etinilestradiol. Los estudios clínicos encontrados lo evalúan sobre todo en endometriosis.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, pero la amenorrea es un efecto farmacológico conocido del tratamiento y no una enfermedad que el fármaco cure.
Hay **4 ensayos clínicos** (todos en endometriosis, es decir, evidencia indirecta) y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dienogest y etinilestradiol (texto registrado en INVIMA; describe la composición del producto, no una indicación clínica) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L4 (solo evidencia indirecta, en endometriosis) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, dienogest es un progestágeno que suprime la ovulación y la proliferación del endometrio. Su eficacia en el contexto ginecológico (principalmente endometriosis) se ha estudiado ampliamente.

La relación entre la indicación original y la nueva es débil. La amenorrea es un efecto esperado del tratamiento con dienogest, no una condición que este fármaco trate. El puntaje alto de TxGNN probablemente refleja esta asociación fármaco-fenotipo y no un beneficio terapéutico real.

Por lo tanto, la predicción es mecanísticamente coherente como efecto farmacológico, pero no respalda un uso terapéutico para tratar la amenorrea. Los cuatro ensayos encontrados incluyeron pacientes con endometriosis.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | Completado | 968 | Estudio observacional en práctica clínica real de dienogest (Visanne) en endometriosis. La amenorrea sería, como mucho, una observación secundaria. |
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Fase 3 | Reclutando | 290 | Estudio aleatorizado, abierto y de no inferioridad que compara Indinol Forto 200 mg con Visanne 2 mg en endometriosis. Aún sin resultados. |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | Completado | 895 | Cohorte observacional sobre calidad de vida y seguridad a largo plazo de dienogest en mujeres asiáticas con endometriosis. |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Activo, sin reclutamiento | 138 | Compara estradiol transdérmico con dienogest frente a drospirenona en endometriosis, con satisfacción de la paciente como objetivo. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20093177 | DIENILLE® COMPRIMIDO RECUBIERTOS (EXELTIS S.A.S.) | Tableta recubierta | Dienogest y etinilestradiol |

Los datos recibidos repiten el mismo registro sanitario. El total reportado es de 20 registros, pero solo se dispone del detalle de este.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La amenorrea es un efecto conocido de dienogest y no un objetivo terapéutico. Los cuatro ensayos son indirectos (endometriosis), sin resultados sobre amenorrea y sin literatura de apoyo. El puntaje alto del modelo no es suficiente por sí solo.

**Para avanzar se necesita:**
- Definir si el objetivo real es la supresión menstrual deseada (efecto terapéutico) o el tratamiento de amenorrea patológica, que sería un uso distinto.
- Verificar la condición y los desenlaces del ensayo de Fase 3 (NCT07164183).
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Advertencias y contraindicaciones del prospecto de INVIMA.
- Datos de seguridad del producto en combinación con etinilestradiol.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

