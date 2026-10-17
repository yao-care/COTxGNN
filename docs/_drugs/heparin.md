---
layout: default
title: Heparin
parent: Solo Predicción del Modelo (L5)
nav_order: 325
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Heparin: nueva indicación predicha, Trastorno primario de liberación plaquetaria (nivel de evidencia L5). Indicación original: Heparina"
monitor_inn: "heparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets"]
---

# Heparin
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

# Heparina: De Heparina (indicación registrada sin detallar) a Trastorno primario de liberación plaquetaria

## Resumen en Una Frase

Heparina es un anticoagulante cuyo registro sanitario en Colombia solo indica "heparina" como indicación, sin mayor detalle.
El modelo TxGNN predice que podría ser efectivo para **trastorno primario de liberación plaquetaria**, pero no hay **ningún ensayo clínico** y las **20 publicaciones** asociadas (de las cuales solo se pudieron revisar 10) no muestran que la heparina trate esta enfermedad; la señal debe considerarse probablemente un falso positivo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Heparina (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la heparina potencia la inhibición de la trombina y del factor Xa mediada por antitrombina, y su eficacia como anticoagulante está establecida.

Sin embargo, los trastornos primarios de liberación plaquetaria son enfermedades hemorrágicas causadas por una secreción deficiente de los gránulos plaquetarios. Un anticoagulante como la heparina tendería a aumentar el riesgo de sangrado, no a tratar la condición. La heparina se relaciona con la biología plaquetaria solo como desencadenante de la trombocitopenia inducida por heparina (HIT), una reacción inmune que es un efecto adverso y no una justificación terapéutica.

El puntaje alto (0.991) probablemente refleja cercanía en el grafo de conocimiento a través de las vías de coagulación y plaquetas. **No se identifica un vínculo mecanístico creíble**, por lo que esta predicción debe tratarse como una señal probablemente falsa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se listan las publicaciones disponibles, priorizando revisiones. Ninguna muestra que la heparina trate este trastorno.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30986390](https://pubmed.ncbi.nlm.nih.gov/30986390/) | 2019 | Revisión | Gastroenterology | Actualización de la AGA sobre coagulación en cirrosis y uso adecuado de anticoagulantes y procoagulantes |
| [11079020](https://pubmed.ncbi.nlm.nih.gov/11079020/) | 2000 | Revisión | Arch Pathol Lab Med | Fisiopatología, diagnóstico y tratamiento de la trombocitopenia inducida por heparina (efecto adverso) |
| [27882374](https://pubmed.ncbi.nlm.nih.gov/27882374/) | 2017 | Revisión | Thromb Haemost | Carga, mecanismos y manejo del tromboembolismo venoso asociado a cáncer |
| [14727968](https://pubmed.ncbi.nlm.nih.gov/14727968/) | 2002 | Revisión | Am J Cardiovasc Drugs | Nuevas dianas de fármacos antitrombóticos y hemostasia plaquetaria |
| [8476260](https://pubmed.ncbi.nlm.nih.gov/8476260/) | 1993 | Revisión | Annu Rev Med | Disfunción endotelial en enfermedad coronaria |
| [8788545](https://pubmed.ncbi.nlm.nih.gov/8788545/) | 1995 | Revisión | Int J Clin Lab Res | Avances clínicos en mastocitosis |
| [28646118](https://pubmed.ncbi.nlm.nih.gov/28646118/) | 2017 | Cohorte | Blood | Anticoagulantes orales directos para tratar la HIT: experiencia de Hamilton y revisión |
| [23839295](https://pubmed.ncbi.nlm.nih.gov/23839295/) | 2013 | Preclínico | Curr Opin Hematol | Expresión celular y actividad biológica de las formas del inhibidor de la vía del factor tisular (TFPI) |
| [30018843](https://pubmed.ncbi.nlm.nih.gov/30018843/) | 2017 | Reporte de caso | J Adv Pract Oncol | Cuidados paliativos en una paciente joven con adenocarcinoma metastásico |
| [27885969](https://pubmed.ncbi.nlm.nih.gov/27885969/) | 2016 | Resumen de congreso | Crit Care | Simposio Internacional de Medicina Intensiva y de Emergencias 2016 |

Nota: solo 10 de las 20 publicaciones fueron incluidas en los datos y revisadas; las otras 10 no pudieron evaluarse.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 206903 | LIOTON® 1000 GEL (cancelado) | Gel tópico | Heparina |
| 19970942 | Heparina sódica inyectable 5.000 U.I./mL (cancelado) | Solución inyectable | Heparina |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no provienen del prospecto): insuficiencia hepática, enfermedades hematológicas, trombocitopenia (incluida la inducida por heparina), trastornos de la coagulación, hemofilia, deficiencia de antitrombina III, defectos plaquetarios cualitativos y trombastenia de Glanzmann, hemorragia intracraneal e intracerebral, desprendimiento de placenta, úlcera péptica activa, colitis ulcerosa y enfermedad inflamatoria intestinal, enfermedad de las vías biliares e ictericia obstructiva, endocarditis infecciosa, retinopatía (diabética e hipertensiva), osteoporosis y arteriosclerosis obliterante.
  Es especialmente relevante que los defectos plaquetarios cualitativos y los trastornos hemorrágicos aparecen como contraindicaciones, lo que va en contra de la indicación predicha.
- **Interacciones Farmacológicas**: se identificaron 614 interacciones. Las de nivel moderado incluyen ácido acetilsalicílico, sulfonilureas y secretagogos de insulina (clorpropamida, glimepirida, glipizida, gliburida, tolbutamida, tolazamida, acetohexamida, repaglinida, nateglinida), además de fenfluramina, dexfenfluramina y sibutramina. Con nivel no clasificado figuran levocarnitina, manitol, calcitriol, vitamina A, pantoprazol, mesalazina y doxiciclina.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura que respalde el uso de la heparina en este trastorno. Mecanísticamente, un anticoagulante podría empeorar el sangrado, y los defectos plaquetarios figuran entre las contraindicaciones del grafo. Además, ambos registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Verificar la predicción con fuentes externas y descartarla como falso positivo, o redirigir la evaluación hacia la otra indicación predicha (deficiencia de proteína C), que tiene mayor plausibilidad mecanística, aunque también carece de evidencia en los datos compilados
- Datos del mecanismo de acción desde DrugBank
- Advertencias y contraindicaciones del prospecto aprobado por INVIMA
- Revisión de las 10 publicaciones no incluidas en los datos
- Aclarar la situación regulatoria, ya que no hay registros vigentes en Colombia
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

