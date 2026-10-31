---
layout: default
title: Glycine
parent: Solo Predicción del Modelo (L5)
nav_order: 319
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Glycine: nueva indicación predicha, Enfermedad de la cavidad nasal (nivel de evidencia L5). Indicación original: Emulsiones lipidas"
monitor_inn: "Glycine"
predicted_indications: ["nasal cavity disease"]
---

# Glycine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Glicina: De Emulsiones Lipidas a Enfermedad de la Cavidad Nasal
{: .text-alpha }

## Resumen en Una Frase

La glicina es un aminoacido que figura en un registro sanitario colombiano (ya cancelado) de una emulsion lipidica para nutricion parenteral.
El modelo TxGNN predice que podria ser efectiva para **enfermedad de la cavidad nasal**,
pero solo hay **1 ensayo clinico** (indirecto, sin relacion con la glicina como tratamiento) y **2 publicaciones** (basicas/preclinicas) que no respaldan realmente esta direccion.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Emulsiones lipidas |
| Nueva Indicacion Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Prediccion TxGNN | 0.9985 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion. Segun la informacion conocida, la glicina es un aminoacido incluido en una formulacion de nutricion parenteral (emulsion lipidica), y su uso aprobado en Colombia se limitaba a ese contexto nutricional.

No se documenta un vinculo plausible entre la indicacion original (nutricion parenteral con emulsiones lipidas) y la enfermedad de la cavidad nasal. El puntaje de TxGNN es muy alto (0.9985), pero corresponde unicamente a una prediccion computacional, sin respaldo clinico ni mecanistico.

El unico ensayo asociado es un estudio de imagen diagnostica con un radiotrazador y las dos publicaciones tratan de histoquimica de mucosa nasal bovina y de adyuvantes mucosos para vacunas. Ninguno evalua la glicina como terapia nasal. Una hipotesis posible (por ejemplo, su papel como neurotransmisor inhibidor o agente citoprotector en la via aerea superior) tendria que formularse y probarse desde cero.

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Fase 1/2 | Completado | 25 | Estudio de imagen PET con el radiotrazador 18F-FPPRGD2 para medir la expresion de integrinas αvβ3 en pacientes con cancer (glioblastoma, canceres ginecologicos, carcinoma renal) tratados con antiangiogenicos. No evalua la glicina; relevancia indirecta (grado C). |

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Investigacion basica (histoquimica veterinaria) | Veterinary Pathology | Histoquimica con lectinas de mucosa nasal bovina normal e infectada con herpesvirus; sin relacion con glicina como tratamiento. |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Preclinico (formulacion de administracion) | Chemical & Pharmaceutical Bulletin | Oligoarginina unida a polimeros como adyuvante mucoso para inducir anticuerpos en cavidades nasales de ratones; sin relacion con glicina. |

## Informacion de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmaceutica | Indicacion Aprobada |
|---------|------|------|-----------|
| 20216947 (cancelado) | NUTRIFLEX® OMEGA SPECIAL NOVO | Emulsion inyectable | Emulsiones lipidas |

## Consideraciones de Seguridad

- **Contraindicaciones segun el grafo de conocimiento (TxGNN/PrimeKG, no provienen del prospecto)**: enfermedad renal (incluida enfermedad renal cronica, insuficiencia renal cronica y terminal), nefrolitiasis, nefrocalcinosis, nefropatia aguda por uratos, hipercalcemia (incluida la hipercalcemia humoral de neoplasias), hiperparatiroidismo, osteitis fibrosa, sarcoidosis, hiperfosfatemia y trastornos del metabolismo del fosforo, enfermedad cardiaca y cardiovascular, fibrilacion ventricular, intoxicacion digitalica, arteriosclerosis obliterante, hipervitaminosis, estrenimiento, lesiones oseas metastasicas liticas, piouréter, fenilcetonuria y otros trastornos del metabolismo de la fenilalanina.
- No se encontraron interacciones farmacologicas registradas en las fuentes consultadas.

Consultar el prospecto para informacion de advertencias y contraindicaciones oficiales, ya que no se pudo obtener esa informacion.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion se basa solo en el modelo computacional (L5): no hay ensayos ni literatura que evaluen la glicina en enfermedad nasal, no se conoce su mecanismo de accion y el unico registro sanitario esta cancelado. La segunda indicacion predicha (laringofaringitis aguda) tampoco tiene ensayos ni literatura.

**Para avanzar se necesita:**
- Obtener el mecanismo de accion desde DrugBank y formular una hipotesis mecanistica para la via aerea superior
- Descargar y analizar el prospecto del INVIMA para conocer advertencias y contraindicaciones oficiales
- Realizar estudios preclinicos o revision sistematica que evaluen la glicina en patologia nasal
- Evaluar la compatibilidad de via de administracion (la unica forma registrada es una emulsion inyectable, no apta para uso nasal)
- Verificar si existe una via de acceso regulatorio, dado que el unico registro esta cancelado
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

