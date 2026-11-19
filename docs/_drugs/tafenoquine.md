---
layout: default
title: Tafenoquine
parent: Solo Predicción del Modelo (L5)
nav_order: 602
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-29
description: "Tafenoquine: nueva indicación predicha, Mastocitosis sistémica indolente (Smouldering systemic mastocytosis) (nivel de evidencia L5). Indicación original: Succinato de tafenoquina"
monitor_inn: "tafenoquine"
predicted_indications: ["Smouldering systemic mastocytosis"]
---

# Tafenoquine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Tafenoquina: De Antipalúdico (Succinato de Tafenoquina) a Mastocitosis Sistémica Indolente (Smouldering)
{: .text-alpha }

## Resumen en Una Frase

Tafenoquina es un antipalúdico del grupo de las 8-aminoquinolinas; en Colombia su registro sanitario (KOZENIS 50 MG) figura bajo el texto "Succinato de tafenoquina", sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para **mastocitosis sistémica indolente (smouldering systemic mastocytosis)**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: la predicción se apoya únicamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Succinato de tafenoquina (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Mastocitosis sistémica indolente (Smouldering systemic mastocytosis) |
| Puntaje de Predicción TxGNN | 0.9905 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Autorizado pero no comercializado (registros: 1) |
| Número de Registros Sanitarios | 1 (vigentes: 0) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Tafenoquine (traducción no oficial): «La tafenoquina es un fármaco antipalúdico del grupo de las 8-aminoquinolinas. […] La tafenoquina, un antipalúdico del grupo de las 8-aminoquinolinas, es activa contra todos los estadios de las especies de Plasmodium, incluido el hipnozoíto (estadio latente) en el hígado. Los estudios in vitro con las formas eritrocíticas de Plasmodium falciparum sugieren que la tafenoquina podría ejercer su efecto mediante la inhibición de la polimerización de la hematina y la inducción de una muerte del parásito similar a la apoptosis.» Texto original en inglés: "Tafenoquine is an 8-aminoquinoline antimalarial drug. […] Tafenoquine, an 8-aminoquinoline antimalarial, is active against all the stages of Plasmodium species that include the hypnozoite (dormant stage) in the liver. Studies in vitro with the erythrocytic forms of Plasmodium falciparum suggest that tafenoquine may exert its effect by inhibiting hematin polymerization and inducing apoptotic like death of the parasite." ([DailyMed: Arakoda (tafenoquine) prescribing information, 60 Degrees Pharmaceuticals, INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=299e49d8-470f-4779-a010-4a1ee0e0c6cd), versión del 2025-01-10; consultado el 2026-11-19). Según la información conocida, tafenoquina es una 8-aminoquinolina antipalúdica, y mecanísticamente podría ser aplicable a la mastocitosis solo a través de hipótesis no verificadas, como efectos sobre vías de señalización o efectos redox relevantes para la biología del mastocito.

La mastocitosis sistémica indolente suele estar impulsada por la mutación KIT D816V. En los datos compilados para este informe no existe ninguna conexión documentada entre tafenoquina y la señalización de KIT o la proliferación de mastocitos. Tampoco hay ensayos ni literatura que sustenten el vínculo.

Por lo tanto, el puntaje alto (0.9905) es una predicción computacional y debe tratarse únicamente como generadora de hipótesis. La relación entre la indicación original (antipalúdica) y la nueva indicación (trastorno clonal de mastocitos) no es evidente desde el punto de vista terapéutico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20239141 | KOZENIS 50 MG | Tableta dispersable | Succinato de tafenoquina | Temp. no comerc - Vigente |

El único registro (GlaxoSmithKline Colombia S.A.) está cancelado, por lo que actualmente no hay producto vigente en el mercado colombiano.

---

## Consideraciones de Seguridad

**Interacciones Farmacológicas:** se identificaron 21 interacciones potenciales (fuente: DDInter), de las cuales 4 son de nivel **Mayor**:
- Ácido nitroso (Nitrous acid)
- Dofetilida
- Prilocaína
- Vacuna tifoidea (viva)

Las demás son de nivel **Moderado**, entre ellas: metformina, clofarabina, dalfampridina, dapsona (sistémica y tópica), guanfacina y varios anestésicos locales (tetracaína, lidocaína, benzocaína, cocaína, proparacaína, oxibuprocaína y cinchocaína, en presentaciones tópicas, oftálmicas o nasales).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo (nivel L5), sin ensayos, literatura ni mecanismo plausible documentado. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener datos del mecanismo de acción (consulta a DrugBank) y analizar su vínculo con la biología de KIT/mastocitos
- Realizar una revisión de literatura preclínica sobre tafenoquina u 8-aminoquinolinas en mastocitosis
- Obtener y revisar el prospecto (advertencias y contraindicaciones) para el cribado de seguridad
- Evaluar la viabilidad regulatoria, dado que no hay registro vigente en Colombia
- Revisar el significado de la advertencia de interacciones mayores antes de cualquier consideración clínica

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Arakoda (tafenoquine) prescribing information, 60 Degrees Pharmaceuticals, INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=299e49d8-470f-4779-a010-4a1ee0e0c6cd) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

