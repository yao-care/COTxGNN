---
layout: default
title: Piroxicam
parent: Solo Predicción del Modelo (L5)
nav_order: 518
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Piroxicam: nueva indicación predicha, Síndrome de microftalmia colobomatosa-displasia rizomélica (nivel de evidencia L5). Indicación original: No detallada en el registro sanitario (el texto solo ind…"
monitor_inn: "PIROXICAM"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis", "juvenile idiopathic arthritis"]
---

# Piroxicam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Piroxicam: De Antiinflamatorio No Esteroideo (indicación no detallada en el registro) a Síndrome de Microftalmia Colobomatosa-Displasia Rizomélica
{: .text-alpha }

## Resumen en Una Frase

Piroxicam es un antiinflamatorio no esteroideo (AINE) que cuenta con registros sanitarios en Colombia, aunque estos no detallan la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de microftalmia colobomatosa-displasia rizomélica**, con un puntaje muy alto (99.996%).
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No detallada en el registro sanitario (el texto solo indica "Piroxicam"); clase AINE |
| Nueva Indicación Predicha | Síndrome de microftalmia colobomatosa-displasia rizomélica |
| Puntaje de Predicción TxGNN | 99.996% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin producto vigente) |
| Número de Registros Sanitarios | 5 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según el conocimiento general, piroxicam es un inhibidor no selectivo de la ciclooxigenasa (COX-1/COX-2). Reduce la síntesis de prostaglandinas y, con ello, la inflamación, el dolor y la rigidez en enfermedades inflamatorias articulares.

La nueva indicación predicha es un síndrome del desarrollo, congénito y muy poco frecuente, que afecta el ojo (coloboma y microftalmia) y el esqueleto (displasia rizomélica). No se identificó ningún vínculo mecanístico plausible: esta enfermedad no tiene una patología inflamatoria dependiente de prostaglandinas que la inhibición de la COX pudiera modificar.

El puntaje alto del modelo proviene de asociaciones en un grafo de conocimiento, no de datos clínicos ni de literatura. Por tanto, debe interpretarse como una hipótesis sin sustento y no como una señal de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Los 5 registros sanitarios encontrados están **cancelados**; no hay registros vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19954060 | STOPEN® Cápsula 20 mg | Cápsula dura | Piroxicam |
| 55823 | Piroxicam 20 mg inyectable | Inyectable | Piroxicam |
| 19967377 | OXIFAR® 20 mg cápsulas | Cápsula dura | Piroxicam |
| 19993956 | Piroxicam 0.5 % gel | Gel tópico | Piroxicam |
| 19934890 | OXIVATE® 20 mg cápsulas | Cápsula dura | Piroxicam |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo PrimeKG, no texto de prospecto): hipertensión, enfermedad renal, enfermedad hepática (incluida insuficiencia hepática aguda, hepatitis y daño hepático inducido por fármacos), enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, infarto de miocardio y otras enfermedades cardiovasculares, accidente cerebrovascular y trastornos cerebrovasculares, enfermedades de la coagulación y trombóticas, anemia, úlcera péptica activa, trastornos de la visión y abuso o dependencia de sustancias.
- **Interacciones farmacológicas**: se registraron 100 interacciones en total. Entre las principales, de nivel **moderado**, están:
  - corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona);
  - ácido acetilsalicílico;
  - metformina, glimepirida y clorpropamida;
  - mesalazina y balsalazida;
  - aprepitant;
  - citrato y bicarbonato de potasio;
  - picosulfato y polietilenglicol.

  Famotidina, ranitidina, cimetidina y linaclotida tienen interacciones de nivel **menor**.

Las advertencias y contraindicaciones del prospecto no están disponibles; consultar el prospecto para completar la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para esta indicación (L5) carece de ensayos clínicos, literatura y vínculo mecanístico plausible. Además, el fármaco no tiene registros vigentes en Colombia, lo que limita cualquier desarrollo práctico.

**Nota:** entre las demás indicaciones predichas, la **artritis idiopática juvenil** es la única con respaldo bibliográfico. Incluye estudios pediátricos antiguos y pequeños de piroxicam, uno de ellos comparativo con naproxeno, y dos metaanálisis en red recientes de AINE. Alcanzaría un nivel L3 y tiene una justificación mecanística sólida, aunque sintomática. Podría evaluarse como pregunta de investigación separada.

**Para avanzar se necesita:**
- Descartar o sustentar la hipótesis con evidencia biológica, ya que hoy no existe ninguna.
- Obtener el prospecto con advertencias y contraindicaciones oficiales (INVIMA).
- Completar los datos de mecanismo de acción desde DrugBank.
- Confirmar la situación regulatoria actual del fármaco, dado que todos sus registros están cancelados.
- Si se prioriza la artritis idiopática juvenil, revisar el texto completo de los estudios para confirmar su diseño y resultados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

