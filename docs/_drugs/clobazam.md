---
layout: default
title: Clobazam
parent: Evidencia Moderada (L3-L4)
nav_order: 167
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Clobazam: nueva indicación predicha, Síndrome de epilepsia relacionada con infección febril (FIRES) (nivel de evidencia L4). Indicación original: Clobazam"
monitor_inn: "CLOBAZAM"
predicted_indications: ["febrile infection-related epilepsy syndrome", "perioral myoclonia with absences", "atypical childhood epilepsy with centrotemporal spikes", "photosensitive occipital lobe epilepsy", "cryptogenic late-onset epileptic spasms", "benign occipital epilepsy", "early-onset epileptic encephalopathy and intellectual disability due to GRIN2A mutation", "restless legs syndrome", "polymicrogyria with optic nerve hypoplasia"]
---

# Clobazam
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

# Clobazam: De Indicación Original (Clobazam, según registro INVIMA) a Síndrome de Epilepsia Relacionada con Infección Febril (FIRES)

## Resumen en Una Frase

Clobazam es una benzodiazepina (1,5-benzodiazepina) que en Colombia contó con registros sanitarios como antiepiléptico/ansiolítico; el texto de indicación registrado se limita al nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de epilepsia relacionada con infección febril (FIRES)**,
pero actualmente solo hay **2 publicaciones** (series y reportes de caso, sobre otros fármacos) y **0 ensayos clínicos** que se relacionan con esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Clobazam (el registro INVIMA no detalla la indicación; solo repite el nombre del principio activo) |
| Nueva Indicación Predicha | Síndrome de epilepsia relacionada con infección febril (FIRES) |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, clobazam es una benzodiazepina que potencia la actividad del receptor GABA-A, y su eficacia como antiepiléptico adyuvante está bien establecida en otros síndromes. Mecanísticamente, podría ser aplicable a convulsiones refractarias como las del FIRES.

El FIRES es una forma de estado epiléptico refractario de inicio reciente (NORSE) que aparece en niños previamente sanos y que suele no responder a los antiepilépticos convencionales; con frecuencia requiere anestésicos en dosis altas. Como clobazam actúa inhibiendo la excitabilidad neuronal por vía GABAérgica, existe una lógica de clase para usarlo en el control de las crisis o en la retirada gradual de agentes anestésicos.

Sin embargo, la evidencia es **indirecta**: los estudios recuperados evalúan lorazepam enteral (serie de casos, 2022) y perampanel (reporte de caso, 2025), no clobazam. Solo respaldan el valor de otras benzodiazepinas y fármacos antiepilépticos como estrategia de apoyo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Serie de casos retrospectiva | Epileptic Disorders | El lorazepam enteral resultó prometedor como estrategia de retirada del midazolam en pacientes con FIRES que respondían a este; no evalúa clobazam |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Reporte de caso | Cureus | En un niño de 13 años con FIRES, perampanel podría reducir la dependencia de barbitúricos; no evalúa clobazam |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 44747 | URBADAN® 20 MG (Sanofi-Aventis) | Tableta | CLOBAZAM (cancelado) |
| 20044091 | OBAX® 10 MG TABLETAS (Humax Pharmaceutical) | Tableta | CLOBAZAM (cancelado) |
| 20262933 | LOGABA® CLOBAZAM 10 MG TABLETAS (MSN Laboratories) | Tableta | CLOBAZAM (cancelado) |
| 29114 | URBADAN® (Sanofi-Aventis) | Tableta | CLOBAZAM (cancelado) |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las principales:
  - **Mayores**: morfina (incluida la forma liposomal) y eliglustat.
  - **Moderadas**: bupropión, aprepitant, omeprazol, esomeprazol, lansoprazol, cimetidina, claritromicina, dexfenfluramina, fenfluramina, dronabinol y metoclopramida.
  - **Menores**: antiácidos como óxido, carbonato e hidróxido de magnesio, hidróxido de aluminio, carbonato de calcio y magaldrato.

No se dispone de advertencias ni contraindicaciones de prospecto; consultar el prospecto para esa información de seguridad. Además, la combinación con opioides (p. ej., morfina) exige especial cautela por el riesgo de depresión respiratoria y sedación aditiva, algo relevante en pacientes críticos con FIRES que ya reciben sedantes.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción del modelo es muy alta (99.82%), pero no hay ensayos clínicos y la literatura disponible es indirecta (otros fármacos, series y reportes de caso). Además, clobazam no tiene registros vigentes en Colombia y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), lo que actualmente bloquea el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar estudios que evalúen clobazam directamente en FIRES/NORSE (series de casos, registros).
- Determinar si existe un producto con registro vigente en Colombia o si habría que iniciar un nuevo trámite regulatorio.
- Evaluar el perfil de interacciones en pacientes críticos (opioides, anestésicos y otros antiepilépticos).

---

### Nota sobre otras indicaciones predichas

Entre las otras nueve predicciones, la de mayor soporte es la de **encefalopatía epiléptica de inicio en la infancia** (puntaje 99.59%, L4), con abundante literatura que incluye clobazam en el síndrome de Lennox-Gastaut. Como clobazam ya está aprobado para ese síndrome en varios mercados, podría no ser un reposicionamiento real; conviene verificarlo con ensayos primarios. Las demás (síndrome de piernas inquietas, polimicrogiria con hipoplasia del nervio óptico, entre otras) solo tienen respaldo predictivo (L5) o evidencia indirecta (L4).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

