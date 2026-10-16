---
layout: default
title: Nifurtimox
parent: Solo Predicción del Modelo (L5)
nav_order: 467
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Nifurtimox: nueva indicación predicha, Analbuminemia congénita (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto aprobado solo indica \"NIFURT…"
monitor_inn: "NIFURTIMOX"
predicted_indications: ["congenital analbuminemia", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "blood group incompatibility", "monoclonal gammopathy", "premalignant hematological system disease", "hematological disease associated with an acquired peripheral neuropathy"]
---

# Nifurtimox
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Nifurtimox: De Indicación Original (no especificada en el registro) a Analbuminemia Congénita

## Resumen en Una Frase

Nifurtimox es un antiprotozoario del grupo de los nitrofuranos, registrado en Colombia bajo la marca Lampit®, cuyo texto de indicación en el registro sanitario solo indica el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **analbuminemia congénita**, con una puntuación muy alta (99.58%), pero con **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "NIFURTIMOX") |
| Nueva Indicación Predicha | Analbuminemia congénita |
| Puntaje de Predicción TxGNN | 99.58% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, nifurtimox es un antiprotozoario nitrofurano cuya actividad depende de la nitrorreducción y la generación de especies reactivas de oxígeno y nitrógeno en los tripanosomas.

La analbuminemia congénita es un trastorno genético raro de la síntesis de albúmina, causado por variantes del gen ALB. **No se identifica ninguna vía plausible** que conecte el mecanismo del fármaco con la corrección de la deficiencia de albúmina. La puntuación alta de TxGNN (0.996) es solo una predicción basada en el grafo de conocimiento y no está respaldada por datos clínicos ni de literatura.

En conclusión, esta predicción debe considerarse una señal computacional sin sustento biológico demostrado.

### Otras indicaciones predichas (todas con evidencia L5 y recomendación Hold)

| Rango | Enfermedad | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Hiperamilasemia | 99.47% | Es un hallazgo de laboratorio, no una enfermedad diana; nifurtimox no modula la amilasa |
| 3 | Síndrome de hiperviscosidad policlonal | 99.47% | Sin efecto conocido sobre inmunoglobulinas ni viscosidad plasmática |
| 4 | Incompatibilidad de grupo sanguíneo | 99.24% | El mecanismo oxidativo podría ser riesgoso en contextos hemolíticos (p. ej., deficiencia de G6PD) |
| 5 | Gammapatía monoclonal | 99.16% | Sin evidencia en trastornos de células plasmáticas |
| 6 | Enfermedad hematológica premaligna | 99.11% | Relación riesgo-beneficio desfavorable en población asintomática |
| 7 | Enfermedad hematológica asociada a neuropatía periférica adquirida | 99.06% | Preocupación de seguridad: nifurtimox se asocia con neuropatía periférica |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20215184 | LAMPIT® 30MG COMPRIMIDOS | Tableta | NIFURTIMOX | Cancelado |
| 20215915 | LAMPIT® 120MG | Tableta | NIFURTIMOX | Cancelado |

Ambos registros pertenecen a BAYER AG y están cancelados; actualmente no hay registros vigentes en Colombia.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (5 registradas):
  - **Etanol**: gravedad **mayor**.
  - **Ritonavir**: gravedad moderada.
  - **Tipranavir**: gravedad moderada.
  - ***Bifidobacterium longum infantis***: gravedad moderada.
  - ***Lactobacillus acidophilus***: gravedad moderada.
- **Alertas derivadas del análisis de las predicciones**: nifurtimox se asocia con neuropatía periférica y otros efectos neurológicos adversos, por lo que su uso en afecciones que ya involucran neuropatía requeriría una justificación sólida. Además, su mecanismo de estrés oxidativo podría ser peligroso en contextos hemolíticos (p. ej., deficiencia de G6PD).

Para advertencias y contraindicaciones formales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre nifurtimox y la analbuminemia congénita. Además, el fármaco no tiene registros vigentes en Colombia y hay señales de seguridad relevantes.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA para advertencias y contraindicaciones (brecha de seguridad bloqueante).
- Completar los datos del mecanismo de acción desde DrugBank.
- Aclarar la indicación original aprobada, ya que el registro solo contiene el nombre del principio activo.
- Realizar estudios preclínicos o de mecanismo que justifiquen un vínculo biológico con la nueva indicación.
- Evaluar la situación regulatoria (registros cancelados) y la compatibilidad de vías de administración.
- Considerar priorizar otras predicciones solo si aparece evidencia independiente; hasta ahora ninguna tiene respaldo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

