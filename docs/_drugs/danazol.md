---
layout: default
title: Danazol
parent: Solo Predicción del Modelo (L5)
nav_order: 193
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
monitor_inn: "DANAZOL"
predicted_indications: ["amenorrhea (disease)", "apocrine adenosis of breast", "blunt duct adenosis of breast", "breast abscess", "fat necrosis of breast", "lactation disease", "breast adenosis", "vulvovaginitis", "vulvitis"]
description: "Danazol: nueva indicación predicha, amenorrea (amenorrhea (disease)) (nivel de evidencia L5). Indicación original: DANAZOL"
---

# Danazol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Danazol: amenorrea (amenorrhea (disease))
{: .text-alpha }

## Resumen en Una Frase

Danazol es un esteroide sintético con actividad androgénica y antigonadotrópica, comercializado en Colombia en cápsulas de 200 mg.
El modelo TxGNN predice que podría ser efectivo para **amenorrea (amenorrhea)**, pero la literatura disponible no estudia directamente el tratamiento de la amenorrea ya establecida: no hay ensayos clínicos registrados y las 20 publicaciones recuperadas son en su mayoría revisiones y estudios antiguos sobre usos relacionados.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DANAZOL |
| Nueva Indicación Predicha | amenorrea (amenorrhea (disease)) |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Danazol (traducción no oficial): «El danazol suprime el eje hipófiso-ovárico.» Texto original en inglés: "Danazol suppresses the pituitary-ovarian axis." ([DailyMed: danazol prescribing information, Chartwell RX, LLC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=55ad6325-16f6-4f0c-a1dc-734847052d0b), versión del 2024-10-10; consultado el 2026-11-19). Según la literatura revisada, danazol es un esteroide sintético con efectos androgénicos que inhibe las gonadotropinas (LH/FSH), suprime la esteroidogénesis ovárica y suprarrenal, y produce atrofia endometrial y amenorrea.

Esa es precisamente la razón de la señal del modelo: danazol **induce** amenorrea. De hecho, se usa para supresión menstrual en endometriosis, sangrado uterino anormal y atención de personas transgénero. Sin embargo, tratar una amenorrea patológica ya existente es un problema distinto, porque el fármaco no la revierte sino que la provoca. Por ello, el puntaje probablemente refleja el efecto inductor de amenorrea del fármaco y no un beneficio terapéutico para pacientes que ya tienen la condición.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguno de los estudios evalúa a danazol como tratamiento de la amenorrea; describen la inducción de amenorrea como efecto farmacológico en otras condiciones.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39051650](https://pubmed.ncbi.nlm.nih.gov/39051650/) | 2024 | Cohorte retrospectiva | Women's Health | Uso de danazol para supresión menstrual en personas transgénero; induce amenorrea con efectos androgénicos reversibles |
| [36434439](https://pubmed.ncbi.nlm.nih.gov/36434439/) | 2023 | Revisión sistemática | Arch Gynecol Obstet | Seguridad y eficacia de gestrinona (fármaco relacionado) en endometriosis, con inducción de atrofia endometrial y amenorrea |
| [2523321](https://pubmed.ncbi.nlm.nih.gov/2523321/) | 1989 | Comparación clínica aleatorizada | Fertil Steril | Gestrinona vs. danazol en endometriosis infértil (39 pacientes, 6 meses) |
| [2140996](https://pubmed.ncbi.nlm.nih.gov/2140996/) | 1990 | Ensayo doble ciego aleatorizado | Fertil Steril | Nafarelina vs. danazol en endometriosis (82 pacientes); ambos reducen la enfermedad activa |
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Revisión | Menopause | Terapias farmacológicas para sangrado uterino anormal |
| [2404115](https://pubmed.ncbi.nlm.nih.gov/2404115/) | 1990 | Revisión | J Reprod Med | Efectos biológicos de danazol: inhibición de gonadotropinas y efectos inmunorreguladores |
| [16280355](https://pubmed.ncbi.nlm.nih.gov/16280355/) | 2006 | Revisión | Hum Reprod Update | Manejo actualizado de la endometriosis |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Revisión | J R Army Med Corps | Métodos para inducir amenorrea en personal militar femenino |
| [6819580](https://pubmed.ncbi.nlm.nih.gov/6819580/) | 1982 | Estudio clínico | Prog Clin Biol Res | Danazol en endometriosis e infertilidad |
| [6210867](https://pubmed.ncbi.nlm.nih.gov/6210867/) | 1982 | Doble ciego | Obstet Gynecol | Efectos de cuatro dosis bajas de danazol en endometriosis pélvica (27 mujeres) |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19905582 | CIPLADANOGEN® 200 MG CÁPSULAS | Cápsula dura | DANAZOL | Vigente |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; entre las principales están:
  - **Mayor**: cisaprida.
  - **Moderada**: antidiabéticos (acarbosa, alogliptina, canagliflozina, dapagliflozina, empagliflozina, glimepirida, glipizida, gliburida, insulina humana, insulina aspart, exenatida, dulaglutida, albiglutida, clorpropamida, acetohexamida), budesonida (incluida la nasal) y eliglustat.
- La literatura también describe una interacción clínicamente relevante con carbamazepina (aumento de aproximadamente el doble en sus niveles) y un caso de rabdomiólisis y pancreatitis con lovastatina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios que evalúen a danazol como tratamiento de la amenorrea; la señal del modelo parece reflejar el efecto inductor de amenorrea del fármaco, lo que lo hace inadecuado para corregir esta condición. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Definir si la pregunta de interés es inducir amenorrea (supresión menstrual) o tratar la amenorrea patológica, ya que la predicción solo tendría sentido en el primer caso.
- Estudios clínicos que evalúen directamente a danazol en la condición predicha.
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones).
- Evaluación de seguridad androgénica y hepática para el uso prolongado.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: danazol prescribing information, Chartwell RX, LLC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=55ad6325-16f6-4f0c-a1dc-734847052d0b) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

