---
layout: default
title: Maraviroc
parent: Solo Predicción del Modelo (L5)
nav_order: 418
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Maraviroc: nueva indicación predicha, Neoplasia endocrina múltiple (nivel de evidencia L5). Indicación original: MARAVIROC"
monitor_inn: "MARAVIROC"
predicted_indications: ["multiple endocrine neoplasia", "acne (disease)", "primary cutaneous T-cell lymphoma", "pediatric systemic lupus erythematosus", "primary cutaneous T-cell non-Hodgkin lymphoma", "primary cutaneous B-cell lymphoma", "candidiasis", "complement component 4a deficiency", "cytomegalovirus infection", "HER2 positive breast carcinoma"]
---

# Maraviroc
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

## Maraviroc: De Infección por VIH (CCR5-trópico) a Neoplasia Endocrina Múltiple
{: .text-alpha }

## Resumen en Una Frase

Maraviroc es un antagonista del receptor de quimiocinas CCR5, comercializado en Colombia como Celsentri® (GlaxoSmithKline) y, según la información conocida, utilizado originalmente como antirretroviral contra el VIH. El modelo TxGNN predice que podría ser efectivo para **neoplasia endocrina múltiple**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | MARAVIROC (el registro sanitario no detalla la indicación; según la información conocida, infección por VIH) |
| Nueva Indicación Predicha | Neoplasia endocrina múltiple |
| Puntaje de Predicción TxGNN | 0.9982 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la información conocida, maraviroc es un antagonista de CCR5, un receptor de quimiocinas que participa en la entrada del VIH a las células y en la migración de células inmunitarias hacia sitios de inflamación.

Las neoplasias endocrinas múltiples (MEN) son síndromes hereditarios impulsados principalmente por mutaciones en genes como MEN1 y RET. Los datos compilados no respaldan un mecanismo plausible mediado por CCR5 en estos síndromes. La puntuación de esta nueva indicación proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; por ahora no hay un vínculo mecanístico demostrado.

Por ello, la predicción debe considerarse una hipótesis exploratoria. Cabe señalar que otras predicciones del mismo modelo tienen un sustento biológico algo más razonable, por ejemplo el cáncer de mama HER2 positivo (eje CCL5-CCR5 y resistencia a trastuzumab, evidencia preclínica) y la infección por citomegalovirus (nivel L4, solo evidencia indirecta), aunque tampoco cuentan con ensayos clínicos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para neoplasia endocrina múltiple.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19989116 | CELSENTRI® 150 MG | Tableta recubierta | MARAVIROC | Vigente |
| 19989118 | CELSENTRI® 300 MG | Tableta recubierta | MARAVIROC | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo, no texto de prospecto): enfermedad hepática y lesión hepática inducida por fármacos, infección crónica por virus de hepatitis B y C, enfermedad renal (crónica, insuficiencia renal crónica y terminal), enfermedad coronaria, infarto de miocardio, trombosis coronaria e isquemia miocárdica, hipotensión ortostática, síndrome de taquicardia postural ortostática, atrofia multisistémica, enfermedad de la vesícula biliar, piouréter, hemoglobinopatía y enfermedades infecciosas.
- **Interacciones farmacológicas**: se identificaron 93 interacciones. Entre las principales:
  - **Mayor**: claritromicina.
  - **Moderadas** (ejemplos): aprepitant, dexametasona, cimetidina, eliglustat, naltrexona, clotrimazol, miconazol, rolapitant, cobicistat, deferasirox, diazóxido, fentolamina, prometazina, epoprostenol y fostamatinib.

Consultar el prospecto para información de seguridad complementaria.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción (0.9982) se basa solo en el modelo TxGNN (aprendizaje profundo), sin ensayos clínicos ni publicaciones, y no existe un mecanismo plausible mediado por CCR5 en los síndromes MEN. Además, el perfil de seguridad es relevante.

<!-- review:begin co-lic-20261105-maraviroc-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, los registros sanitarios en Colombia están cancelados y el perfil de seguridad es relevante." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-maraviroc-1 -->

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión de literatura dirigida y estudios preclínicos que evalúen el papel de CCR5 en MEN.
- Evaluar candidatas alternativas con mayor sustento (p. ej., cáncer de mama HER2 positivo, infección por CMV) antes de invertir en esta indicación.
- Aclarar la situación regulatoria.

<!-- review:begin co-lic-20261105-maraviroc-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria, dado que los registros están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-maraviroc-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "los registros sanitarios en Colombia están cancelados y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que los registros están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

