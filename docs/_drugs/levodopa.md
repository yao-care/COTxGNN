---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 1
---

# Levodopa
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

# LEVODOPA: De Enfermedad de Parkinson a Encefalitis Subaguda de Rasmussen

## Resumen en Una Frase

Levodopa es el precursor de dopamina más ampliamente utilizado, indicado clásicamente para el tratamiento de la enfermedad de Parkinson y otros trastornos del movimiento dopaminérgicos.
El modelo TxGNN predice que podría ser efectivo para la **Encefalitis Subaguda de Rasmussen**,
sin embargo, actualmente **no existen ensayos clínicos ni publicaciones** que respalden directamente esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (precursor dopaminérgico) |
| Nueva Indicación Predicha | Encefalitis Subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, Levodopa es el precursor directo de la dopamina en el sistema nervioso central: cruza la barrera hematoencefálica y es convertida en dopamina por la enzima DOPA descarboxilasa, restaurando los niveles de neurotransmisor en los ganglios basales. Su eficacia en la enfermedad de Parkinson ha sido ampliamente comprobada durante décadas.

La conexión propuesta con la Encefalitis de Rasmussen es de naturaleza indirecta y especulativa. La dopamina —metabolito activo de Levodopa— ejerce efectos inmunomoduladores: los receptores D1/D5 se expresan en microglía y linfocitos T, con capacidad potencial de inhibir citocinas proinflamatorias vía la vía del AMPc. Dado que la Encefalitis de Rasmussen es una neuroinflamación crónica mediada por linfocitos T CD8+ que afecta un hemisferio cerebral, existe una hipótesis mecanística de que la señalización dopaminérgica podría modular indirectamente la infiltración de células T.

Sin embargo, esta cadena causal carece de validación experimental directa. El modelo TxGNN probablemente detectó similitud a nivel de grafo de conocimiento a través del nodo compartido de neuroinflamación con la enfermedad de Parkinson, no a través de evidencia clínica o preclínica directa. Levodopa no posee actividad antiepiléptica ni inmunosupresora conocida, lo que hace que este reposicionamiento sea altamente especulativo en el estado actual.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Levodopa no cuenta con registros sanitarios activos en Colombia (INVIMA). No se encontraron licencias registradas para este principio activo.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN se basa exclusivamente en similitud de grafo de conocimiento (nivel L5), sin ningún ensayo clínico, estudio observacional ni publicación de literatura que respalde la eficacia de Levodopa en Encefalitis de Rasmussen. La conexión mecanística propuesta es especulativa e indirecta, y Levodopa carece de actividad inmunosupresora o antiepiléptica conocida que pudiera justificar su uso en esta enfermedad autoinmune grave.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) completo desde DrugBank para validar la hipótesis de inmunomodulación dopaminérgica
- Estudios preclínicos (modelos animales de encefalitis autoinmune) que demuestren efecto modificador de la enfermedad con Levodopa o dopamina
- Revisión de literatura sobre el papel de receptores dopaminérgicos en linfocitos T CD8+ en contextos de neuroinflamación
- Evaluación de seguridad completa (advertencias, contraindicaciones, interacciones) mediante descarga del prospecto oficial de TFDA o EMA
- Consideración de si el perfil de efectos adversos de Levodopa (discinesias, hipotensión ortostática, psicosis) es compatible con la población pediátrica afectada por Encefalitis de Rasmussen
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

