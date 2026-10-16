---
layout: default
title: Loperamide
parent: Solo Predicción del Modelo (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Loperamide: nueva indicación predicha, Conjuntivitis contagiosa aguda (nivel de evidencia L5). Indicación original: Loperamida"
---

# Loperamide
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

# Loperamida: De Antidiarreico a Conjuntivitis Contagiosa Aguda

## Resumen en Una Frase

Loperamida es un antidiarreico oral (agonista opioide periférico), cuyo registro sanitario en Colombia solo indica "LOPERAMIDA" como indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis contagiosa aguda**, pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo, sin plausibilidad mecanística identificada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Loperamida (el texto del registro no detalla la indicación; corresponde al uso antidiarreico conocido del fármaco) |
| Nueva Indicación Predicha | Conjuntivitis contagiosa aguda |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, loperamida es un agonista de receptores opioides mu de acción periférica que actúa sobre las neuronas del plexo mientérico intestinal y reduce la motilidad gastrointestinal, lo que explica su uso en la diarrea.

**La predicción no resulta razonable desde el punto de vista mecanístico.** No existe un vínculo plausible entre la reducción de la motilidad intestinal y la inflamación infecciosa de la conjuntiva. El puntaje alto de TxGNN (99.97%) es solo una predicción del modelo y probablemente es un artefacto del grafo de conocimiento. Además, varias predicciones del mismo grupo (conjuntivitis, conjuntivitis pseudomembranosa, conjuntivitis folicular crónica, foliculosis conjuntival, conjuntivitis serosa, conjuntivitis parasitaria) comparten puntajes idénticos o casi idénticos, lo que sugiere una propagación por ontología y no una señal independiente.

Entre las otras predicciones evaluadas, **disentería amebiana** (99.95%) y **gastroduodenitis** (99.77%) son más cercanas al campo gastrointestinal, pero la literatura disponible las muestra como señales de **daño**, no de eficacia (véase Consideraciones de Seguridad).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para conjuntivitis contagiosa aguda.

Como referencia, para otras indicaciones predichas existe la siguiente literatura, que sugiere riesgos y no beneficios:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Reporte de caso | Journal of Travel Medicine | Colitis amebiana fulminante tras uso intenso de loperamida; el fármaco pudo influir en el curso de la enfermedad (megacolon tóxico). |
| [41924411](https://pubmed.ncbi.nlm.nih.gov/41924411/) | 2026 | Reporte de caso | Cureus | Depresión respiratoria inducida por loperamida en inflamación gastrointestinal grave secundaria a quimioterapia, probablemente por mayor absorción sistémica con la barrera intestinal comprometida. |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Revisión | The American Journal of Medicine | Revisión del tratamiento no líquido y la quimioprofilaxis de la diarrea aguda; los agentes inespecíficos reducen los síntomas de la diarrea. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 34537 | Loperamida Tabletas por 2 mg (Laboratorios Ecar S.A.) | Tableta | Loperamida (cancelado) |
| 207751 | Loperamida Clorhidrato 2 mg Tabletas (Laproff S.A.S.) | Tableta | Loperamida (cancelado) |
| 20046526 | Loperamida Clorhidrato 2 mg (Genfar S.A.) | Tableta | Loperamida (cancelado) |
| 19924345 | Pangetan NF Tabletas (Tecnoquímicas S.A.) | Tableta | Loperamida (cancelado) |

Los 4 registros están cancelados; actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no según el prospecto):** enfermedad hepática, enfermedad de la vesícula biliar, íleo paralítico, obstrucción intestinal, miopatía visceral familiar, disentería, enfermedad diarreica, enfermedad diarreica infecciosa y enfermedad infecciosa intestinal.
- **Señales de seguridad en la literatura:**
  - Colitis amebiana fulminante y megacolon tóxico asociados al uso de loperamida en infecciones invasivas.
  - Depresión respiratoria en inflamación gastrointestinal grave, por posible aumento de la absorción sistémica.
- **Interacciones farmacológicas:** se identificaron 591 interacciones. Entre las de nivel **Mayor**: abiraterona, ranitidina, fosamprenavir y gemfibrozilo. Entre las de nivel **Moderado**: clorfeniramina, dihidrocodeína, codeína, tramadol, acrivastina, salbutamol, etanol, foscarnet, fostamatinib, fostemsavir, galantamina, gemifloxacino, gilteritinib, alfuzosina, feniltoloxamina y cetirizina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para conjuntivitis contagiosa aguda es solo del modelo (L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible. Todas las predicciones evaluadas quedan en Hold, y las señales disponibles en indicaciones gastrointestinales apuntan a riesgos de seguridad y no a oportunidades de reposicionamiento. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consultar DrugBank).
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad.
- Una hipótesis biológica plausible que vincule la acción opioide periférica con la patología ocular, y estudios preclínicos que la respalden.
- Confirmar si existe alguna vía de administración compatible (la única forma registrada es la tableta oral, no apta para uso ocular).
- Revisar si el puntaje alto proviene de un artefacto de propagación en el grafo de conocimiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

