---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 8
---

# Moroctocog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Moroctocog Alfa: De Hemofilia A a Trastorno Primario de Liberación de Plaquetas

## Resumen en Una Frase

Moroctocog alfa es un Factor VIII recombinante con dominio B eliminado (BDD-rFVIII), originalmente utilizado para el tratamiento y profilaxis de episodios hemorrágicos en pacientes con Hemofilia A.
El modelo TxGNN predice que podría ser efectivo para el **Trastorno Primario de Liberación de Plaquetas**,
con **7 ensayos clínicos** identificados (todos de relevancia indirecta, Grado C) y **ninguna publicación** que respalde directamente esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemofilia A (tratamiento y profilaxis de episodios hemorrágicos) |
| Nueva Indicación Predicha | Trastorno Primario de Liberación de Plaquetas |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de moroctocog alfa. Según la información conocida, moroctocog alfa es un Factor VIII recombinante con dominio B eliminado, cuya eficacia en Hemofilia A ha sido ampliamente comprobada a través de múltiples ensayos clínicos de Fase 3. Su función central consiste en suplir la deficiencia del Factor VIII en la vía de coagulación intrínseca, facilitando la formación del complejo Xasa (Factor VIIIa + Factor IXa) para la generación de trombina y la hemostasia secundaria.

Sin embargo, la relación mecanística entre moroctocog alfa y el **Trastorno Primario de Liberación de Plaquetas** es débil. Este trastorno se caracteriza por defectos en la secreción de gránulos densos o alfa de las plaquetas (como en el síndrome de Hermansky-Pudlak o el síndrome de la plaqueta gris), siendo un defecto en la hemostasia primaria de origen plaquetario. El Factor VIII actúa exclusivamente en la hemostasia secundaria y no tiene efecto directo sobre la función secretora de los gránulos plaquetarios.

Desde una perspectiva patofisiológica, los mecanismos de la indicación original (deficiencia de FVIII → fallo de coagulación secundaria) y la nueva indicación predicha (fallo de liberación de gránulos plaquetarios → alteración de hemostasia primaria) no se superponen. La alta puntuación TxGNN probablemente refleja una asociación de red basada en la categoría compartida de "trastornos hemorrágicos por coagulopatía/trombocitopatía", más que una relación farmacológica directa.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Fase 3 | Completado | 159 | Eficacia y seguridad de BIVV001 (rFVIIIFc-VWF-XTEN) en profilaxis de Hemofilia A severa en pacientes ≥12 años |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Fase 3 | Completado | 74 | Seguridad y eficacia de BIVV001 en pacientes pediátricos (<12 años) con Hemofilia A severa |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Fase 3 | Completado | 30 | Eficacia y seguridad de BAX 855 (rFVIII PEGilado) en Hemofilia A severa sometidos a procedimientos quirúrgicos electivos |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | No iniciado | 80 | Perfil clínico-hematológico y de coagulación en pacientes con leucemia mieloide aguda bajo quimioterapia de inducción intensiva |
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | Reclutando | 200 | Evaluación de síntomas clínicos y recuperación en pacientes con síndrome post-vacunación COVID-19 |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | Reclutando | 25 | Sistema de soporte hepático artificial (DPMAS + TPE) en fallo hepático agudo sobre crónico: efecto en coagulación primaria y función orgánica |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | Reclutando | 45 | Exploración de hemostasia sistémica y portal en pacientes con colocación de TIPS (shunt portosistémico intrahepático) |

> **Nota:** Todos los ensayos identificados tienen relevancia indirecta (Grado C). Ninguno evalúa directamente moroctocog alfa para el trastorno primario de liberación de plaquetas; la mayoría corresponde a ensayos sobre Hemofilia A con otras moléculas rFVIII o estudios observacionales de coagulopatías no relacionadas.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el uso de moroctocog alfa en trastorno primario de liberación de plaquetas.

---

## Información de Mercado en Colombia

Moroctocog alfa **no cuenta con registros sanitarios activos en Colombia**. No se identificaron licencias ni productos comercializados bajo esta denominación común internacional en el sistema regulatorio consultado.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
A pesar del alto puntaje TxGNN (99.97%), la base mecanística es insuficiente para respaldar este reposicionamiento: moroctocog alfa actúa en la coagulación secundaria (vía intrínseca, complejo Xasa), mientras que el trastorno primario de liberación de plaquetas es un defecto de hemostasia primaria plaquetaria (fallo de secreción granular) que no se ve corregido por la suplementación de FVIII. No existe ningún ensayo clínico ni publicación que evalúe directamente este uso, y la totalidad de los ensayos encontrados son de relevancia indirecta (todos Grado C). El nivel de evidencia es L5 (predicción de modelo sin respaldo de estudios reales).

**Para avanzar se necesita:**
- Obtener datos del mecanismo de acción (MOA) completo de moroctocog alfa desde DrugBank (actualmente Data Gap)
- Recuperar las advertencias, contraindicaciones y datos de seguridad desde el prospecto oficial (FDA/EMA/INVIMA)
- Estudios preclínicos que exploren si existe algún vínculo indirecto entre el eje FVIII/VWF y la función secretora de gránulos plaquetarios
- Revisión de hipótesis mecanística alternativa antes de considerar cualquier paso clínico
- Evaluación de estrategia regulatoria en Colombia, donde el fármaco aún no está comercializado y requeriría proceso de registro sanitario completo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

