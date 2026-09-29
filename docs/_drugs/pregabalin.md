---
layout: default
title: Pregabalin
parent: Evidencia Moderada (L3-L4)
nav_order: 333
evidence_level: L4
indication_count: 6
---

# Pregabalin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **6** 
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

# Pregabalina: De Dolor Neuropático a Tendinitis

## Resumen en Una Frase

La pregabalina es un ligando de la subunidad alfa2-delta de los canales de calcio dependientes de voltaje, conocido por su uso en dolor neuropático. El registro sanitario colombiano solo consigna el nombre del principio activo, sin texto de indicación.
El modelo TxGNN predice que podría ser efectiva para **tendinitis**, pero hay **0 ensayos clínicos** y solo **6 publicaciones**, todas indirectas: analgesia perioperatoria, casos y estudios preclínicos. Ninguna prueba la pregabalina como tratamiento de la tendinitis.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro INVIMA (el texto solo dice "PREGABALINA"). Uso conocido: dolor neuropático |
| Nueva Indicación Predicha | Tendinitis |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

La pregabalina se une a la subunidad alfa2-delta de los canales de calcio dependientes de voltaje. Esto reduce la liberación de neurotransmisores excitatorios y la sensibilización central del dolor. Por eso se usa en dolor neuropático.

En la tendinitis, el vínculo mecanístico sería indirecto. El fármaco podría aliviar el dolor asociado a la tendinopatía, pero no actúa sobre la patología del tendón (inflamación, degeneración o reparación tisular). Las publicaciones encontradas apoyan solo su uso como analgésico perioperatorio (por ejemplo, tras reparación artroscópica del manguito rotador) y en contextos de dolor neuropático.

El puntaje TxGNN es muy alto (0.997), pero es una predicción basada en grafos de conocimiento y no está respaldado por datos clínicos. Debe leerse como una hipótesis de alivio sintomático, no de tratamiento de la enfermedad.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | ECA | Arthroscopy | Tras reparación artroscópica del manguito rotador, la pregabalina oral perioperatoria logró puntajes de dolor postoperatorio equivalentes al bloqueo interescalénico del plexo braquial. Es analgesia posquirúrgica, no tratamiento de tendinitis. |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Cohorte retrospectiva | J Orthop Sci | Evalúa el efecto analgésico y ahorrador de opioides de la pregabalina tras cirugía del manguito rotador. La literatura previa mostraba resultados contradictorios. |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial | Arthroscopy | Comentario sobre el síndrome piriforme y su tratamiento con neurólisis del ciático y liberación del tendón piriforme. No evalúa pregabalina. |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Reporte de caso | Pain Pract | Caso de atrapamiento del nervio cutáneo femoral posterior por tendinitis de isquiotibiales en un corredor de maratón. No evalúa pregabalina. |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Caso/Revisión | Praxis | Discapacidad asociada a fluoroquinolonas (incluidas tendinopatías) tras ciprofloxacino. Relación tangencial con la pregabalina. |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclínico | Adv Pharmacol Pharm Sci | Un extracto vegetal atenuó la neuropatía periférica inducida por vincristina en ratas. Aparece por coincidencia temática y no evalúa pregabalina en tendinitis. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20190070 | LIMIAR ® 150 MG (Momenta Farmacéutica S.A.S.) | Cápsula dura | Solo se consigna "PREGABALINA" (sin texto de indicación) |

Nota: en el conjunto de datos recibido, los cinco registros listados corresponden al mismo número de registro (20190070). El total reportado es de 20 registros sanitarios.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni estudios que prueben la pregabalina para tendinitis. La literatura solo respalda la analgesia perioperatoria y el dolor neuropático, y el alto puntaje TxGNN no tiene respaldo clínico.

**Para avanzar se necesita:**
- Estudios clínicos que evalúen la pregabalina en tendinopatía, con desenlaces de dolor y función, y no solo analgesia posquirúrgica
- Descargar y analizar el prospecto INVIMA para completar la revisión de advertencias y contraindicaciones
- Datos detallados de mecanismo de acción desde DrugBank
- Considerar priorizar otra indicación predicha: **migraña** tiene evidencia más sólida (nivel L2). Incluye ECA pediátricos frente a valproato y propranolol y estudios preclínicos sobre depresión cortical propagada. Su ensayo de Fase 3 (NCT00447369) fue retirado, por lo que no hay datos confirmatorios.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

