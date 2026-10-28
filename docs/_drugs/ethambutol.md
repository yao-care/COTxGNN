---
layout: default
title: Ethambutol
parent: Solo Predicción del Modelo (L5)
nav_order: 266
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ethambutol: nueva indicación predicha, Epiglotitis (nivel de evidencia L4). Indicación original: ETMABUTOL"
monitor_inn: "ethambutol"
predicted_indications: ["epiglottitis", "laryngitis", "meningococcal infection", "peritonitis", "infectious otitis media"]
---

# Ethambutol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Etambutol: De Tuberculosis (indicación registrada como "Etambutol") a Epiglotitis
{: .text-alpha }

## Resumen en Una Frase

Etambutol es un antimicobacteriano usado originalmente como parte de los esquemas de tratamiento de la tuberculosis; el registro sanitario local solo consigna "ETMABUTOL" como indicación.
El modelo TxGNN predice que podría ser efectivo para **epiglotitis**, pero no hay ensayos clínicos y solo existe **1 publicación** (una serie de casos de tuberculosis laríngea) que se relaciona con esta dirección, por lo que la evidencia es muy débil.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ETMABUTOL (texto del registro INVIMA; corresponde al uso antituberculoso) |
| Nueva Indicación Predicha | Epiglotitis |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el etambutol inhibe la arabinosil transferasa de las micobacterias e interfiere con la síntesis de la pared celular de *Mycobacterium tuberculosis*. Su eficacia en tuberculosis está comprobada, siempre dentro de esquemas combinados.

La única evidencia vinculada a epiglotitis es una serie de 41 casos de tuberculosis laríngea (1975-1985), en la que la epiglotis fue uno de los sitios afectados y los pacientes recibieron isoniazida, rifampicina y etambutol, entre otros. Esto respalda actividad frente a la afectación tuberculosa de la vía aérea superior, no frente a la epiglotitis en general.

La epiglotitis suele ser causada por *Haemophilus influenzae* tipo b y otras bacterias que el etambutol no cubre, ya que su actividad se limita a micobacterias. Por ello, el puntaje alto del modelo probablemente refleja la cercanía en la red de conocimiento con la tuberculosis laríngea y no una base mecanística real para la indicación predicha.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Serie de casos | The European Respiratory Journal | 41 casos de tuberculosis laríngea; la epiglotis fue el segundo sitio más afectado tras las cuerdas vocales verdaderas. El tratamiento incluyó isoniazida, rifampicina y etambutol, entre otros. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20272629 (cancelado) | ECOX® 400 MG TABLETAS | Tableta recubierta | ETMABUTOL |

---

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación (según grafo de conocimiento, no texto del prospecto)**: enfermedad renal, piouréter, gota, retinopatía diabética, catarata diabética y neuritis óptica.
- **Interacciones Farmacológicas**: se identificaron 112 interacciones. Las de nivel moderado incluyen metronidazol, ácido picosulfúrico, naltrexona, rosuvastatina, simvastatina, tinidazol e hidróxido de aluminio. Otras de nivel no clasificado incluyen clotrimazol, pantoprazol, morfina, omeprazol, lansoprazol, vancomicina, prednisona, nistatina, hidrocortisona, cloruro de potasio, sulfasalazina, prednisolona y ranitidina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos y la única publicación es una serie de casos de tuberculosis laríngea en la que el etambutol formaba parte de un esquema combinado. No hay base mecanística para tratar la epiglotitis bacteriana habitual, y el producto local tiene su único registro cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) para completar el análisis de seguridad
- Evidencia clínica específica que distinga la epiglotitis tuberculosa de la epiglotitis bacteriana común
- Verificar si existe algún producto con etambutol vigente en Colombia
- Considerar que otras indicaciones predichas (laringitis, peritonitis) también se limitan a formas tuberculosas, donde el etambutol ya es parte del tratamiento estándar y no constituye un reposicionamiento real
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

