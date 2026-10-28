---
layout: default
title: Clomifene
parent: Solo Predicción del Modelo (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Clomifene: nueva indicación predicha, Trastorno del desarrollo sexual 46,XY por defecto de esteroidogénesis testicular (nivel de evidencia L5). Indicación original: Clomifeno"
monitor_inn: "clomifene"
predicted_indications: ["46,XY disorder of sex development due to testicular steroidogenesis defect", "transverse vaginal septum", "longitudinal vaginal septum", "symptomatic form of fragile X syndrome in female carrier", "blepharophimosis-epicanthus inversus-ptosis", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "partial trisomy/tetrasomy of the short arm of chromosome 18", "partial trisomy/tetrasomy of the short arm of chromosome 5", "partial trisomy/tetrasomy of the short arm of chromosome 12", "anovulation"]
---

# Clomifene
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Clomifeno: De Inducción de la Ovulación a Trastorno del Desarrollo Sexual 46,XY por Defecto de Esteroidogénesis Testicular
{: .text-alpha }

## Resumen en Una Frase

El clomifeno es un modulador selectivo de los receptores de estrógenos, utilizado para inducir la ovulación en la infertilidad femenina. El modelo TxGNN predice que podría ser efectivo para el **trastorno del desarrollo sexual 46,XY por defecto de esteroidogénesis testicular**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, y el análisis del mecanismo la hace poco plausible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Clomifeno (el registro sanitario solo indica el nombre del principio activo; su uso conocido es la inducción de la ovulación) |
| Nueva Indicación Predicha | Trastorno del desarrollo sexual 46,XY por defecto de esteroidogénesis testicular |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

El clomifeno es un modulador selectivo de los receptores de estrógenos (SERM). Bloquea los receptores de estrógenos del hipotálamo, lo que reduce la retroalimentación negativa y aumenta la secreción de GnRH, LH y FSH. Su acción sobre el receptor de estrógenos alfa (ESR1) está documentada en las bases farmacológicas consultadas.

La relación con la nueva indicación es débil. En este trastorno, el bloqueo ocurre dentro del propio testículo, por una deficiencia enzimática en la síntesis de esteroides. Aumentar el estímulo de gonadotropinas difícilmente restauraría la síntesis de andrógenos si la enzima no funciona. El puntaje alto del modelo TxGNN (deep learning) probablemente refleja similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni un mecanismo terapéutico demostrado.

En resumen, la predicción es una señal computacional sin respaldo mecanístico claro ni evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20016201 | ZIMAQUIN 50 MG TABLETAS | Tableta | CLOMIFENO |

Este registro (Laboratorio Franco Colombiano Lafrancol S.A.S.) figura como **cancelado**. No hay registros vigentes en los datos compilados.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN/PrimeKG, no texto de prospecto):
  - Hepatopatía y enfermedad de la vesícula biliar.
  - Trastornos tiroideos: hipotiroidismo, mixedema, hipotiroidismo congénito, tirotoxicosis, hipertiroidismo y enfermedad de Graves.
  - Insuficiencia suprarrenal: insuficiencia adrenocortical y enfermedad de Addison.
  - Tumores hipofisarios: tumor, cáncer, adenoma y adenocarcinoma de hipófisis.
  - Trastornos ginecológicos: endometriosis, cáncer de endometrio y de cuerpo uterino, quiste ovárico, síndrome de hiperestimulación ovárica y síndrome de ovario poliquístico.
  - Trastornos psiquiátricos: ansiedad, trastorno neurótico y trastorno distímico.
  - Otros: tromboflebitis, trastornos de la visión y ceguera.
- **Interacciones farmacológicas**: se identificó una interacción de nivel **Mayor** con **bexaroteno** (fuente: DDInter).
- **Datos de prospecto**: las advertencias y contraindicaciones del registro sanitario INVIMA no estaban disponibles, por lo que se recomienda consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (L5), sin ensayos ni literatura. Además, el mecanismo del clomifeno (aumentar el estímulo de gonadotropinas) no corrige un defecto enzimático intratesticular.

Entre las otras predicciones del modelo, solo **anovulación** (puesto 10, puntaje 0.9952) tiene evidencia: 3 ensayos clínicos completados, incluido un ensayo aleatorizado doble ciego de fase 4 (NCT00478504, n=159) que usa clomifeno como comparador, y revisiones sistemáticas como el ensayo M-OVIN (PMID 29273245). Sin embargo, es el uso establecido del fármaco, no un reposicionamiento real.

**Para avanzar se necesita:**
- Una hipótesis mecanística plausible, o estudios preclínicos, que justifiquen el uso en defectos de esteroidogénesis testicular.
- Una búsqueda dirigida de literatura y ensayos específicos para esta enfermedad rara.
- Verificar la disponibilidad comercial, ya que el único registro sanitario en Colombia está cancelado.
- Obtener el prospecto de INVIMA para completar el perfil de seguridad.
- Evaluar la relevancia de las contraindicaciones del grafo de conocimiento, en particular las hormonales y hepáticas, antes de cualquier uso en esta población.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

