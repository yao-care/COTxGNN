---
layout: default
title: Thimerosal
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Thimerosal
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

# Thimerosal: De Conservante Antimicrobiano a Hipotricosis Simple del Cuero Cabelludo

## Resumen en Una Frase

Thimerosal es un compuesto organomercúrico (etilmercurio) históricamente utilizado como conservante antimicrobiano en vacunas, preparaciones oftálmicas y productos farmacéuticos. El modelo TxGNN predice que podría ser efectivo para **Hipotricosis Simple del Cuero Cabelludo**, con un puntaje de predicción del **99.99%**; sin embargo, actualmente no existen **ensayos clínicos ni publicaciones** que respalden esta dirección. Cabe destacar que el análisis mecanístico sugiere que la totalidad de las predicciones del top-10 corresponden muy probablemente a **señales falsas positivas** generadas por co-ocurrencias de toxicidad en el grafo de conocimiento.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Sin indicaciones aprobadas (uso histórico como conservante/antiséptico) |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) de Thimerosal según las fuentes consultadas. Según la información conocida, Thimerosal (etilmercurio tiosalicilato) es un compuesto organomercúrico con propiedades antimicrobianas, utilizado durante décadas como conservante en multidosis de vacunas, soluciones para lentes de contacto y colirios. Su actividad biocida se basa en la unión covalente del etilmercurio a grupos tiol de proteínas bacterianas, inhibiendo enzimas clave del metabolismo microbiano.

La hipotricosis simple del cuero cabelludo es una condición genética rara caracterizada por escasez congénita de cabello, asociada principalmente a variantes en genes como *LPAR6*, *LIPH* y *DSG4*, que regulan la morfogénesis del folículo piloso. No existe ningún vínculo mecanístico plausible entre la inhibición microbiana por etilmercurio y la corrección de defectos en el desarrollo folicular.

El análisis de racionalidad de reposicionamiento identifica explícitamente esta predicción como una **probable señal falsa positiva**: el grafo de conocimiento (KG) de TxGNN contiene aristas de co-ocurrencia entre Thimerosal y nódulos de enfermedades dermatológicas/capilares, derivadas de su uso histórico como preservante en formulaciones tópicas y oftálmicas, lo que el modelo puede haber interpretado erróneamente como evidencia de eficacia terapéutica. De hecho, la exposición al mercurio orgánico es un **factor causal conocido de alopecia** (síntoma de intoxicación mercúrica), lo que sitúa la dirección de la predicción en contraposición directa con la toxicología establecida.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para ninguna de las indicaciones predichas.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible que vincule Thimerosal con el tratamiento de las indicaciones predichas.

---

## Información de Mercado en Colombia

Thimerosal no cuenta con ningún registro sanitario activo en Colombia. No se encontraron licencias de comercialización en la base de datos consultada.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota de alerta toxicológica:** Aunque los datos formales de seguridad no están disponibles en el Evidence Pack, la literatura científica documenta ampliamente que los compuestos organomercúricos —incluido el etilmercurio— presentan toxicidad sobre el sistema nervioso central, riñones, sistema inmunológico y aparato reproductor. El etilmercurio puede inducir o agravar enfermedades autoinmunes, causar daño en el epitelio corneal y el túbulo renal proximal, y producir alopecia como síntoma de intoxicación. Estos perfiles de toxicidad son directamente relevantes para evaluar la seguridad de cualquier propuesta de reposicionamiento.

---

## Análisis Crítico del Top-10 de Predicciones

El conjunto completo de predicciones presenta un patrón sistemático que merece atención especial:

| Rango | Indicación Predicha | Problema Mecanístico Identificado |
|-------|--------------------|------------------------------------|
| 1 | Hipotricosis simple del cuero cabelludo | Mercurio orgánico es causa conocida de alopecia, no tratamiento |
| 2 | Alopecia | Exposición a Hg → pérdida de cabello (efecto tóxico, no terapéutico) |
| 3 | Hipotricosis congénita con milios | Enfermedad genética (ABCA5); sin vía mecanística posible |
| 4 | Alopecia areata difusa | Hg puede inducir/agravar autoinmunidad; dirección opuesta al objetivo terapéutico |
| 5 | Glaucoma hereditario primario | Hg es tóxico para la malla trabecular; co-ocurrencia por uso en colirios históricos |
| 6 | Glaucoma de ángulo abierto | Sin mecanismo de reducción de presión intraocular |
| 7 | Acidosis tubular renal | Hg orgánico es nefrotóxico para el túbulo proximal (causa RTA, no la trata) |
| 8 | Osteoporosis posmenopáusica | Hg interfiere en osteoblastos (toxicidad), sin mecanismo terapéutico óseo |
| 9 | Enfermedad por déficit de potasio | Inhibición de Na⁺/K⁺-ATPase por Hg = mecanismo tóxico, no terapéutico |
| 10 | Infertilidad masculina por disgenesia gonadal | Hg es toxina reproductiva documentada; KG confunde toxicidad con terapia |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La totalidad de las 10 indicaciones predichas presentan un patrón consistente con **artefactos del grafo de conocimiento**: Thimerosal aparece conectado a enfermedades dérmicas, oftálmicas, renales y reproductivas en el KG de TxGNN debido a su historial como conservante en formulaciones para esas especialidades, pero dicha co-ocurrencia refleja uso como excipiente tóxico —no como agente terapéutico—. En múltiples casos, el mercurio orgánico es precisamente la *causa* de la condición que se predice tratar. No existe evidencia clínica (L5 en las 10 indicaciones), y el perfil toxicológico del etilmercurio contraindica su desarrollo como nuevo agente terapéutico bajo estos vectores de reposicionamiento.

**Para avanzar se necesita:**
- Revisión del modelo TxGNN para identificar y mitigar la confusión entre aristas de "co-ocurrencia como excipiente tóxico" y aristas de "eficacia terapéutica" en el grafo de conocimiento
- Investigación de si existe alguna indicación clínica residual legítima de Thimerosal como antiséptico tópico de uso externo (aplicaciones históricas en heridas menores), que podría justificar un vector de reposicionamiento más fundamentado
- Datos completos de MOA (DrugBank) y advertencias de seguridad (ficha técnica) antes de cualquier evaluación posterior
- Consideración de eliminar o marcar Thimerosal como "candidato no viable" en el pipeline de reposicionamiento, dado el riesgo toxicológico intrínseco del etilmercurio
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

