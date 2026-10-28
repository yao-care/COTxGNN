---
layout: default
title: Etoposide
parent: Solo Predicción del Modelo (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
monitor_inn: "etoposide"
predicted_indications: ["well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "Ewing sarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma"]
last_modified_at: 2026-10-28
description: "Etoposide: nueva indicación predicha, carcinoma adenomatoso fetal bien diferenciado del pulmón (well-differentiated fetal adenocarcinoma of the lung) (nivel de evidencia L5). Indicación original: ETO…"
---

# Etoposide
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

## Etopósido: inhibidor de la topoisomerasa II → carcinoma adenomatoso fetal bien diferenciado del pulmón (well-differentiated fetal adenocarcinoma of the lung)
{: .text-alpha }

## Resumen en Una Frase

Etopósido es un antineoplásico inhibidor de la topoisomerasa II, de uso en quimioterapia combinada.
El modelo TxGNN predice que podría ser efectivo para **carcinoma adenomatoso fetal bien diferenciado del pulmón (well-differentiated fetal adenocarcinoma of the lung)**,
pero solo se dispone de **0 ensayos clínicos** y **1 publicación** (un reporte de caso y revisión sobre un tumor relacionado pero distinto), por lo que la evidencia es muy limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ETOPOSIDO |
| Nueva Indicación Predicha | carcinoma adenomatoso fetal bien diferenciado del pulmón (well-differentiated fetal adenocarcinoma of the lung) |
| Puntaje de Predicción TxGNN | 0,9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 4 de 4) |
| Número de Registros Sanitarios | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el etopósido es un inhibidor de la topoisomerasa II que causa daño en el ADN de las células en división, y se usa en neoplasias pulmonares como el cáncer de pulmón de células pequeñas.

La nueva indicación predicha es un tumor pulmonar raro, componente del espectro del blastoma pulmonar. Mecanísticamente, un fármaco citotóxico con actividad en tumores pulmonares podría ser aplicable, pero el vínculo es indirecto.

La única publicación asociada es un reporte de caso y revisión sobre blastoma pulmonar bifásico clásico, una entidad relacionada pero distinta, en la que el paciente recibió nedaplatino más paclitaxel (no etopósido). Ningún estudio citado evalúa directamente esta enfermedad con etopósido, por lo que el nivel de evidencia se asigna como L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | Reporte de caso/Revisión | The Journal of International Medical Research | Caso de blastoma pulmonar bifásico clásico tratado con resección y quimioterapia adyuvante (nedaplatino + paclitaxel); no existen guías estándar de tratamiento por la rareza del tumor |

## Información de Mercado en Colombia

Los datos locales registran 4 registros sanitarios de etopósido en solución inyectable (monofármaco).

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20094214 | ETOSID 100 MG/ 5 ML | Solución inyectable | ETOPOSIDO |
| 20048821 | ETOPOSIDO INYECTABLE 100 MG / 5 ML | Solución inyectable | ETOPOSIDO |
| 19951646 | ETOPOSIDO 100 MG | Solución inyectable | ETOPOSIDO |
| 19982071 | ETOPOSIDO 100 MG/5 ML SOLUCION INYECTABLE. | Solución inyectable | ETOPOSIDO |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (inhibidor de la topoisomerasa II) |
| Riesgo de Mielosupresión | Alto (las contraindicaciones registradas incluyen trombocitopenia, neutropenia, leucopenia y anemia) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, equilibrio ácido-base |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Condiciones asociadas a contraindicación en los datos compilados**: trombocitopenia, neutropenia, agranulocitosis, anemia, anemia macrocítica, enfermedad pulmonar intersticial, insuficiencia renal, acidosis (incluida la metabólica), lesión hepática inducida por fármacos, leucopenia y fibrosis pulmonar (incluida la postinflamatoria). Estas provienen de relaciones de contraindicación fármaco-enfermedad y no del texto del prospecto.
- **Interacciones farmacológicas**: se registran 495 interacciones. Entre las de nivel moderado figuran aprepitant, metronidazol, eliglustat, rolapitant, rosuvastatina, simvastatina y tinidazol; levofloxacino es de nivel menor.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la única publicación vinculada es un reporte de caso sobre una entidad relacionada pero distinta, sin uso de etopósido. El puntaje alto del modelo (0,9994) no basta para respaldar avanzar.

**Para avanzar se necesita:**
- Literatura o ensayos que estudien directamente esta enfermedad con etopósido
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones oficiales)
- Evaluación de seguridad hematológica y de interacciones en la población objetivo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

