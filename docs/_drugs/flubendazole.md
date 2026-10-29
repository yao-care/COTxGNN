---
layout: default
title: Flubendazole
parent: Solo Predicción del Modelo (L5)
nav_order: 288
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-29
description: "Flubendazole: nueva indicación predicha, Carcinoma de vejiga urinaria (urinary bladder carcinoma) (nivel de evidencia L5). Indicación original: Flubendazol"
monitor_inn: "flubendazole"
predicted_indications: ["urinary bladder carcinoma", "urinary bladder neoplasm", "infiltrating bladder urothelial carcinoma", "non-invasive bladder urothelial carcinoma", "bladder urachal urothelial carcinoma", "bladder squamous papilloma", "bladder signet ring cell adenocarcinoma", "bladder colloid adenocarcinoma", "bladder mixed adenocarcinoma", "bladder colonic type adenocarcinoma"]
---

# Flubendazole
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

## Flubendazol: De Antihelmíntico (Flubendazol) a Carcinoma de Vejiga Urinaria
{: .text-alpha }

## Resumen en Una Frase

Flubendazol es un antihelmíntico bencimidazólico, registrado en Colombia bajo el principio activo "flubendazol" en suspensión oral y tabletas.
El modelo TxGNN predice que podría ser efectivo para el **carcinoma de vejiga urinaria**,
pero actualmente **no hay ensayos clínicos** ni **publicaciones sobre flubendazol** que respalden esta dirección; solo existen 2 publicaciones preclínicas con fenbendazol, un fármaco análogo, para la neoplasia de vejiga (indicación ubicada en el segundo lugar de la lista de predicciones).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Flubendazol (el registro sanitario solo indica el principio activo, sin texto de indicación detallado; antihelmíntico según la clase del fármaco) |
| Nueva Indicación Predicha | Carcinoma de vejiga urinaria (urinary bladder carcinoma) |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 4 de 6) |
| Número de Registros Sanitarios | 6 (vigentes: 4) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, flubendazol pertenece a la clase de los bencimidazoles antihelmínticos. En general, esta clase se une a la beta-tubulina e interfiere con la polimerización de los microtúbulos. Esta descripción proviene del conocimiento general de la clase y no está respaldada por los datos suministrados.

Mecanísticamente, la alteración de los microtúbulos es una vía antimitótica plausible en células tumorales, lo que podría aplicarse al cáncer de vejiga. Sin embargo, la relación entre la indicación original (antiparasitaria) y la nueva indicación (oncológica) es solo inferida; no se ha evaluado formalmente la similitud entre ambas.

Las dos publicaciones disponibles estudian fenbendazol (no flubendazol) en cáncer de vejiga, en combinación con terapia fototérmica y con CRISPR-Cas13a. Ofrecen apoyo indirecto a nivel de clase, pero no demuestran eficacia de flubendazol ni eficacia en humanos. El puntaje alto del modelo (0.9999) es una predicción computacional y, en los subtipos raros de vejiga de la lista, probablemente refleja la cercanía en la ontología de enfermedades con otras neoplasias de vejiga.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la predicción principal (carcinoma de vejiga urinaria) no hay literatura disponible. Para la predicción relacionada "neoplasia de vejiga urinaria" se identificaron las siguientes publicaciones, que tratan sobre **fenbendazol, no flubendazol**:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41861111](https://pubmed.ncbi.nlm.nih.gov/41861111/) | 2026 | Preclínico (inferido del título) | Advanced Science | Nanoplataforma intravesical con fenbendazol que combina inducción de ferroptosis, muerte celular inmunogénica y terapia fototérmica contra el cáncer de vejiga |
| [39128990](https://pubmed.ncbi.nlm.nih.gov/39128990/) | 2024 | Preclínico (inferido del título) | J Exp Clin Cancer Res | Instilación intravesical que combina CRISPR-Cas13a con fenbendazol para el cáncer de vejiga |

---

## Información de Mercado en Colombia

Los 6 registros sanitarios están cancelados; actualmente no hay productos vigentes con flubendazol.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 40823 | FLUOBEN® SUSPENSION 2% | Suspensión oral | Flubendazol |
| 20020871 | FERITREX® SUSPENSION | Suspensión oral | Flubendazol |
| 20039210 | DECAFLUSAN® 500 MG TABLETAS | Tableta | Flubendazol |
| 19959902 | FERITREX® 500 MG TABLETAS | Tableta | Flubendazol |
| 19929393 | FUGOS SUSPENSIÓN | Suspensión oral | Flubendazol |

*(Existe además un sexto registro cancelado: 19960792, FLUBENDAZOL 300 MG, tableta, de PROCAPS S.A.)*

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo TxGNN (nivel de evidencia L5): no hay ensayos clínicos, no hay literatura sobre flubendazol en esta indicación y los estudios disponibles usan otro fármaco (fenbendazol). Además, el fármaco está comercializado en Colombia, con 6 registros sanitarios vigentes de 6, y faltan datos de seguridad y de mecanismo de acción.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción confirmado de flubendazol (por ejemplo, desde DrugBank).
- Conseguir el prospecto y la información de advertencias y contraindicaciones (INVIMA), necesarios antes de cualquier evaluación de seguridad.
- Estudios preclínicos específicos de flubendazol en modelos de cáncer de vejiga (in vitro e in vivo).
- Evaluar la compatibilidad de la vía de administración (oral frente a intravesical), hoy pendiente de análisis.
- Aclarar la situación regulatoria, dado que no hay registros vigentes en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

