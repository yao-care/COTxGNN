---
layout: default
title: Cyclosporine
parent: Evidencia Moderada (L3-L4)
nav_order: 185
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-14
description: "Cyclosporine: nueva indicación predicha, Enfermedad granulomatosa crónica autosómica recesiva (nivel de evidencia L4). Indicación original: Ciclosporina"
monitor_inn: "Cyclosporine"
predicted_indications: ["granulomatous disease, chronic, autosomal recessive", "brain aneurysm", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "congenital ichthyosiform erythroderma", "fetal erythroblastosis", "brachydactyly-syndactyly syndrome", "prolapse of lacrimal gland"]
---

# Cyclosporine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Ciclosporina: De Indicación Original (Ciclosporina, sin detalle de indicación) a Enfermedad Granulomatosa Crónica Autosómica Recesiva

## Resumen en Una Frase

La ciclosporina es un inmunosupresor inhibidor de la calcineurina, utilizado principalmente para prevenir el rechazo en trasplantes. En los registros sanitarios colombianos solo aparece mencionada como "ciclosporina", sin detalle de indicación.
El modelo TxGNN predice que podría ser efectiva para **enfermedad granulomatosa crónica autosómica recesiva**, pero actualmente solo hay **0 ensayos clínicos** y **1 publicación** indirecta (un estudio de cohorte sobre trasplante de células madre) que se relaciona con esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ciclosporina (el registro sanitario no detalla la indicación) |
| Nueva Indicación Predicha | Enfermedad granulomatosa crónica autosómica recesiva |
| Puntaje de Predicción TxGNN | 99.68% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 6 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la ciclosporina es un inhibidor de la calcineurina que bloquea la activación de los linfocitos T, y su eficacia en la prevención del rechazo de trasplantes está bien establecida. Los datos de farmacología señalan además que se une a la peptidil-prolil isomerasa A (PPIA) y D (PPID), y que interactúa con transportadores como ABCG2, OATP1B1, OATP1B3 y SLC10A1, y con el receptor FPR1.

La enfermedad granulomatosa crónica es una inmunodeficiencia hereditaria causada por un defecto de la NADPH oxidasa. La ciclosporina no corrige ese defecto. El único artículo recuperado trata del trasplante de células madre hematopoyéticas en esta enfermedad, donde la ciclosporina podría formar parte de la profilaxis de la enfermedad injerto contra huésped. Es un apoyo indirecto: la ciclosporina sería un agente de soporte en el trasplante y no un tratamiento de la enfermedad de fondo.

Por tanto, el puntaje alto del modelo no está respaldado por evidencia clínica directa, y la plausibilidad mecanística es limitada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22078471](https://pubmed.ncbi.nlm.nih.gov/22078471/) | 2012 | Cohorte | J Allergy Clin Immunol | Excelente supervivencia tras trasplante de células madre de donante hermano o no emparentado en enfermedad granulomatosa crónica. Es evidencia indirecta: no evalúa la ciclosporina como tratamiento de la enfermedad. |

---

## Información de Mercado en Colombia

Todos los registros sanitarios están cancelados.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 33038 | Sandimmun Neoral cápsulas blandas con microemulsión 25 mg | Cápsula blanda | Ciclosporina |
| 33037 | Sandimmun Neoral cápsula blanda microemulsión 100 mg | Cápsula blanda | Ciclosporina |
| 20070206 | Citabiclos 100 | Cápsula blanda | Ciclosporina |
| 51612 | Sandimmun Neoral cápsula blanda con microemulsión 50 mg | Cápsula blanda | Ciclosporina |
| 24092 | Sandimmun concentrado para perfusión 50 mg/ml | Solución inyectable | Ciclosporina |

Existe un sexto registro cancelado (19937980, Restasis emulsión oftálmica, AbbVie), que no se muestra en la tabla por el límite de cinco registros.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento del modelo asocia la ciclosporina con enfermedades en las que podría estar contraindicada, entre ellas hipertensión, epilepsia, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, enfermedades infecciosas (incluidas las oculares y la conjuntivitis), hipertrigliceridemia, hiperbilirrubinemia (incluido el síndrome de Gilbert), púrpura trombocitopénica, hipertensión intracraneal/pseudotumor cerebral, cáncer y neoplasias (incluidos linfoma y linfoma primario del sistema nervioso central).
- **Interacciones y dianas farmacológicas:** se identificaron 7 interacciones o dianas: FPR1, ABCG2, SLC10A1, OATP1B1, OATP1B3, PPIA y PPID. Varias son transportadores relevantes para la disposición de otros fármacos, por lo que pueden generar interacciones clínicamente importantes.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya en un solo estudio indirecto sobre trasplante de células madre, sin ensayos clínicos, y la ciclosporina no actúa sobre el defecto de fondo de la enfermedad. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción que justifiquen un vínculo con la enfermedad granulomatosa crónica.
- Evidencia clínica directa, o confirmar si el papel de la ciclosporina se limita a la profilaxis de la enfermedad injerto contra huésped en el trasplante.
- Obtener las advertencias y contraindicaciones del prospecto (INVIMA).
- Aclarar la situación regulatoria en Colombia, ya que los 6 registros están cancelados.
- Evaluar el perfil de seguridad (nefrotoxicidad, neurotoxicidad, hipertensión, interacciones) en pacientes pediátricos con esta enfermedad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

