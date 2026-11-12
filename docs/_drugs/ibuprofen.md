---
layout: default
title: Ibuprofen
parent: Solo Predicción del Modelo (L5)
nav_order: 333
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-12
description: "Ibuprofen: nueva indicación predicha, Displasia acromesomélica, tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: Ibuprofeno"
monitor_inn: "Ibuprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Ibuprofen
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Ibuprofeno: De Ibuprofeno (indicación no detallada) a Displasia acromesomélica, tipo Hunter-Thompson
{: .text-alpha }

## Resumen en Una Frase

Ibuprofeno es un antiinflamatorio no esteroideo (AINE) ampliamente utilizado por sus efectos analgésico y antipirético; en Colombia su único registro sanitario corresponde a una suspensión oral pediátrica.
El modelo TxGNN predice que podría ser efectivo para **displasia acromesomélica tipo Hunter-Thompson**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ibuprofeno (el registro no detalla la indicación; uso conocido: analgésico y antipirético) |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 0.9974 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 19) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el ibuprofeno es un inhibidor no selectivo de la ciclooxigenasa (COX-1 y COX-2), y su eficacia como analgésico y antipirético está bien establecida.

La displasia acromesomélica tipo Hunter-Thompson es un trastorno esquelético causado por variantes de pérdida de función en el gen *CDMP1/GDF5*, que alteran la señalización de BMP. No se identifica un mecanismo plausible que conecte la inhibición de COX con la corrección de ese defecto.

El puntaje alto (0.9974) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, como las displasias esqueléticas raras, y no una relación biológica demostrada. En el mejor de los casos, el ibuprofeno podría servir como manejo sintomático del dolor, lo cual sería cuidado de soporte y no reposicionamiento.

Otras predicciones del modelo (todas L5, sin evidencia y con recomendación Hold) incluyen: síndrome de braquiolmia-amelogénesis imperfecta, miosclerosis, braquiolmia, síndrome de braquidactilia-sindactilia, pseudoacondroplasia y síndrome de microftalmía colobomatosa-displasia rizomélica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 227672 | ADVIL® CHILDREN SUSPENSION ORAL PARA NIÑOS (HALEON COLOMBIA S.A.S) | Suspensión oral | IBUPROFENO |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen de un prospecto):** el modelo asocia el ibuprofeno con posibles contraindicaciones en hipertensión, insuficiencia hepática, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, enfermedad ulcerosa péptica, enfermedad inflamatoria intestinal, lupus eritematoso sistémico, trastornos de la coagulación, accidente cerebrovascular, infarto cerebral e infarto de miocardio, entre otras (epilepsia, EPOC, hipotiroidismo, diabetes, cetoacidosis diabética, hiperplasia prostática benigna, hipotensión, deficiencia de potasio y abuso de sustancias).
- **Interacciones y dianas farmacológicas:** se identificaron 6 dianas: COX-1 (PTGS1), COX-2 (PTGS2), PPAR-γ, ASIC1, SMCT1 (SLC5A8) y el transportador de aminoácidos acoplado a protones 1 (SLC36A1). No hay niveles de severidad de interacción con otros fármacos.
- **Consideración adicional:** la exposición prenatal a AINE plantea preocupaciones de seguridad, lo que desfavorece su uso en malformaciones congénitas del desarrollo.

Consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (L5), sin ensayos ni publicaciones, y no existe un vínculo mecanístico plausible entre la inhibición de COX y la señalización GDF5/BMP.

<!-- review:begin co-lic-20261105-ibuprofen-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción es solo computacional (L5), sin ensayos ni publicaciones, y no existe un vínculo mecanístico plausible entre la inhibición de COX y la señalización GDF5/BMP. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-ibuprofen-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto aprobado (advertencias y contraindicaciones) para completar el análisis de seguridad
- Estudios preclínicos que demuestren un vínculo biológico entre la inhibición de COX y la patogenia de la enfermedad
- Verificar la situación regulatoria actual del ibuprofeno en Colombia (registros vigentes de otros productos)
- Evaluación de la ruta de administración y de la población objetivo (pediátrica, con posible riesgo en etapas del desarrollo)

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

