---
layout: default
title: Risdiplam
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 1
---

# Risdiplam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Risdiplam: De Atrofia Muscular Espinal a Acné

## Resumen en Una Frase

Risdiplam es un modulador de splicing de ARNm desarrollado para el tratamiento de la Atrofia Muscular Espinal (AME), actuando sobre el gen SMN2 para aumentar los niveles de la proteína SMN funcional en el sistema neuromuscular.
El modelo TxGNN predice que podría ser efectivo para **Acné**,
sin embargo, **no existe ninguna evidencia clínica ni preclínica** que respalde esta dirección — ni ensayos clínicos ni publicaciones registradas apoyan esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Atrofia Muscular Espinal (AME) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 99.45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Sin embargo, Risdiplam (conocido comercialmente como Evrysdi®) es un fármaco de pequeña molécula desarrollado por Roche para la Atrofia Muscular Espinal (AME). Su mecanismo central consiste en modificar el splicing del pre-ARNm de SMN2, promoviendo la inclusión del exón 7 y aumentando la producción de la proteína SMN de longitud completa, que es crítica para la supervivencia de las neuronas motoras espinales.

El acné vulgar, en cambio, tiene una fisiopatología completamente ajena a este mecanismo: sobreactivación de las glándulas sebáceas impulsada por andrógenos, queratinización anormal del folículo piloso, proliferación excesiva de *Cutibacterium acnes* y una cascada inflamatoria mediada por IL-1α, TNF-α e IL-8. No existe ninguna vía molecular publicada que conecte los niveles de proteína SMN con la secreción de sebo, la señalización de receptores androgénicos ni la respuesta inmune frente a *C. acnes*.

La puntuación elevada de TxGNN (0.9945) muy probablemente es un **falso positivo estadístico** originado en la co-ocurrencia de términos como "inflamación" en el grafo de conocimiento, y no refleja una relación biológica real. La conexión mecanística entre Risdiplam y el acné se considera extremadamente débil y sin sustento científico actual.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Risdiplam no cuenta con registros sanitarios activos en Colombia. La consulta a la base regulatoria no arrojó ninguna licencia registrada para este principio activo.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece por completo de respaldo experimental o clínico (Nivel L5), y el análisis mecanístico indica que la conexión entre el mecanismo de acción de Risdiplam —modulación del splicing de SMN2 en el sistema neuromuscular— y la fisiopatología del acné es biológicamente incoherente. La puntuación alta de TxGNN es casi con certeza un artefacto estadístico del grafo de conocimiento por co-ocurrencia de vocabulario inflamatorio, no una señal de reposicionamiento real.

**Para avanzar se necesita:**
- Identificación de cualquier vía biológica compartida entre la proteína SMN y la patología del acné (actualmente inexistente en la literatura publicada)
- Estudios preclínicos in vitro o in vivo que demuestren actividad de Risdiplam en modelos de acné
- Datos completos de MOA y perfil de seguridad (actualmente ausentes en el Evidence Pack)
- Registro sanitario en Colombia como requisito previo a cualquier evaluación clínica local
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

