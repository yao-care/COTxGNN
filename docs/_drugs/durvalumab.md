---
layout: default
title: Durvalumab
parent: Solo Predicción del Modelo (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Durvalumab: nueva indicación predicha, Carcinoma urotelial de la uretra prostática (nivel de evidencia L5). Indicación original: No disponible"
monitor_inn: "DURVALUMAB"
predicted_indications: ["prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
---

# Durvalumab
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

# Durvalumab: De Indicación Original No Especificada a Carcinoma Urotelial de la Uretra Prostática

## Resumen en Una Frase

Durvalumab es un anticuerpo anti-PD-L1 comercializado en Colombia como IMFINZI®. En los datos compilados para este informe, el registro sanitario no detalla una indicación aprobada (solo figura el nombre del principio activo).
El modelo TxGNN predice que podría ser efectivo para el **carcinoma urotelial de la uretra prostática**, pero **no hay ensayos clínicos ni publicaciones** que respalden específicamente esta indicación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el registro sanitario solo indica "DURVALUMAB", sin texto de indicación) |
| Nueva Indicación Predicha | Carcinoma urotelial de la uretra prostática |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, durvalumab es un anticuerpo monoclonal que bloquea PD-L1, restableciendo la capacidad del sistema inmune para atacar células tumorales. Este mecanismo está establecido en el carcinoma urotelial de vejiga.

El carcinoma urotelial de la uretra prostática comparte la histología urotelial con el de vejiga, por lo que es biológicamente plausible que dependa de una vía PD-L1 similar. Esto hace coherente la predicción del modelo.

Sin embargo, esta plausibilidad es una extrapolación: no se aportaron ensayos ni literatura para este sitio anatómico específico, por lo que la predicción sigue siendo solo computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

*Nota de contexto:* para otras indicaciones predichas de la misma familia urotelial sí existen ensayos (por ejemplo, [NCT03912818](https://clinicaltrials.gov/study/NCT03912818), Fase 2, terminado con solo 7 participantes, en cáncer de vejiga de histología variante; y [NCT02812420](https://clinicaltrials.gov/study/NCT02812420), Fase 1 temprana, 54 participantes, en carcinoma urotelial músculo-invasivo). No son específicos de la uretra prostática y no sustentan conclusiones de eficacia para ella.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20143749 (cancelado) | IMFINZI® 50 MG/ML concentrado para solución para infusión (AstraZeneca Colombia S.A.S) | Solución concentrada para infusión | DURVALUMAB (sin texto de indicación detallado) |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (inhibidor del punto de control inmune anti-PD-L1) |
| Riesgo de Mielosupresión | Bajo en general, a diferencia de los citotóxicos convencionales; consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma, función hepática, renal y tiroidea; vigilancia de eventos adversos inmunomediados |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 81 interacciones en total. Las más relevantes de la muestra disponible son:
  - **Mayor:** adalimumab.
  - **Moderadas:** corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona, metilprednisolona, deflazacort), roflumilast, alefacept, alemtuzumab, anakinra, toxoide tetánico y vacuna contra el ántrax.
  - **Menores:** sales de zinc (acetato, gluconato, sulfato, cloruro).

  Es de esperar que los inmunosupresores interfieran con el efecto inmunomediado del fármaco.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.98%) y es mecanísticamente plausible, pero está en nivel L5: no existen ensayos ni literatura específicos para el carcinoma urotelial de la uretra prostática. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Búsqueda de evidencia clínica y publicaciones específicas en carcinoma urotelial de uretra prostática, o estudios en urotelial de vejiga que incluyan este subsitio.
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Prospecto con advertencias y contraindicaciones, descargado del sitio de INVIMA.
- Aclarar la indicación aprobada original y el motivo de la cancelación del registro, y evaluar la situación regulatoria vigente en Colombia.
- Análisis de compatibilidad de vía de administración y similitud con la indicación original (actualmente pendientes).
- Considerar otras predicciones con más evidencia, como el carcinoma urotelial de vejiga de variante sarcomatoide (L2) y el carcinoma endocervical (L3), como candidatas prioritarias.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

