---
layout: default
title: Metamizole
parent: Evidencia Moderada (L3-L4)
nav_order: 433
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Metamizole: nueva indicación predicha, Artritis reumatoide (nivel de evidencia L4). Indicación original: Butilescopolamina y analgésicos"
---

# Metamizole
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Metamizol: De Analgésico/Antiespasmódico a Artritis Reumatoide

## Resumen en Una Frase

Metamizol (dipirona) se comercializó en Colombia en una solución inyectable combinada con hioscina (butilescopolamina), indicada como analgésico y antiespasmódico.
El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide**, pero no existen ensayos clínicos y la literatura recuperada trata sobre seguridad e interacciones, no sobre eficacia, por lo que la evidencia que lo respalda es mínima.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Butilescopolamina y analgésicos |
| Nueva Indicación Predicha | Artritis reumatoide |
| Puntaje de Predicción TxGNN | 99.78% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, metamizol es un analgésico y antipirético no opioide con actividad antiinflamatoria débil, atribuida a inhibición de la ciclooxigenasa (COX) y a mecanismos centrales. Su utilidad en dolor y fiebre está ampliamente documentada.

Mecanísticamente, el alivio sintomático del dolor en enfermedades reumáticas es plausible. Sin embargo, esto es distinto de modificar la enfermedad: metamizol no ha demostrado efecto sobre la progresión de la artritis reumatoide. La indicación original (analgesia y espasmo) comparte con la nueva únicamente el componente del dolor.

La literatura recuperada se refiere a la seguridad (agranulocitosis cuando se usa junto con metotrexato), interacciones y patrones de prescripción. El puntaje tan alto del modelo no está respaldado por evidencia clínica, y el riesgo de mielotoxicidad aditiva con metotrexato es una preocupación importante.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [42604876](https://pubmed.ncbi.nlm.nih.gov/42604876/) | 2026 | Farmacovigilancia | Naunyn-Schmiedeberg's Arch Pharmacol | Análisis de EudraVigilance sobre agranulocitosis en reportes de metotrexato para AR con uso concomitante de metamizol |
| [40188149](https://pubmed.ncbi.nlm.nih.gov/40188149/) | 2025 | Farmacovigilancia | Arthritis Res Ther | Reacciones renales y hepáticas por metotrexato en AR y posible influencia de analgésicos concomitantes |
| [33825975](https://pubmed.ncbi.nlm.nih.gov/33825975/) | 2021 | Análisis de reclamaciones | Z Rheumatol | Frecuencia de prescripción de analgésicos en pacientes con enfermedades reumáticas en Alemania |
| [21412604](https://pubmed.ncbi.nlm.nih.gov/21412604/) | 2011 | Transversal | Rev Bras Reumatol | Posibles interacciones farmacológicas en pacientes con AR |
| [23238666](https://pubmed.ncbi.nlm.nih.gov/23238666/) | 2013 | Revisión farmacodinámica | Thromb Haemost | Interacción de AINE con el efecto antiplaquetario de la aspirina |
| [18679134](https://pubmed.ncbi.nlm.nih.gov/18679134/) | 2008 | Transversal | J Clin Rheumatol | Alergias a fármacos más frecuentes en lupus que en AR |
| [2041854](https://pubmed.ncbi.nlm.nih.gov/2041854/) | 1991 | Reporte de caso | Postgrad Med J | Insuficiencia exocrina tipo Sjögren tras necrólisis epidérmica tóxica inducida por metamizol |

Ninguna de estas publicaciones evalúa la eficacia de metamizol en artritis reumatoide.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19959402 (cancelado) | Dipirona 2.5 g + Hioscina 20 mg/5 mL solución inyectable (Laboratorio Biosano S.A.) | Solución inyectable | Butilescopolamina y analgésicos |

---

## Consideraciones de Seguridad

- **Agranulocitosis:** la literatura recuperada asocia metamizol con agranulocitosis, y el uso junto con metotrexato (tratamiento estándar de la AR) plantea un riesgo aditivo de toxicidad hematológica.
- **Interacciones farmacológicas:** no se encontraron interacciones registradas en la base consultada, lo que no equivale a ausencia de interacciones; la literatura señala la relevancia de la combinación con metotrexato.

Para advertencias y contraindicaciones detalladas, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios de eficacia en artritis reumatoide; la literatura se limita a seguridad y patrones de uso. Además, el único registro sanitario en Colombia está cancelado y el riesgo de agranulocitosis con metotrexato es relevante.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y evidencia de un efecto más allá del alivio sintomático
- Estudios clínicos específicos en artritis reumatoide (por ejemplo, como analgésico adyuvante)
- Revisión de las advertencias y contraindicaciones del prospecto
- Evaluación del perfil de seguridad hematológica en pacientes tratados con metotrexato
- Aclarar la situación regulatoria, dado que el registro está cancelado

**Nota:** Entre las demás predicciones, la migraña (L3, estudio comparativo con clonixinato de lisina y revisiones) tiene mayor respaldo clínico que la artritis reumatoide y podría ser una línea de investigación más prometedora.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

