---
layout: default
title: Bosentan
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 9
---

# Bosentan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

Usando el skill `txgnn-pipeline` para orientar la generación del informe de reposicionamiento.

Analizando el Evidence Pack: indicación top es **artritis reumatoide** (Rank 1), nivel L3, sin registros en Colombia. Procedo a generar el informe completo.

---

# Bosentan: De Hipertensión Arterial Pulmonar a Artritis Reumatoide

## Resumen en Una Frase

Bosentan es un antagonista dual de los receptores de endotelina (ETA/ETB), reconocido globalmente como tratamiento de primera línea para la hipertensión arterial pulmonar (HAP).
El modelo TxGNN predice que podría ser efectivo para **Artritis Reumatoide**,
con **1 ensayo clínico** (de relevancia indirecta) y **16 publicaciones** que actualmente exploran esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión Arterial Pulmonar (HAP) |
| Nueva Indicación Predicha | Artritis Reumatoide |
| Puntaje de Predicción TxGNN | 99.80% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales sobre el mecanismo de acción en las bases de datos consultadas. Sin embargo, según la literatura científica publicada, Bosentan es un antagonista dual de los receptores de endotelina tipo A y tipo B (ETA/ETB) que bloquea la acción de la endotelina-1 (ET-1), un potente vasoconstrictor y mediador inflamatorio. Su eficacia en la hipertensión arterial pulmonar ha sido ampliamente comprobada en ensayos Phase 3 (RAPIDS-1/2), donde reduce la resistencia vascular pulmonar al antagonizar los efectos vasoconstrictores y proliferativos de la ET-1 sobre el endotelio pulmonar.

En la artritis reumatoide (AR), el tejido sinovial presenta niveles elevados de ET-1. Esta molécula actúa a través del receptor ETA para promover la liberación de TNF-α, amplificar la cascada inflamatoria sinovial y contribuir a la hipernociception articular (dolor crónico de origen inflamatorio). Al bloquear de forma dual los receptores ETA y ETB, Bosentan podría interrumpir este circuito de retroalimentación inflamatoria, reduciendo tanto la sinovitis como la sensibilización nociceptiva característica de la AR.

Estudios en modelos animales respaldan esta hipótesis: el modelo de artritis inducida por colágeno (CIA) en ratones demuestra que Bosentan mejora significativamente los marcadores de artritis (PMID 22249931), y estudios mecanísticos adicionales confirman que la ET-1 participa activamente en la inflamación articular mediada por citoquinas clave como IL-15 e IL-17 (PMID 16766656, 19969421). No obstante, hasta la fecha no existen ensayos clínicos directos en humanos con AR, lo que limita el nivel de evidencia a **L3** y justifica una recomendación de **Hold** mientras se consolida la base preclínica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06957002](https://clinicaltrials.gov/study/NCT06957002) | Fase 2 | Aún no reclutando | 40 | Evalúa Bosentan + glucocorticoides vs. glucocorticoides solos en Arteritis de Células Gigantes (GCA). Objetivo: superioridad en supervivencia libre de fracaso a 12 meses. Relevancia para AR es indirecta: GCA y AR comparten vías inmuno-inflamatorias (eje TNF/IL-6), pero son entidades clínicas distintas con resultados no solapables. |

> ⚠️ **Nota de relevancia**: El único ensayo clínico identificado tiene como objetivo la Arteritis de Células Gigantes (GCA), **no la Artritis Reumatoide**. Su relevancia para AR es indirecta (Grado C). No existen ensayos clínicos directos de Bosentan en AR registrados a la fecha de corte (2026-05-06).

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22249931](https://pubmed.ncbi.nlm.nih.gov/22249931/) | 2012 | Modelo animal (CIA) | Inflammation Research | Bosentan (antagonista dual ETA/ETB) mejora la artritis inducida por colágeno en ratones; TNF-α induce la expresión de genes del sistema endotelínico en tejido articular inflamado — evidencia preclínica más directa disponible |
| [18515326](https://pubmed.ncbi.nlm.nih.gov/18515326/) | 2008 | Estudio mecanístico animal | J Leukocyte Biology | Las endotelinas modulan la acumulación de neutrófilos y la formación de edema articular en el modelo de artritis por zymosan; los niveles de ET-1 están elevados en plasma y membrana sinovial de pacientes con AR |
| [16766656](https://pubmed.ncbi.nlm.nih.gov/16766656/) | 2006 | Estudio mecanístico animal | PNAS | IL-15 induce hipernociception mecánica en ratones a través de la liberación secuencial de IFN-γ, endotelina y prostaglandina; el antagonismo dual ERA inhibe esta cadena — mecanismo relevante al dolor crónico en AR |
| [19969421](https://pubmed.ncbi.nlm.nih.gov/19969421/) | 2010 | Estudio mecanístico animal | Pain | IL-17 induce hipernociception articular dosis-dependiente en el modelo de artritis por antígeno (mBSA) en ratones; refuerza el papel del eje citoquinas-endotelina en la fisiopatología del dolor en AR |
| [24268012](https://pubmed.ncbi.nlm.nih.gov/24268012/) | 2014 | Revisión | Rheum Dis Clin North Am | HAP asociada a enfermedades del tejido conectivo (incluyendo AR) conlleva mortalidad de 10-15% en el primer año; revisión de opciones terapéuticas con ERA y diagnóstico temprano |
| [19487226](https://pubmed.ncbi.nlm.nih.gov/19487226/) | 2009 | Revisión | Rheumatology (Oxford) | Vasculitis y HAP en LES y síndrome de Sjögren; justificación del uso de ERA en vasculopatías asociadas a enfermedades reumáticas del tejido conectivo |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Revisión | Lupus | HAP como complicación de enfermedades del tejido conectivo incluyendo AR, dermatomiositis y síndrome de Sjögren; sustenta el papel de la ET-1 como diana terapéutica en reumatología |
| [19851110](https://pubmed.ncbi.nlm.nih.gov/19851110/) | 2010 | Revisión | Curr Opin Rheumatology | Revisión del estado del arte en enfermedades cutáneas reumáticas: fisiopatología, medidas de resultado y terapias emergentes; contexto general del campo |
| [20054770](https://pubmed.ncbi.nlm.nih.gov/20054770/) | 2009 | Reporte de caso | Kardiologia Polska | Niña de 8.5 años con síndrome de Eisenmenger tratada con Bosentan que desarrolló simultáneamente artritis reumatoide juvenil; único caso documentado de coexistencia, sin interacción terapéutica adversa reportada |
| [18238768](https://pubmed.ncbi.nlm.nih.gov/18238768/) | 2008 | Revisión | AJHP | Opciones terapéuticas actuales y emergentes para complicaciones de esclerosis sistémica; contextualiza el uso de ERA en el espectro de enfermedades reumáticas con componente vascular |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia actual para Bosentan en artritis reumatoide se limita a modelos animales y estudios mecanísticos preclínicos (Nivel L3), sin ningún ensayo clínico directo en humanos. Aunque el fundamento biológico es plausible —ET-1 elevada en tejido sinovial activa la cascada inflamatoria vía ETA— la brecha entre la evidencia preclínica y la clínica es demasiado amplia para justificar avanzar en este momento. Adicionalmente, Bosentan no se encuentra comercializado en Colombia, lo que representa una barrera regulatoria adicional.

**Para avanzar se necesita:**
- Confirmación formal del mecanismo de acción (MOA) mediante consulta a DrugBank API y ficha técnica oficial
- Obtención del prospecto INVIMA/TFDA para evaluación completa de advertencias, contraindicaciones e interacciones
- Evaluación de interacciones farmacológicas con DMARDs convencionales usados en AR (metotrexato, leflunomida, sulfasalazina)
- Diseño y registro de un ensayo clínico Fase 2 específico en pacientes con AR activa refractaria
- Análisis de viabilidad regulatoria para uso compasivo o importación en Colombia ante INVIMA
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

