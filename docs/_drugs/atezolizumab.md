---
layout: default
title: Atezolizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Atezolizumab: nueva indicación predicha, Carcinoma urotelial de la uretra prostática (nivel de evidencia L5). Indicación original: No especificada en el registro"
monitor_inn: "ATEZOLIZUMAB"
predicted_indications: ["prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
---

# Atezolizumab
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

# Atezolizumab: De Indicación No Especificada en el Registro a Carcinoma Urotelial de la Uretra Prostática

## Resumen en Una Frase

Atezolizumab es un anticuerpo monoclonal anti-PD-L1 comercializado en Colombia como TECENTRIQ®, cuyo registro sanitario no detalla una indicación específica.
El modelo TxGNN predice que podría ser efectivo para el **carcinoma urotelial de la uretra prostática**,
con **1 ensayo clínico** (Fase 1b, no específico de esta localización) y **ninguna publicación** que respalden actualmente esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto del registro solo indica "ATEZOLIZUMAB") |
| Nueva Indicación Predicha | Carcinoma urotelial de la uretra prostática |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L3 (según la evaluación de los datos compilados; evidencia limitada a un ensayo de Fase 1b) |
| Estado de Mercado en Colombia | Solo cancelado |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, atezolizumab es un anticuerpo anti-PD-L1 (inhibidor de punto de control inmunitario) que bloquea la señal con la que los tumores evaden al sistema inmune. Esta descripción proviene del conocimiento general del fármaco, no de los datos compilados para este informe.

El epitelio urotelial de la uretra prostática comparte histología y biología de PD-L1 con el urotelio de la vejiga, donde atezolizumab ha mostrado actividad clínica. Por ello, mecanísticamente podría ser aplicable a esta localización. Sin embargo, el único ensayo disponible es un estudio de tipo "basket" de Fase 1b, con población mixta y sin datos de eficacia específicos para esta localización. Tampoco hay literatura que lo respalde de forma directa.

Otras predicciones del modelo con puntajes similares (carcinomas uroteliales de pelvis renal y variante sarcomatoide de vejiga) comparten la misma lógica de PD-L1, pero no cuentan con ensayos ni publicaciones en los datos compilados.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Fase 1b | Activo, sin reclutar | 914 | Escalada de dosis de cabozantinib solo o con atezolizumab en tumores sólidos localmente avanzados o metastásicos (incluye carcinoma urotelial de vejiga, pelvis renal, uréter y uretra, además de carcinoma renal, próstata, pulmón, mama triple negativo y ovario). Evalúa seguridad, tolerabilidad, eficacia preliminar y farmacocinética. Relevancia indirecta. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20145962 (cancelado) | TECENTRIQ® | Solución inyectable | ATEZOLIZUMAB |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-PD-L1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 75 interacciones en total. Entre las mostradas, las de nivel **mayor** son:
  - Adalimumab
  - Baricitinib
  - Vacuna BCG (cepa Tice, antígeno vivo)

  Las de nivel **moderado** incluyen corticosteroides (hidrocortisona, triamcinolona, betametasona, budesonida, dexametasona, prednisolona, prednisona, metilprednisolona, deflazacort), roflumilast, azatioprina, alefacept, alemtuzumab, anakinra y varias vacunas (toxoide tetánico, ántrax, adenovirus tipo 4).

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados; consultar el prospecto para esa información.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El único ensayo para el carcinoma urotelial de la uretra prostática es un estudio de Fase 1b multitumoral sin datos de eficacia específicos, no hay literatura de respaldo, y el registro sanitario en Colombia está cancelado. La predicción del modelo es muy alta, pero la evidencia clínica es insuficiente para avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto (advertencias y contraindicaciones), ya que falta información de seguridad que bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Aclarar la indicación original y la situación regulatoria actual en Colombia (registro cancelado).
- Buscar estudios específicos en carcinoma urotelial de uretra prostática o de tracto superior, con datos de eficacia.
- Evaluar la relevancia de los hallazgos en cáncer cervical (rango 6: endocervical, con ensayo de Fase 2 completado de solo 11 pacientes) como línea alternativa con mayor soporte clínico relativo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

