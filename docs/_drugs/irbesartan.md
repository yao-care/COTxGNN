---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 4
---

# Irbesartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Irbesartan: De Hipertensión Arterial a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Irbesartan es un bloqueador de los receptores de angiotensina II (ARB), ampliamente utilizado en la práctica clínica internacional para el tratamiento de la hipertensión arterial y la nefropatía diabética. El modelo TxGNN predice que podría ser efectivo para la **Enfermedad Renal Hipertensiva Maligna**, con un puntaje de predicción del **99.31%**; sin embargo, actualmente **no existen ensayos clínicos ni publicaciones específicas** que respalden directamente esta indicación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial / Nefropatía diabética (indicación establecida internacionalmente; sin registro INVIMA en Colombia) |
| Nueva Indicación Predicha | Enfermedad Renal Hipertensiva Maligna |
| Puntaje de Predicción TxGNN | 99.31% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales de mecanismo de acción (MOA) en la base de datos consultada. Con base en la información conocida, irbesartan pertenece a la clase de los ARB (Bloqueadores de los Receptores de Angiotensina II). Su mecanismo central consiste en antagonizar el receptor AT1, bloqueando la acción vasoconstrictora de la angiotensina II. Esto produce vasodilatación sistémica, reducción de la presión arterial y, a nivel renal, disminución de la presión intraglomerular — lo que confiere efectos nefroprotectores documentados: reducción de la proteinuria y retardo en la progresión del daño renal crónico.

La enfermedad renal hipertensiva maligna se caracteriza por hipertensión severa con daño renal agudo progresivo, en cuya fisiopatología el eje RAAS (renina-angiotensina-aldosterona) desempeña un papel central: la activación excesiva de angiotensina II provoca vasoconstricción intrarrenal, lesión vascular y necrosis fibrinoide. El bloqueo del receptor AT1 por irbesartan atacaría directamente este mecanismo patogénico, lo que otorga coherencia mecanística a la predicción del modelo.

No obstante, la revisión sistemática de la evidencia disponible no identificó ningún ensayo clínico ni publicación que haya estudiado irbesartan específicamente en esta indicación. La predicción se sustenta únicamente en la similitud mecanística y en el modelo de grafos de conocimiento TxGNN, sin respaldo empírico directo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Irbesartan no cuenta con registros sanitarios INVIMA activos en Colombia al momento de la consulta (marzo 2026).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN posee coherencia mecanística clara (bloqueo ARB → inhibición RAAS → nefroprotección en contexto de hipertensión maligna), pero la ausencia total de ensayos clínicos y literatura específica para esta indicación, junto con la falta de registro en Colombia, ubica este candidato en nivel de evidencia L5, insuficiente para avanzar sin investigación adicional previa.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre la clase ARB en el manejo de la hipertensión maligna renal (no limitada a irbesartan)
- Búsqueda dirigida de estudios observacionales, series de casos o registros clínicos sobre ARBs en esta indicación específica
- Verificación del MOA completo en DrugBank (DG002) y obtención de la ficha técnica/prospecto con advertencias y contraindicaciones (DG001)
- Evaluación de la posibilidad de uso con supervisión especializada nefrológica, dado que la indicación comparte fisiopatología directa con el mecanismo de acción conocido del fármaco
- Evaluación de viabilidad regulatoria y trámite de registro INVIMA en Colombia si la evidencia preliminar es favorable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

