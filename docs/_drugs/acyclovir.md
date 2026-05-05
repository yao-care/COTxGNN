---
layout: default
title: Acyclovir
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
---

# Acyclovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

El skill confirma que este es trabajo de pipeline TxGNN — procedo a generar el informe de evaluación siguiendo el formato del sistema para el Evidence Pack proporcionado.

---

# Acyclovir: De Infección por Herpes Simple a Queratoconjuntivitis Epitelial Puntata

## Resumen en Una Frase

Acyclovir es un antiviral clásico de la familia de los análogos de nucleósidos, reconocido internacionalmente por su eficacia en el tratamiento de infecciones por virus Herpes Simple (HSV-1/2) y Varicela-Zoster (VZV), aunque actualmente no cuenta con registro sanitario en Colombia. El modelo TxGNN predice que podría ser efectivo para la **Queratoconjuntivitis Epitelial Puntata**, con **0 ensayos clínicos** y **2 publicaciones** que actualmente respaldan esta dirección, ambas de carácter indirecto y sin evaluar esta indicación de forma directa.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por Herpes Simple / Varicela-Zoster (sin registro sanitario en Colombia) |
| Nueva Indicación Predicha | Queratoconjuntivitis Epitelial Puntata |
| Puntaje de Predicción TxGNN | 99.67% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Acyclovir es un profármaco análogo acíclico de guanosina que, al ser fosforilado selectivamente por la timidina quinasa codificada por los herpesvirus (HSV/VZV), se convierte en un potente inhibidor de la ADN polimerasa viral, deteniendo la replicación del virus en las células infectadas. Aunque los datos formales del mecanismo de acción no están disponibles en el expediente actual, el conocimiento farmacológico establecido es sólido: esta selectividad por la timidina quinasa viral le confiere tanto su eficacia antiherpética como una limitación fundamental para actuar sobre otros patógenos que carecen de dicha enzima.

La conexión con la queratoconjuntivitis epitelial puntata (QEP) tiene un sustento biológico plausible: el HSV-1 es uno de los agentes etiológicos reconocidos de esta patología ocular superficial. De hecho, las formulaciones oftálmicas de Acyclovir (ungüento al 3%) están aprobadas en Europa y otros mercados para la queratitis herpética superficial, que puede manifestarse precisamente como QEP. En este sentido, el modelo TxGNN captura una asociación real entre el fármaco y la patología corneal herpética.

Sin embargo, la evidencia disponible en el expediente para esta indicación específica es notablemente débil. Las dos únicas publicaciones recuperadas son series de casos que abordan condiciones distintas: la primera describe lipidosis corneal inducida por fármacos en pacientes con SIDA (sin relación con Acyclovir en QEP), y la segunda reporta queratoconjuntivitis por microsporidios (infección parasitaria intracelular, no viral). No existe ningún ensayo clínico registrado para esta combinación fármaco-indicación. La predicción del modelo, aunque mecanísticamente plausible, parece capturar una asociación general de "Acyclovir + patología ocular herpética" sin evidencia suficiente para esta presentación clínica específica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Acyclovir en queratoconjuntivitis epitelial puntata.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Serie de Casos | American Journal of Ophthalmology | Dos pacientes con SIDA bajo tratamiento para infecciones oportunistas desarrollaron cambios bilaterales en la superficie ocular compatibles con lipidosis corneal inducida por fármacos que se unen a fosfolípidos lisosomales. Evidencia indirecta; no evalúa Acyclovir en QEP. |
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Serie de Casos | Indian Journal of Pathology & Microbiology | Serie de casos de queratoconjuntivitis microsporidiana en una cohorte de la India oriental. Infección parasitaria intracelular (Microsporidia), sin vínculo directo con HSV ni con Acyclovir como tratamiento. |

---

## Información de Mercado en Colombia

Acyclovir **no cuenta con ningún registro sanitario vigente en Colombia** (INVIMA). El medicamento figura con estado **no comercializado**, con un total de **0 licencias activas**. No existe base regulatoria local para evaluar formulaciones disponibles ni indicaciones aprobadas en el mercado nacional en este momento.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN es mecanísticamente plausible dado el papel reconocido del HSV en la patología corneal superficial, pero carece completamente de evidencia clínica directa para queratoconjuntivitis epitelial puntata: ningún ensayo clínico registrado y las dos publicaciones disponibles son evidencia indirecta e irrelevante para esta indicación (nivel L4). Sumado a que Acyclovir no está comercializado en Colombia, la barrera regulatoria y evidencial es considerable para avanzar.

**Para avanzar se necesita:**
- Búsqueda dirigida de estudios clínicos con Acyclovir oftálmico (ungüento 3% o colirio) específicamente en queratoconjuntivitis herpética superficial y QEP
- Verificar si las fichas técnicas europeas o de EE.UU. de las formulaciones oftálmicas de Acyclovir incluyen la QEP como indicación explícita o implícita
- Obtención del prospecto completo y datos de mecanismo de acción formal (consulta DrugBank API, DG002)
- Datos de seguridad y advertencias de la ficha de INVIMA o equivalente internacional (DG001)
- Evaluación de viabilidad de registro o importación ante INVIMA para formulación oftálmica
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

