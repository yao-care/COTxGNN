---
layout: default
title: Lubiprostone
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 10
---

# Lubiprostone
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

# Lubiprostone: De Constipación Crónica a Alopecia

## Resumen en Una Frase

Lubiprostone es un derivado bicíclico del ácido graso estructuralmente relacionado con la prostaglandina E1, aprobado originalmente en Estados Unidos para el tratamiento de la constipación idiopática crónica, el síndrome de intestino irritable con constipación (SII-C) y la constipación inducida por opioides.
El modelo TxGNN predice que podría ser efectivo para **Alopecia**, con un puntaje de confianza del **99.93%**.
Sin embargo, actualmente **no existe ningún ensayo clínico ni publicación científica** que respalde directamente esta dirección de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Constipación idiopática crónica / SII-C / Constipación inducida por opioides (aprobación FDA; sin registros en Colombia) |
| Nueva Indicación Predicha | Alopecia |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por Qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Con base en la información farmacológica conocida, Lubiprostone actúa principalmente activando los canales de cloro tipo 2 (ClC-2) en el epitelio intestinal, lo que aumenta la secreción de fluido intestinal y facilita el tránsito. Adicionalmente, posee actividad agonista sobre los receptores de prostaglandina EP1 y EP4, con menor actividad sobre EP2.

La hipótesis de reposicionamiento para alopecia descansa en la biología de las prostaglandinas en el folículo piloso: la prostaglandina E2 (PGE2), al actuar sobre receptores EP2 y EP4, promueve la entrada del folículo a la fase de crecimiento (anágena), mientras que la prostaglandina D2 (PGD2) ejerce el efecto contrario. La estructura derivada de PGE1 de Lubiprostone le confiere teóricamente la capacidad de modular el microambiente folicular a través de esta vía.

No obstante, esta conexión es marcadamente indirecta: Lubiprostone actúa principalmente en la mucosa intestinal con biodisponibilidad sistémica muy baja, y no existe ninguna evidencia preclínica (in vitro, modelos animales) ni clínica que haya explorado su efecto sobre el ciclo folicular capilar. La predicción del modelo TxGNN captura una relación de red entre entidades biológicas, pero la plausibilidad biológica en este caso es especulativa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Lubiprostone en alopecia.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para Lubiprostone en alopecia.

---

## Información de Mercado en Colombia

Lubiprostone no cuenta con ningún registro sanitario activo en Colombia (INVIMA). El medicamento no está comercializado en el país.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias, contraindicaciones e interacciones farmacológicas no están disponibles en el Evidence Pack actual.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN alcanza un puntaje elevado (99.93%), pero la evidencia de soporte es completamente inexistente: no hay ensayos clínicos, no hay publicaciones en PubMed, y el mecanismo propuesto (actividad EP2/EP4 en folículos pilosos) es altamente especulativo dado que el perfil farmacológico de Lubiprostone está orientado al epitelio gastrointestinal con biodisponibilidad sistémica mínima. La puntuación TxGNN refleja conectividad en redes biológicas, no validación experimental.

**Para avanzar se necesita:**
- Estudios in vitro que evalúen el efecto de Lubiprostone sobre células de papila dérmica o queratinocitos foliculares
- Modelos animales de alopecia (ratón C3H/HeJ o depilación química) para confirmar efecto in vivo
- Aclarar si alguna formulación tópica podría superar la limitación de baja biodisponibilidad sistémica
- Obtener datos completos de MOA desde DrugBank y advertencias desde INVIMA / FDA package insert
- Explorar si las indicaciones de mayor plausibilidad mecanística del mismo Evidence Pack (p. ej., hipertensión pulmonar, enfermedad vascular periférica) ofrecen una ruta regulatoria más viable como prioridad alternativa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

