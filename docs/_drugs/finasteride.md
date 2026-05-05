---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 6
---

# Finasteride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Usando el skill **txgnn-pipeline** para orientar la generación del informe de reposicionamiento, y aplicando el formato del sistema (v5) al Evidence Pack de FINASTERIDE. A continuación el informe completo:

---

# Finasteride: De Alopecia Androgénica / Hiperplasia Prostática Benigna a Hipertricosis Universal Congénita Tipo Ambras

## Resumen en Una Frase

Finasteride es un inhibidor de la 5α-reductasa utilizado principalmente para el tratamiento de la hiperplasia prostática benigna (HPB) y la alopecia androgénica masculina, actuando mediante la reducción de dihidrotestosterona (DHT).
El modelo TxGNN predice que podría ser efectivo para la **Hipertricosis Universal Congénita Tipo Ambras (Síndrome de Ambras)**,
con **0 ensayos clínicos** y **0 publicaciones** que respalden actualmente esta dirección. La plausibilidad mecanística es extremadamente débil, ya que el síndrome de Ambras es una enfermedad genética estructural sin dependencia androgénica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperplasia prostática benigna / Alopecia androgénica masculina (sin registro en Colombia) |
| Nueva Indicación Predicha | Hipertricosis Universal Congénita Tipo Ambras |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Finasteride actúa como inhibidor selectivo de la enzima 5α-reductasa tipo II, bloqueando la conversión de testosterona en dihidrotestosterona (DHT). La DHT es el andrógeno activo que miniaturiza los folículos pilosos en la alopecia androgénica y que estimula el crecimiento del tejido prostático en la HPB. Al reducir los niveles séricos y tisulares de DHT en aproximadamente un 70%, finasteride interrumpe estas vías andrógeno-dependientes. Sin embargo, los datos de mecanismo de acción completo están actualmente marcados como pendientes en la fuente DrugBank (Data Gap), por lo que el análisis se basa en el conocimiento farmacológico establecido.

La conexión mecanística entre finasteride y el Síndrome de Ambras es, no obstante, extremadamente débil. El síndrome de Ambras (hipertricosis universalis congenita tipo Ambras) está causado por mutaciones en los genes TRPS1/EXT1, que producen una alteración estructural y genética del desarrollo folicular completamente independiente de señales androgénicas. Los folículos afectados en esta condición no responden a DHT, por lo que la inhibición de su síntesis no tendría efecto terapéutico relevante.

La discordancia entre el alto puntaje del modelo (99.99%) y la baja plausibilidad biológica indica que TxGNN ha identificado una correlación topológica en el grafo de conocimiento —ambas condiciones involucran el folículo piloso— sin que exista una relación causal real. Este es un caso ilustrativo de las limitaciones de los modelos de predicción basados en grafos cuando la similitud ontológica no refleja similitud mecanística.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la indicación Hipertricosis Universal Congénita Tipo Ambras.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación Hipertricosis Universal Congénita Tipo Ambras.

---

## Información de Mercado en Colombia

Finasteride no cuenta con registros sanitarios vigentes en Colombia (0 registros encontrados en la consulta INVIMA).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota:** Los datos de advertencias clave, contraindicaciones e interacciones farmacológicas no están disponibles en el Evidence Pack actual (marcados como Data Gap). Se recomienda obtener el prospecto oficial como paso previo a cualquier evaluación clínica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN obtiene un puntaje extremadamente alto (99.99%) pero carece de toda evidencia clínica o preclínica de soporte (nivel L5), y el mecanismo de acción de finasteride —inhibición de DHT— no tiene relevancia biológica para el Síndrome de Ambras, que es una enfermedad genética estructural no andrógeno-dependiente. La predicción refleja correlación ontológica, no mecanismo farmacológico.

**Para avanzar se necesita:**
- Identificar una hipótesis mecanística biológicamente plausible que vincule la inhibición de 5α-reductasa (o metabolitos como allopregnanolona) con los genes TRPS1/EXT1 o la vía de desarrollo folicular implicada en el síndrome de Ambras
- Datos de estudios preclínicos (in vitro / modelos animales) en hipertricosis congénita de base genética
- Confirmar el MOA completo de finasteride vía consulta a DrugBank API (actualmente Data Gap)
- Obtener el prospecto oficial (INVIMA / TFDA) para evaluación completa del perfil de seguridad antes de considerar cualquier avance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

