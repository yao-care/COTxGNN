---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 5
---

# Etonogestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Etonogestrel: De Anticoncepción a Amenorrea

## Resumen en Una Frase

Etonogestrel es un progestágeno sintético utilizado principalmente como anticonceptivo de larga duración en implante subdérmico (Implanon/Nexplanon), cuyo mecanismo principal es la supresión del eje hipotálamo-hipófisis-ovario.
El modelo TxGNN predice que podría estar asociado con **Amenorrea (enfermedad)**,
con **1 ensayo clínico** y **2 publicaciones** recuperadas, aunque ninguna respalda directamente su uso como tratamiento de la amenorrea.

> ⚠️ **Nota de interpretación:** El análisis de plausibilidad mecanística sugiere que esta predicción puede reflejar una **confusión de dirección causal**: etonogestrel *induce* amenorrea como efecto farmacológico, en lugar de *tratar* la amenorrea como condición patológica.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Anticoncepción hormonal de larga duración (implante subdérmico) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L4 (estudios de mecanismo; sin ensayos diseñados para tratar amenorrea) |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción desde la fuente DrugBank (gap identificado). Sin embargo, por información farmacológica conocida, etonogestrel es un progestágeno sintético de tercera generación —metabolito activo del desogestrel— que actúa como agonista selectivo del receptor de progesterona (PR). Su principal mecanismo anticonceptivo es la supresión del pico de LH, inhibición de la ovulación y alteración del moco cervical.

La relación entre etonogestrel y la amenorrea es directa, pero **en sentido inverso al de un reposicionamiento terapéutico tradicional**: el fármaco suprime el eje HPO (hipotálamo-hipófisis-ovario), lo que frecuentemente provoca amenorrea como consecuencia farmacológica en usuarias del implante (entre el 20–30% de las usuarias reportan ausencia de sangrado). El modelo TxGNN probablemente detectó esta fuerte asociación en el grafo de conocimiento y la interpretó como indicación tratable.

Existe un escenario de reposicionamiento conceptualmente posible: el uso de **amenorrea inducida como objetivo terapéutico** en condiciones como endometriosis severa o menorragia refractaria. No obstante, ninguno de los ensayos o publicaciones recuperadas está diseñado con ese objetivo, por lo que la evidencia clínica dirigida es inexistente en este paquete de evidencia.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|-----------------|------|--------|-------------|----------------------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Fase 3 | Completado | 498 | Evaluación de eficacia anticonceptiva del implante de etonogestrel en uso extendido (4.º y 5.º año). El sangrado/amenorrea se evalúa como resultado secundario de seguridad, **no como indicación terapéutica de amenorrea**. |

> **Advertencia de relevancia (Grado C):** El único ensayo recuperado está diseñado para eficacia anticonceptiva. La amenorrea es un resultado secundario de patrón de sangrado, no un objetivo de tratamiento.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | ECA | Contraception | Comparación de Implanon (una varilla) vs. Norplant (seis cápsulas) en 200 mujeres durante 2–4 años en China. Sin embarazos; evalúa patrones de sangrado incluyendo amenorrea como resultado de tolerabilidad, no de tratamiento. |
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | ECA (protocolo) | Trials | Protocolo de ensayo para BIO101 en deterioro respiratorio por COVID-19. **Sin relación con etonogestrel ni con amenorrea.** Posible falso positivo en la búsqueda bibliográfica. |

> **Nota:** Ninguna de las publicaciones recuperadas evalúa etonogestrel como tratamiento de la amenorrea. La publicación PMID 33430924 es un falso positivo no relacionado con el fármaco ni la indicación.

---

## Información de Mercado en Colombia

Etonogestrel **no cuenta con registros sanitarios vigentes en Colombia** según los datos disponibles. No se han encontrado licencias de comercialización, por lo que no hay productos aprobados que listar.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> Los datos de advertencias clave, contraindicaciones e interacciones farmacológicas no están disponibles en este paquete de evidencia. Se recomienda revisar la ficha técnica oficial de Implanon/Nexplanon y consultar las bases de datos de seguridad de DrugBank y la FDA antes de cualquier evaluación clínica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN refleja una **confusión de dirección causal**: etonogestrel suprime el eje HPO e *induce* amenorrea como efecto farmacológico esperado, pero esto no equivale a una indicación terapéutica para tratar la amenorrea patológica. El único ensayo recuperado (Fase 3) estudia eficacia anticonceptiva, no tratamiento de amenorrea; la evidencia de literatura no es relevante para la indicación predicha; y el fármaco no está comercializado en Colombia, lo que añade una barrera regulatoria adicional.

**Para reconsiderar se necesita:**
- Redefinir la hipótesis clínica: si el objetivo es evaluar la **amenorrea inducida como beneficio terapéutico** (p. ej., en endometriosis o menorragia), reformular la indicación y buscar evidencia específica para esas condiciones
- Obtener el mecanismo de acción completo desde DrugBank (Data Gap DG002) para confirmar la selectividad PR y sus efectos endometriales
- Consultar las advertencias y contraindicaciones del prospecto oficial (Data Gap DG001) antes de cualquier evaluación de seguridad
- Verificar si existen ensayos diseñados específicamente para amenorrea inducida como endpoint primario terapéutico en condiciones ginecológicas crónicas
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

