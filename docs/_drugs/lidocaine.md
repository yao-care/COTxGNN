---
layout: default
title: Lidocaine
parent: Solo Predicción del Modelo (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lidocaine: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: Lidocaína combinaciones"
---

# Lidocaine
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

# Lidocaína: De Lidocaína (combinaciones) a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

La lidocaína es un anestésico local que bloquea los canales de sodio, registrado en Colombia en presentaciones tópicas y rectales (supositorios, ungüento y crema).
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica; se trata de una predicción exclusivamente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lidocaína combinaciones |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Según la información conocida, la lidocaína es un bloqueador de canales de sodio dependientes de voltaje (los datos farmacológicos compilados incluyen su interacción con Nav1.2, Nav1.4, Nav1.5, Nav1.7 y Nav1.8). Su eficacia como anestésico local, por inyección y por vía tópica, está bien establecida.

Mecanísticamente, esto podría aliviar el dolor de la superficie ocular. Sin embargo, no hay evidencia de que modifique el curso de la queratoconjuntivitis epitelial punteada. Además, es conocido que el uso prolongado de anestésicos tópicos es tóxico para el epitelio corneal, por lo que un daño es plausible. La similitud con la indicación original (anestesia/analgesia local) es solo sintomática, no terapéutica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para queratoconjuntivitis epitelial punteada.

*Nota:* para la indicación de "trastorno conjuntival" (rango 6 en las predicciones) existen dos ensayos, que son de anestesia procedimental y no de tratamiento de enfermedad:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05978687](https://clinicaltrials.gov/study/NCT05978687) | Fase 4 | Completado | 41 | Gel de lidocaína vs. inyección subconjuntival de lidocaína en escisión de pterigión |
| [NCT01350024](https://clinicaltrials.gov/study/NCT01350024) | N/A | Completado | 34 | Comparación del dolor posoperatorio con dos tipos de anestesia local en cirugía de ptosis palpebral |

---

## Evidencia de Literatura

No hay literatura relacionada disponible para queratoconjuntivitis epitelial punteada. A modo de contexto, para otras indicaciones oculares predichas se identificó lo siguiente:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18989343](https://pubmed.ncbi.nlm.nih.gov/18989343/) | 2009 | ECA | Eye | Gel de lidocaína al 2% vs. gotas de tetracaína al 1% como anestésico tópico único en cirugía de pterigión primario |
| [37819721](https://pubmed.ncbi.nlm.nih.gov/37819721/) | 2023 | Estudio preclínico | JCI Insight | Asociación nervio-célula caliciforme que promueve la conjuntivitis alérgica; apoyo mecanístico indirecto |
| [29135709](https://pubmed.ncbi.nlm.nih.gov/29135709/) | 2018 | Estudio piloto | Cornea | Comparación de inyección subconjuntival, gel de lidocaína al 2% y al 5% en cirugía de pterigión |
| [15799734](https://pubmed.ncbi.nlm.nih.gov/15799734/) | 2005 | Estudio clínico | Acta Ophthalmol Scand | Eficacia del gel de lidocaína al 2% en cirugía de pterigión |
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Estudio abierto prospectivo / metaanálisis | J Neurol Neurosurg Psychiatry | Tratamiento médico de SUNCT/SUNA (cefaleas, no enfermedad conjuntival) |

Estas publicaciones corresponden a anestesia en cirugía ocular o a cefaleas, y no constituyen evidencia terapéutica para la indicación predicha.

---

## Información de Mercado en Colombia

Los tres registros sanitarios identificados están cancelados; actualmente no hay registros vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 227028 | PROCTO - GLYVENOL® Supositorios | Supositorio | Lidocaína combinaciones |
| 20265430 | AXIFER FARMET® | Ungüento tópico | Lidocaína combinaciones |
| 20021553 | LIDOMAX® | Crema tópica | Lidocaína |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** se asocian enfermedades como hipertensión, insuficiencia hepática, cirrosis, enfermedad renal, epilepsia, insuficiencia suprarrenal/enfermedad de Addison, hipotiroidismo, glaucoma de ángulo abierto, queratitis por herpes simple, infección por varicela zóster, osteoporosis, trastornos psicóticos y esquizoafectivos, dermatitis atópica, infecciones fúngicas, deficiencia de potasio y gastritis, entre otras. Estas relaciones deben verificarse con la ficha técnica antes de cualquier interpretación clínica.
- **Riesgos señalados en la literatura:** toxicidad neuropsiquiátrica y cardiológica con lidocaína intravenosa (PMID 19250287); metahemoglobinemia con uso tópico concomitante de otros fármacos inductores (caso pediátrico, PMID 41995267); mayor fracción libre de lidocaína en enfermedad renal (PMID 7037263).
- **Riesgo específico de la indicación predicha:** el uso prolongado de anestésicos tópicos puede dañar el epitelio corneal y dificultar su cicatrización.
- **Interacciones farmacológicas:** la consulta no identificó interacciones fármaco-fármaco clínicas; solo se registraron interacciones farmacológicas con dianas de canales de sodio (Nav1.2, 1.4, 1.5, 1.7 y 1.8).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos ni literatura para queratoconjuntivitis epitelial punteada. Además, existe un riesgo plausible de daño corneal con el uso prolongado de anestésicos tópicos, y no quedan registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), actualmente pendiente y bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Estudios preclínicos o clínicos que demuestren beneficio modificador de la enfermedad (no solo analgesia sintomática) y evalúen la toxicidad epitelial corneal
- Evaluar la compatibilidad de vía de administración (ocular) frente a las formas registradas (rectal y cutánea)
- Considerar que otras indicaciones predichas, como el trastorno conjuntival y la conjuntivitis atópica (ambas L4), solo ofrecen evidencia anestésica o mecanística indirecta y se clasifican como preguntas de investigación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

