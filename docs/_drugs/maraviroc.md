---
layout: default
title: Maraviroc
parent: Solo Predicción del Modelo (L5)
nav_order: 418
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
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
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la información conocida, maraviroc es un antagonista de CCR5, un receptor de quimiocinas que participa en la entrada del VIH a las células y en la migración de células inmunitarias hacia sitios de inflamación.

Las neoplasias endocrinas múltiples (MEN) son síndromes hereditarios impulsados principalmente por mutaciones en genes como MEN1 y RET. Los datos compilados no respaldan un mecanismo plausible mediado por CCR5 en estos síndromes. La relación entre la indicación original y la nueva es, por ahora, solo una asociación del grafo de conocimiento, sin vínculo mecanístico demostrado.

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
| 19989116 | CELSENTRI® 150 MG | Tableta recubierta | MARAVIROC | Cancelado |
| 19989118 | CELSENTRI® 300 MG | Tableta recubierta | MARAVIROC | Cancelado |

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
La predicción (99.82%) se basa solo en el grafo de conocimiento, sin ensayos clínicos ni publicaciones, y no existe un mecanismo plausible mediado por CCR5 en los síndromes MEN. Además, los registros sanitarios en Colombia están cancelados y el perfil de seguridad es relevante.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión de literatura dirigida y estudios preclínicos que evalúen el papel de CCR5 en MEN.
- Evaluar candidatas alternativas con mayor sustento (p. ej., cáncer de mama HER2 positivo, infección por CMV) antes de invertir en esta indicación.
- Aclarar la situación regulatoria, dado que los registros están cancelados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

