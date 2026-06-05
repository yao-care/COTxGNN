---
layout: default
title: Vismodegib
parent: 僅模型預測 (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
---

# Vismodegib
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

# Vismodegib: De Carcinoma Basocelular a Meduloblastoma con Extensa Nodularidad

## Resumen en Una Frase

Vismodegib es el primer inhibidor de la vía de señalización Hedgehog aprobado a nivel global (FDA/EMA), utilizado para el tratamiento del carcinoma basocelular (BCC) localmente avanzado o metastásico. El modelo TxGNN predice que podría ser efectivo para el **meduloblastoma con extensa nodularidad (MBEN)**, con **0 ensayos clínicos** y **0 publicaciones** que respalden directamente esta indicación hasta la fecha. La predicción se sustenta en una coherencia mecanicista muy sólida: el MBEN es el subtipo de meduloblastoma SHH con mayor nivel de activación de la vía Hedgehog, el mismo blanco farmacológico de vismodegib.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicacion Original | Carcinoma basocelular localmente avanzado o metastásico (aprobación global FDA/EMA; sin registro en Colombia) |
| Nueva Indicacion Predicha | Meduloblastoma con extensa nodularidad (MBEN) |
| Puntaje de Prediccion TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Numero de Registros Sanitarios | 0 |
| Decision Recomendada | Hold |

---

## Por qué es Razonable esta Prediccion?

Vismodegib actúa como inhibidor selectivo y directo de SMO (Smoothened), un receptor transmembrana clave en la vía de señalización Hedgehog. En condiciones fisiológicas, el receptor PTCH1 suprime la actividad de SMO; cuando PTCH1 o PTCH2 presentan mutaciones de pérdida de función, SMO queda constitutivamente activo, activando los factores de transcripción de la familia GLI y desencadenando proliferación celular desregulada. Este es el mecanismo central que sustentó su aprobación en carcinoma basocelular, y el mismo que hace biológicamente plausible su aplicación en MBEN.

El meduloblastoma con extensa nodularidad (MBEN) pertenece al subtipo molecular SHH del meduloblastoma y representa la variante con mayor grado de activación de la vía Hedgehog. Las mutaciones en PTCH1/PTCH2 que conducen a la activación persistente de SMO son alteraciones definitorias de este subtipo tumoral, lo que establece una coincidencia directa entre el blanco molecular del fármaco y la fisiopatología del tumor. La justificación biológica es, por tanto, de alta coherencia mecanicista.

Sin embargo, esta base mecanicista sólida no ha sido respaldada todavía por ninguna evidencia clínica o preclínica específica para MBEN. La predicción del modelo TxGNN se apoya exclusivamente en la topología del grafo de conocimiento biomédico (nivel L5), sin ensayos clínicos ni publicaciones directamente relacionados. Una prioridad inmediata sería la búsqueda de estudios pediátricos de Fase 1/2 en meduloblastoma SHH en términos generales —en bases de datos del NCI pediátrico, SIOPE e ITCC— que podrían incluir cohortes de pacientes con MBEN o servir como punto de partida para estudios específicos.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida (inhibidor selectivo de SMO / vía Hedgehog; no es citotóxico convencional) |
| Riesgo de Mielosupresion | Bajo (el mecanismo de acción dirigido no produce supresión hematológica significativa de forma habitual) |
| Clasificacion de Emetogenicidad | Baja |
| Items de Monitoreo | Función hepática, función renal, peso corporal, prueba de embarazo obligatoria antes y durante el tratamiento |
| Proteccion en Manejo | Alto riesgo teratogénico (Categoría X en embarazo); requiere programa de gestión de riesgos (REMS); evitar cualquier contacto en personas embarazadas o con posibilidad de embarazo |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Aunque la coherencia mecanicista entre vismodegib y el MBEN es muy sólida —ambos comparten la vía SMO/Hedgehog activada por mutaciones en PTCH1/PTCH2—, la ausencia total de ensayos clínicos y publicaciones específicas para esta indicación impide avanzar más allá de una pregunta de investigación en nivel L5.

**Para avanzar se necesita:**
- Búsqueda sistemática de ensayos Fase 1/2 en meduloblastoma SHH (NCI Pediatric Oncology Branch, SIOPE, ITCC) que incluyan o permitan identificar cohortes MBEN
- Datos sobre la penetración de vismodegib en el sistema nervioso central (evaluación del paso por la barrera hematoencefálica), factor crítico dada la localización del tumor
- Datos de farmacocinética y perfil de seguridad en población pediátrica (el MBEN afecta predominantemente a niños menores de 3 años)
- Datos detallados del mecanismo de acción (actualmente con brecha de información en el sistema)
- Gestión del trámite de registro sanitario INVIMA en Colombia si la investigación clínica avanza a etapas posteriores
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

