---
layout: default
title: Emicizumab
parent: Evidencia Alta (L1-L2)
nav_order: 248
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Emicizumab: nueva indicación predicha, Deficiencia adquirida de factores de coagulación (hemofilia A adquiri… (nivel de evidencia L2). Indicación original: Hemofilia A"
monitor_inn: "EMICIZUMAB"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "thrombotic thrombocytopenic purpura", "fetal and neonatal alloimmune thrombocytopenia", "flood factor deficiency"]
---

# Emicizumab
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Emicizumab: De Hemofilia A a Deficiencia Adquirida de Factores de Coagulación (Hemofilia A Adquirida)

## Resumen en Una Frase

Emicizumab es un anticuerpo biespecífico que se comercializó en Colombia con la marca Hemlibra®; su indicación original figura en los registros únicamente como "EMICIZUMAB", sin texto de indicación detallado. El modelo TxGNN predice que podría ser efectivo para la **deficiencia adquirida de factores de coagulación** (en la práctica, hemofilia A adquirida), con **0 ensayos clínicos registrados** y **20 publicaciones** que respaldan esta dirección, entre ellas estudios prospectivos de fase 2 y 3 de un solo brazo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemofilia A (según información farmacológica compilada; el registro INVIMA solo indica "EMICIZUMAB") |
| Nueva Indicación Predicha | Deficiencia adquirida de factores de coagulación (hemofilia A adquirida) |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

**Nota sobre la selección:** la indicación con mayor puntaje TxGNN es la pseudo-enfermedad de von Willebrand (99.99%), pero carece de evidencia (L5) y de plausibilidad mecanística, por lo que la decisión es *Hold*. Este informe se centra en la deficiencia adquirida de factores de coagulación, la única candidata con evidencia sustancial.

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Según la información farmacológica compilada, emicizumab es un anticuerpo biespecífico que se une al factor IX activado (KD 1,52 µM) y al factor X (KD 0,98 µM), imitando la función cofactora del factor VIII activado. Fue aprobado por la FDA en 2017 para profilaxis en hemofilia A con inhibidores, y en 2018 se amplió a pacientes con hemofilia A independientemente del estado de inhibidores.

En la hemofilia A adquirida (HAA), autoanticuerpos neutralizan el factor VIII endógeno. Como emicizumab actúa mediante el puente FIXa/FX y no depende del FVIII, los inhibidores anti-FVIII no lo neutralizan. Esto ofrece un respaldo biológico directo y coherente para la predicción. Esta lógica no se extiende al resto de las categorías: la evidencia aplica solo a la HAA, no a todas las deficiencias adquiridas de factores.

Por el contrario, las demás predicciones del modelo tienen respaldo débil o nulo. En trastornos plaquetarios (Glanzmann, síndrome de Scott, defectos del receptor de colágeno, trombocitopenias) el defecto no está en la vía del factor VIII. En el síndrome de Scott, la eficacia del propio emicizumab podría verse limitada porque depende de superficies fosfolipídicas. Para la púrpura trombocitopénica trombótica existe una señal de seguridad en contra. El término "flood factor deficiency" no corresponde a una entidad clínica reconocida.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en los datos compilados. Los estudios prospectivos relevantes aparecen en la sección de literatura (por ejemplo, un estudio de fase 3 en Japón y el estudio de fase 2 GTH-AHA-EMI).

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (prioridad a estudios prospectivos, luego cohortes y revisiones):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Fase 3, un solo brazo, prospectivo | J Thromb Haemost | Primer estudio prospectivo multicéntrico de profilaxis con emicizumab en hemofilia A adquirida |
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Fase 2, un solo brazo (GTH-AHA-EMI) | Lancet Haematol | Emicizumab protege del sangrado y permite posponer la inmunosupresión durante las primeras 12 semanas |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Análisis final fase 3 (AGEHA) | Thromb Haemost | Perfil beneficio-riesgo favorable, con y sin inmunosupresión, incluidos pacientes no elegibles para ella |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | Cohorte | Blood Adv | Seguimiento a 2 años de GTH-AHA-EMI: beneficio de supervivencia sostenido al posponer la inmunosupresión |
| [38936699](https://pubmed.ncbi.nlm.nih.gov/38936699/) | 2024 | Análisis comparativo | J Thromb Haemost | Compara emicizumab frente a terapia inmunosupresora en HAA |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | Recomendaciones de consenso | Hamostaseologie | Recomendaciones del grupo GTH-AHA para el uso de emicizumab en HAA |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | Cohorte retrospectiva multicéntrica | Blood Adv | 62 pacientes con HAA tratados fuera de indicación con emicizumab en 12 centros de EE. UU. |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | Revisión narrativa | J Thromb Haemost | Manejo de la HAA en la era de emicizumab |
| [37276345](https://pubmed.ncbi.nlm.nih.gov/37276345/) | 2023 | Serie de casos | Haemophilia | Experiencia con emicizumab en HAA; no existen ensayos aleatorizados |
| [36795341](https://pubmed.ncbi.nlm.nih.gov/36795341/) | 2023 | Revisión | Blood Transfus | Ventajas y desventajas de emicizumab en la prevención y tratamiento del sangrado en HAA |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20152900 | HEMLIBRA® 30 MG/ML SOLUCIÓN INYECTABLE (cancelado) | Solución inyectable | EMICIZUMAB |
| 20135003 | HEMLIBRA® 150 MG/ML SOLUCIÓN INYECTABLE (cancelado) | Solución inyectable | EMICIZUMAB |

Ambos registros, de F. Hoffmann-La Roche, figuran como cancelados; no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas** (5 registradas):
  - **Complejo coagulante anti-inhibidor (aPCC): interacción mayor.** El uso combinado se asocia con riesgo de eventos trombóticos y microangiopatía trombótica.
  - Factor antihemofílico recombinante humano: interacción moderada.
  - Factor VIIa recombinante humano: interacción moderada.
  - Se registran además interacciones farmacológicas con los factores de coagulación X y IX, que corresponden a sus dianas de unión.
- **Señal mecanística de alerta:** en púrpura trombocitopénica trombótica, un fármaco procoagulante podría ser perjudicial, por lo que esta indicación no debe considerarse.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails** (para hemofilia A adquirida). Las demás indicaciones predichas: **Hold**.

**Justificación:**
La hemofilia A adquirida cuenta con un fundamento mecanístico directo y con estudios prospectivos de fase 2 y 3 (de un solo brazo) y cohortes de seguimiento, por lo que se clasifica como L2 y no L1 al no haber ECA aleatorizados. El puntaje de TxGNN por sí solo no es indicador de eficacia: las otras nueve predicciones, aun con puntajes similares, carecen de evidencia.

**Para avanzar se necesita:**
- Verificar el estado regulatorio actual en INVIMA, ya que ambos registros figuran cancelados.
- Obtener y revisar el prospecto de INVIMA para advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Establecer salvaguardas: vigilancia del riesgo trombótico (especialmente con aPCC), seguimiento de la erradicación del inhibidor de FVIII y decisiones sobre inmunosupresión.
- Delimitar la indicación a hemofilia A adquirida, no a deficiencias adquiridas de factores en general.
- Buscar ensayos clínicos registrados (incluido el estudio de fase 3 en Japón) y evidencia comparativa aleatorizada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

