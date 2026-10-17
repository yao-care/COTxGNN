---
layout: default
title: Azithromycin
parent: Solo Predicción del Modelo (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Azithromycin: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (nivel de evidencia L5). Indicación original: Azitromicina"
monitor_inn: "Azithromycin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Azithromycin
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

# Azitromicina: De Indicación Original (Azitromicina) a Síndrome de Hiperviscosidad Policlonal

## Resumen en Una Frase

Azitromicina es un antibiótico macrólido, registrado en Colombia bajo la indicación genérica "azitromicina".
El modelo TxGNN predice que podría ser efectivo para **síndrome de hiperviscosidad policlonal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Azitromicina (el registro sanitario no detalla la indicación clínica) |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 7 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la información conocida, la azitromicina es un antibiótico macrólido con actividad antibacteriana y propiedades inmunomoduladoras y antiinflamatorias descritas en la literatura general.

Los datos compilados no respaldan un vínculo mecanístico entre la azitromicina y el síndrome de hiperviscosidad policlonal. El puntaje alto de TxGNN (0.998) proviene únicamente de las relaciones del grafo de conocimiento y no está acompañado de ensayos clínicos, literatura ni análisis de similitud con la indicación original.

Por tanto, esta predicción debe considerarse una hipótesis sin sustento y no una recomendación de uso.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

Como referencia, entre las demás predicciones del modelo, la única con ensayos registrados es "trastorno hematológico congénito" (enfermedad de células falciformes). Allí aparecen dos ensayos con azitromicina o macrólidos que fueron **retirados sin inscribir pacientes**, por lo que no generaron datos:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02960503](https://clinicaltrials.gov/study/NCT02960503) | Fase 1/2 | Retirado | 0 | Macrólidos para mejorar el VEF1 en adultos con enfermedad de células falciformes |
| [NCT02630394](https://clinicaltrials.gov/study/NCT02630394) | Fase 1 | Retirado | 0 | Profilaxis con azitromicina del síndrome torácico agudo en enfermedad de células falciformes |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Reclutando | 5000 | Estudio general de farmacocinética y seguridad de fármacos poco estudiados en niños; no específico de enfermedades hematológicas |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el síndrome de hiperviscosidad policlonal.

---

## Información de Mercado en Colombia

Los 7 registros sanitarios están **cancelados**; no hay registros vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19911014 | PENFLUZ 500 MG TABLETAS | Tableta | Azitromicina |
| 20068317 | AKRIBACT® | Tableta | Azitromicina |
| 19970784 | AZITROFAR® TABLETAS | Tableta | Azitromicina |
| 20189232 | AZITROMICINA 500MG | Tableta recubierta | Azitromicina |
| 20099969 | MILAGRAM® TABLETAS | Tableta | Azitromicina |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: síndrome de QT largo (incluido el familiar), torsades de pointes, enfermedad hepática, enfermedad de la vesícula biliar, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, miastenia gravis, enfermedad de la unión neuromuscular, trastornos de la audición y enfermedades del sistema auditivo.
- **Interacciones farmacológicas**: la consulta no identificó interacciones fármaco-fármaco clásicas. Solo se registraron dos interacciones farmacológicas con dianas humanas: el receptor de motilina (MLNR) y el receptor del gusto amargo TAS2R4.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para síndrome de hiperviscosidad policlonal es de nivel L5: solo puntaje del modelo, sin ensayos, sin literatura y sin mecanismo plausible. Además, no hay registros sanitarios vigentes en Colombia y faltan los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad.
- Obtener el mecanismo de acción desde DrugBank para evaluar un posible vínculo mecanístico.
- Buscar evidencia preclínica o clínica específica en síndrome de hiperviscosidad policlonal.
- Considerar priorizar otras predicciones con señales más concretas, como la enfermedad de células falciformes (síndrome torácico agudo; actualmente solo con ensayos retirados) o la gammapatía monoclonal (evidencia preclínica in vitro en mieloma sobre bloqueo de autofagia), aunque ambas siguen siendo de evidencia indirecta.
- Aclarar la situación regulatoria (registros cancelados) antes de cualquier plan de desarrollo local.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

