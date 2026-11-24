---
layout: default
title: Cefpodoxime
parent: Solo Predicción del Modelo (L5)
nav_order: 143
evidence_level: L5
indication_count: 2
monitor_inn: "cefpodoxime"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis"]
last_modified_at: 2026-11-24
description: "Cefpodoxime: nueva indicación predicha, Osteoartritis (osteoarthritis) (nivel de evidencia L5). Indicación original: CEFPODOXIMA"
---

# Cefpodoxime
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Cefpodoxime: Osteoartritis (osteoarthritis)
{: .text-alpha }

## Resumen en Una Frase

Cefpodoxima es una cefalosporina oral de tercera generación, cuya licencia local registra únicamente el texto "CEFPODOXIMA" como indicación.
El modelo TxGNN predice que podría ser efectivo para **osteoartritis**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; es solo una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CEFPODOXIMA |
| Nueva Indicación Predicha | Osteoartritis (osteoarthritis) |
| Puntaje de Predicción TxGNN | 0.9925 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 4) |
| Número de Registros Sanitarios | 4 (vigentes: 2) |
| Número de Aprobaciones | Al menos 2 registros sanitarios (la lista puede ser parcial) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Cefpodoxime es (traducción no oficial): «Inhibidor de las proteínas bacterianas de unión a penicilina». Texto original en inglés: "Bacterial penicillin-binding protein inhibitor" ([ChEMBL CHEMBL1672 (cefpodoxime): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1672), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, la cefpodoxima es una cefalosporina oral de tercera generación que inhibe la síntesis de la pared celular bacteriana al unirse a las proteínas de unión a penicilina.

La osteoartritis es una enfermedad degenerativa de la articulación, asociada a degradación del cartílago, estrés mecánico e inflamación de bajo grado. Ningún mecanismo antibacteriano explica de forma plausible un efecto sobre ella, por lo que no se establece un vínculo mecanístico.

El puntaje alto de TxGNN (0.9925) es solo una predicción del modelo TxGNN (aprendizaje profundo). Podría reflejar artefactos de proximidad en la red (por ejemplo, patrones compartidos de interacciones o genes vecinos) y no un efecto terapéutico real.

Como segunda predicción, el modelo también propone **artritis reumatoide** (0.9924), igualmente sin evidencia clínica ni bibliográfica ni vínculo mecanístico reconocido.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

La lista puede ser parcial: se muestran los registros incluidos en los datos compilados.

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19992617 | DOXCEF® SUSPENSION | POLVO PARA RECONSTITUIR A SUSPENSION ORAL | CEFPODOXIMA | Vigente |
| 19992953 | DOXCEF ® 100 | TABLETA RECUBIERTA | CEFPODOXIMA | Vigente |

Se muestran 2 de 4 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 78 interacciones conocidas; las siguientes son de nivel moderado (primeras 20 listadas):
  - Antagonistas H2 y antiácidos: famotidina, ranitidina, cimetidina, nizatidina, ranitidina (citrato de bismuto), hidróxido de aluminio, carbonato de calcio, magaldrato, carbonato de magnesio, hidróxido de magnesio, óxido de magnesio.
  - Inhibidores de la bomba de protones: rabeprazol, omeprazol, dexlansoprazol, esomeprazol, lansoprazol, pantoprazol.
  - Otros: balsalazida, kanamicina, neomicina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo TxGNN, sin ensayos clínicos, literatura ni vínculo mecanístico plausible entre un antibiótico betalactámico y la osteoartritis. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Evidencia directa (preclínica o clínica) que estudie cefpodoxima en osteoartritis.
- Datos del mecanismo de acción y una hipótesis mecanística justificada.
- Advertencias y contraindicaciones del prospecto de INVIMA.
- Revisión de las interacciones farmacológicas si se considerara su uso junto con tratamientos habituales (por ejemplo, antiácidos o inhibidores de bomba de protones).

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL1672 (cefpodoxime): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1672) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

