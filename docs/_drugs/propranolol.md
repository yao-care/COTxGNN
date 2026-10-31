---
layout: default
title: Propranolol
parent: Solo Predicción del Modelo (L5)
nav_order: 540
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
description: "Propranolol: nueva indicación predicha, Miopatía distal, tipo Tateyama (nivel de evidencia L5). Indicación original: Propranolol"
monitor_inn: "propranolol"
predicted_indications: ["distal myopathy, Tateyama type", "congenital myopathy with excess of thin filaments", "chondroma", "cirrhotic cardiomyopathy"]
---

# Propranolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Propranolol: De Propranolol (indicación no detallada en el registro) a Miopatía distal, tipo Tateyama
{: .text-alpha }

## Resumen en Una Frase

Propranolol es un betabloqueante no selectivo cuyos registros sanitarios en Colombia (tabletas orales) no detallan la indicación aprobada; en ellos solo figura el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **miopatía distal tipo Tateyama**, con un puntaje alto (0.9940), pero **sin ensayos clínicos ni publicaciones** que respalden esta predicción específica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Propranolol (el registro no especifica la indicación; el texto aprobado solo repite el nombre del fármaco) |
| Nueva Indicación Predicha | Miopatía distal, tipo Tateyama |
| Puntaje de Predicción TxGNN | 0.9940 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 4) |
| Número de Registros Sanitarios | al menos 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, propranolol es un betabloqueante no selectivo, usado ampliamente en hipertensión, arritmias, angina, temblor y prevención de hemorragia por várices, entre otros usos. Sin embargo, no hay respaldo en los datos para vincular este mecanismo con la miopatía distal tipo Tateyama.

El análisis de la relación mecanística concluye que no existe un vínculo respaldado: el puntaje del modelo es alto, pero no hay ensayos ni literatura, y plantear un bloqueo betaadrenérgico como racional para esta miopatía distal rara es especulativo.

Por ello, esta predicción debe leerse como una señal computacional que requiere validación, no como una hipótesis terapéutica sustentada.

### Otras predicciones del modelo

| Posición | Enfermedad predicha | Puntaje TxGNN | Nivel de evidencia | Recomendación |
|---|---|---|---|---|
| 2 | Miopatía congénita con exceso de filamentos delgados | 0.9930 | L5 | Hold |
| 4 | Condroma | 0.9914 | L5 | Hold |
| 5 | Miocardiopatía cirrótica | 0.9912 | L5 | Pregunta de investigación |
| 6 | Miocardiopatía | 0.9912 | L5 | Pregunta de investigación |

Las predicciones 5 y 6 son las únicas con literatura asociada. La miocardiopatía (en particular la hipertrófica) es un uso ya establecido de los betabloqueantes, por lo que confirma un uso existente más que un reposicionamiento nuevo. En la miocardiopatía cirrótica la señal es mixta: un reporte de 2024 sugiere que propranolol corrige el intervalo QT prolongado, mientras que otros estudios indican efectos cardiovasculares atenuados y posible daño circulatorio y renal en enfermedad avanzada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para miopatía distal tipo Tateyama.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para miopatía distal tipo Tateyama.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 57771 | Propranolol clorhidrato 40 mg tabletas (Pentacoop S.A.) | Tableta | Propranolol | Vigente |
| 35618 | Propranolol clorhidrato 40 mg tabletas (Tecnoquímicas S.A.) | Tableta | Propranolol | Vigente |
| 35619 | Propranolol 80 mg tabletas (Tecnoquímicas S.A.) | Tableta | Propranolol | Vigente |
| 19978181 | Propranolol 40 mg tabletas (Novamed S.A.S.) | Tableta | Propranolol | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): bronquitis, trastornos de ansiedad, trastorno neurótico, trastorno distímico, enfermedad renal, piouréter, pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico (incluido el pediátrico), miopatía, enfermedad muscular y del músculo esquelético, parálisis periódica familiar, deficiencia de potasio, diabetes mellitus, cetoacidosis diabética, hiperuricemia, hiperparatiroidismo, osteítis fibrosa, coma hepático, encefalopatía hepática, ictericia neonatal, anuria, gota, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo y miastenia gravis.
  - **Dato relevante:** el grafo incluye *miopatía*, *enfermedad muscular* y *enfermedad del músculo esquelético* como contraindicaciones, lo que va en sentido contrario a la nueva indicación predicha y exige especial cautela.
- **Interacciones farmacológicas:** se identificaron 307 interacciones. Entre las principales:
  - **Mayor:** epinefrina.
  - **Moderadas:** hidrocortisona, metscopolamina, hiosciamina, bupropión, triamcinolona, morfina, atropina, dexametasona, lorcaserina, betametasona, fosfato de calcio, budesonida, acetato de calcio, canagliflozina, clorpropamida, cimetidina.
  - **Menores:** ácido ascórbico, ácido acetilsalicílico, óxido de magnesio.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para miopatía distal tipo Tateyama se basa únicamente en el puntaje del modelo, sin ensayos, literatura ni vínculo mecanístico sustentado. Además, el grafo de conocimiento lista la miopatía y las enfermedades musculares como contraindicaciones, y en Colombia no hay registros vigentes del producto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto oficial de INVIMA (advertencias y contraindicaciones), pues su ausencia bloquea el tamizaje de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank para evaluar el vínculo mecanístico.
- Revisión de literatura dirigida sobre betabloqueo en miopatías distales y la plausibilidad biológica.
- Verificar la situación regulatoria: no hay registros vigentes en Colombia, por lo que habría que definir la vía para un producto comercializable.
- Considerar priorizar las predicciones con algo de literatura (miocardiopatía cirrótica) como preguntas de investigación, verificando primero los diseños de los estudios, de los cuales solo se dispuso de títulos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

